#! -*- coding: utf-8 -*-
import os
import fnmatch
import re
# typing
from typing import List, Dict, Tuple


def find_all_text_files(path_resource_dir: str)->List[str]:
    return [os.path.join(path_resource_dir, f_name)
            for f_name in fnmatch.filter(os.listdir(path_resource_dir), '*.txt')]


def get_text_data(path_target_file: str)->str:
    """ファイルから情報を獲得する"""
    document = codecs.open(path_target_file, 'r', encoding='shift_jis').read()
    return document


def extract_pre_and_body_document(document: str)->Tuple[str, str, str]:
    """次の規則で前書きと本文を取得する。段落情報を保持するために改行は残しておく。

    1. 点線が出てくる前がすべて前書き
    2. 点線が２回出現した後から「底本」の記述があるところまでが本文

    * Return
    - - -
    - author
    - title
    - body
    """
    end_word = "底本："
    start_line_count = 0

    seq_pre_document_lines = []
    seq_body_lines = []
    seq_lines = document.split('\r\n')
    for line in seq_lines:
        # 終了と開始を判定する
        if line.find(end_word) > -1:
            break
        # 前書き部分の取得
        if start_line_count == 0 and not re.match(r'-{5,100}?', line):
            _pre_doc_line = line.strip('\r\n')
            if len(_pre_doc_line) == 0:
                continue
            else:
                seq_pre_document_lines.append(_pre_doc_line)
            continue
        if re.match(r'-{5,100}?', line):
            start_line_count += 1
            continue
        # 点線範囲内部
        if start_line_count < 2:
            continue
        # 本文取得
        elif start_line_count >= 2:
            _body_line = line.strip('\r\n\u3000')
            if len(_body_line) == 0:
                continue
            else:
                seq_body_lines.append(_body_line)
    else:
        # 底本情報がない場合の処理 とりあえず例外出しておく
        raise Exception()

    if len(seq_pre_document_lines) == 2:
        title = seq_pre_document_lines[0].strip('\r\n')
        author = seq_pre_document_lines[1].strip('\r\n')
    elif len(seq_pre_document_lines) == 3:
        title = seq_pre_document_lines[0].strip('\r\n') + " " + seq_pre_document_lines[1].strip('\r\n')
        author = seq_pre_document_lines[2].strip('\r\n')
    else:
        raise Exception("Unexpected error when pre-document is {}".format(seq_pre_document_lines))

    return author, title, "\n".join(seq_body_lines)


def extract_information(document: str)->Dict[str, str]:
    """テキストをクリーニングして情報獲得

    * Return
    - - -
    - dict
        - title: 作品名
        - author: 作者名
        - reference: 出展
        - body: 本文
    """
    author, title, body_text = extract_pre_and_body_document(document)
    # 本文のルビを除去 #
    cleaned_body_text = re.sub(r"《.+?》|｜|［＃.+?］|〔.+?〕", "", body_text)

    return {
        "author": author,
        "title": title,
        "body": cleaned_body_text
    }


def main(path_resource_dir: str)->List[Dict[str, str]]:
    """次の処理を実行
    1. 処理対象ファイルを集める
    2. テキスト前処理を実施する
    """
    seq_target_file_path = find_all_text_files(path_resource_dir)
    seq_extracted_obj = [extract_information(get_text_data(path_target_file))
                         for path_target_file in seq_target_file_path]
    return seq_extracted_obj


if __name__ == '__main__':
    import json
    import codecs
    seq_cleaned_obj = main('resources/raw_text')
    with codecs.open('resources/cleaned_text.json', 'w', 'utf-8') as f:
        f.write(json.dumps(seq_cleaned_obj, ensure_ascii=False))
