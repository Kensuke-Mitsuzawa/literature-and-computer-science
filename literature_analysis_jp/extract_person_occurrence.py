#! -*- coding: utf-8 -*-
from JapaneseTokenizer import MecabWrapper
# typing
from typing import Dict, List, Tuple, Any
# else
from itertools import combinations, chain
from collections import Counter
import json
import codecs


"""人物名どうしの共起によって、人物間の関係取得を試すスクリプト
代名詞を含むバージョンと、人名だけのアプローチの２つを試す
"""


def pre_process(document_text: str)->List[str]:
    """段落ごとに文書を区切る。改行コードで区切ってあるところが段落の境目"""
    return document_text.split("\n")


def extract_person_co_occurrence(paragraph_text: str,
                                 mecab_obj: MecabWrapper,
                                 pos_condition: List[Tuple[str, ...]])->List[Tuple[str, str]]:
    """段落ないにおける人物名共起を獲得する"""
    seq_person_names = mecab_obj.tokenize(paragraph_text).\
        filter(pos_condition=pos_condition).convert_list_object()
    seq_co_occurrence_pair =[
        tuple(sorted(t_comb)) for t_comb in combinations(seq_person_names, 2)
        if not t_comb[0] == t_comb[1]
    ]
    return seq_co_occurrence_pair


def compute_jaccard_score(counter_obj_pair_co_occurrence: Counter)->List[Dict[str, float]]:
    """Jaccard係数を計算してみる"""
    dict_freq_single_item = {}
    for t_pair in counter_obj_pair_co_occurrence:
        freq = counter_obj_pair_co_occurrence[t_pair]
        if t_pair[0] in dict_freq_single_item:
            dict_freq_single_item[t_pair[0]] += freq
        else:
            dict_freq_single_item[t_pair[0]] = freq

        if t_pair[1] in dict_freq_single_item:
            dict_freq_single_item[t_pair[1]] += freq
        else:
            dict_freq_single_item[t_pair[1]] = freq

    seq_jaccard_score_obj = []
    for t_pair in counter_obj_pair_co_occurrence:
        pair_freq = counter_obj_pair_co_occurrence[t_pair]
        freq_a = dict_freq_single_item[t_pair[0]]
        freq_b = dict_freq_single_item[t_pair[1]]
        jaccard_score = pair_freq / (freq_a + freq_b - pair_freq)
        seq_jaccard_score_obj.append({"pair": t_pair, "jaccard_score": jaccard_score, "freq": pair_freq})
    else:
        return list(sorted(seq_jaccard_score_obj, key=lambda obj: obj["jaccard_score"], reverse=True))


def extract_person_occurrence(seq_document_object: List[Dict[str, str]],
                              tokenizer_obj: MecabWrapper)->Tuple[Dict[str, Any], Dict[str, Any]]:
    """main関数"""
    seq_paragraph_text = [p_text for doc_obj in seq_document_object for p_text in pre_process(doc_obj["body"])]
    seq_pair_person_name_only = Counter(chain.from_iterable([
        extract_person_co_occurrence(p_text, tokenizer_obj, [("名詞", "固有名詞", "人名")])
        for p_text in seq_paragraph_text]))
    seq_pair_person_name_pronoun = Counter(chain.from_iterable([
        extract_person_co_occurrence(p_text, tokenizer_obj, [("名詞", "固有名詞", "人名"), ("名詞", "代名詞")])
        for p_text in seq_paragraph_text]))
    seq_jaccard_person_name_only = compute_jaccard_score(seq_pair_person_name_only)
    seq_jaccard_person_name_pronoun = compute_jaccard_score(seq_pair_person_name_pronoun)
    return seq_jaccard_person_name_only, seq_jaccard_person_name_pronoun


if __name__ == "__main__":
    path_input_data = '../resources/cleaned_text.json'
    seq_input_object = json.loads(open(path_input_data, 'r').read())
    mecab_obj = MecabWrapper(dictType="all", pathUserDictCsv="../user_dic_nakazima.csv")
    seq_jaccard_person_name_only, seq_jaccard_person_name_pronoun = extract_person_occurrence(seq_input_object, mecab_obj)

    with codecs.open('../processed_resources/jaccard_person_name_only.json', 'w', 'utf-8') as f:
        f.write(json.dumps(seq_jaccard_person_name_only, ensure_ascii=False))
    with codecs.open('../processed_resources/jaccard_person_name_pronoun.json', 'w', 'utf-8') as f:
        f.write(json.dumps(seq_jaccard_person_name_pronoun, ensure_ascii=False))