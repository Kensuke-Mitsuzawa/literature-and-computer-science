#! -*- coding: utf-8 -*-
from DocumentFeatureSelection import interface
from JapaneseTokenizer import MecabWrapper
# typing
from typing import Dict, List, Tuple, Any
# else
import json
import codecs

"""作品からキーワード名詞の獲得をするためのスクリプト"""


def make_format_input_data(seq_document_object: List[Dict[str, str]],
                           tokenizer_obj: MecabWrapper,
                           unit: str="all",
                           stopwords: List[str]=None,
                           pos_condition: List[Tuple[str, ...]]=(
                                   ("名詞", "サ変接続"), ("名詞", "ナイ形容詞語幹"), ("名詞", "形容動詞語幹"), ("名詞", "一般"),
                                   ("名詞", "固有名詞"), ("名詞", "代名詞"))
                           )->Dict[str, List[List[str]]]:
    """DocumentFeatureSelectionに適した入力フォーマットを作成する。

    * Parameter
    - - -
    - unit: str
        - TFDIDFにおける１文書の単位を設定する。sentenceは１文を１文書とみなす。だから文書数のかさましをするイメージ
        特定の作品のみに出現する単語はIDF値が高くなるはず(logを取る前の値が大きくなるはず N(全文書)/N(単語tが出現する文書)だから)、
        だから"all"の方がいいと思う。

    * Return
    - - -
    - dict
        - {title: [ [word] ]}
    """
    if unit == "sentence":
        seq_title_and_words_obj = {
            doc_obj["title"]:
                [tokenizer_obj.tokenize(sent).filter(list(pos_condition), stopwords=stopwords).convert_list_object()
                 for sent in doc_obj["body"].split("。") if not len(sent) == 0]
            for doc_obj in seq_document_object}
    elif unit == "all":
        seq_title_and_words_obj = {
            doc_obj["title"]:
                [tokenizer_obj.tokenize(doc_obj["body"]).
                     filter(list(pos_condition), stopwords=stopwords).convert_list_object()]
            for doc_obj in seq_document_object}
    else:
        raise Exception()

    return seq_title_and_words_obj


def extract_keywords_tf_idf(dict_input_obj_tfidf: Dict[str, List[List[str]]])->List[Dict[str, Any]]:
    """TF-IDFで各文書からキーワードを獲得する"""
    result_obj = interface.run_feature_selection(dict_input_obj_tfidf, method='tf_idf').\
        convert_score_matrix2score_record()
    return result_obj


def extract_keywords(seq_document_object: List[Dict[str, str]],
                     tokenizer_obj: MecabWrapper)->Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """テキストからキーワードを獲得する
    名詞と形容詞を対象とする。が、「名詞だけのTFIDF値」と「形容詞だけのTFIDF値」と別にする。
    直感的に、名詞表現と形容表現は同種として扱ってはいけない気がする。
    """
    dict_input_obj_tfidf_nouns = make_format_input_data(seq_document_object, tokenizer_obj, unit="all")
    seq_result_tfidf_nouns = extract_keywords_tf_idf(dict_input_obj_tfidf_nouns)

    dict_input_obj_tfidf_adj = make_format_input_data(seq_document_object, tokenizer_obj, unit="all",
                                                           pos_condition=[("形容詞", "自立")],
                                                           stopwords=["ない", "無い"])
    seq_result_tfidf_adj = extract_keywords_tf_idf(dict_input_obj_tfidf_adj)

    return seq_result_tfidf_nouns, seq_result_tfidf_adj


if __name__ == '__main__':
    path_input_data = '../resources/cleaned_text.json'
    seq_input_object = json.loads(open(path_input_data, 'r').read())
    mecab_obj = MecabWrapper(dictType="all", pathUserDictCsv="../user_dic_nakazima.txt")
    result_tfidf_nouns, result_tfidf_adj = extract_keywords(seq_input_object, mecab_obj)
    with codecs.open('../processed_resources/tfidf-nouns.json', 'w', 'utf-8') as f:
        f.write(json.dumps(result_tfidf_nouns, ensure_ascii=False))
    with codecs.open('../processed_resources/tfidf-adj.json', 'w', 'utf-8') as f:
        f.write(json.dumps(result_tfidf_adj, ensure_ascii=False))