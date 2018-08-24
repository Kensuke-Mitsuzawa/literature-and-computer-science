#! -*- coding: utf-8 -*-
from knp_utils import knp_job, models, KnpSubProcess
import pyknp
import json
import shutil
from typing import List, Dict
import logging
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

"""テキストから登場人物の特徴を獲得する。
係り受け解析と述語こう構造の関係により取得をする。
"""

PATH_JUMAN_COMMAND="juman"
PATH_KNP_COMMAND="knp"
PATH_JUMANPP_COMMAND="jumanpp"


def make_format_input_document(document_obj: Dict[str, str],
                               mode: str="sentence")->List[Dict[str, str]]:
    """knp_utilsの入力に適した形にする。文は句点で区切る。

    * parameter
    - - -
    - document_obj: dict
        - {"body": str, "title": str}
    - mode: str
        -

    * Return
    - - -
    - dict
        - {"text-id": str, "text": str}
    """
    seq_input_sentence_obj = [{"text-id": "{}-{}".format(document_obj["title"], str(sent_number)), "text": sent}
                              for sent_number, sent
                              in enumerate(document_obj["body"].split("。"))]
    return seq_input_sentence_obj


def parse_text(input_document: List[Dict[str, str]], path_destination_db: str):
    """KNPで構文解析を実施する"""
    logger.debug("Parsing sentences with KNP...")
    result_obj = knp_job.main(seq_input_dict_document=input_document,
                              n_jobs=-1,
                              process_mode='everytime',
                              is_normalize_text=True,
                              is_get_processed_doc=True,
                              juman_command=PATH_JUMANPP_COMMAND,
                              knp_command=PATH_KNP_COMMAND,
                              is_delete_working_db=False)
    path_processed_db = result_obj.path_working_db
    shutil.copy(path_processed_db, path_destination_db)
    return True


def extract_feature_dependency():
    pass


def test():
    """"""
    pass


if __name__ == '__main__':
    path_cleaned_text = "../resources/cleaned_text.json"
    path_save_destination_db = "../resources/parsed_data_db.sqlite3"
    seq_title2document_obj = json.loads(open(path_cleaned_text, 'r').read())
    seq_input_format_knp_utils = [d
                                  for document_obj in seq_title2document_obj
                                  for d in make_format_input_document(document_obj)]
    parse_text(seq_input_format_knp_utils, path_save_destination_db)