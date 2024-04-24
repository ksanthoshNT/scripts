# def key_present_in_bbox_and_surround(self, documents: list = [], keys: list = [], results_extraction: dict = {},
#                                      lc_key_values: dict = {},
#                                      source_documents: list = [], source_keys: list = [], dest_documents: list = [],
#                                      dest_keys: list = [],
#                                      results_classification: dict = {}, condition: dict = {}, status: bool = None,
#                                      condition_dict: dict = None):
#     doc_fail = {}
#     docs_fail = []
#
#     return True, doc_fail, docs_fail
import json
import os
from typing import List
import re

from loguru import logger


def get_intersection_percentage(bb1, bb2):
    """
    Finds the percentage of intersection  with a smaller box. (what percernt of smaller box is in larger box)
    """
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])
    if x_right < x_left or y_bottom < y_top:
        return 0.0
    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    # compute the area of both AABBs
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])
    # min_area = min(bb1_area,bb2_area)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area

    if bb1_area > bb2_area:
        intersection_percent = intersection_area / bb2_area
    else:
        intersection_percent = intersection_area / bb1_area
        if intersection_percent < 0.5:
            intersection_percent = 1  # if ocr bounding box is big then we need to consider the entire token if the intersection is less than o.5 also

    assert intersection_percent >= 0.0
    assert intersection_percent <= 1.0

    # print(f"Intersection Percentage: {intersection_percent}")
    return intersection_percent


def sort_the_coordinates(intersection_points):
    intersection_points = list(sorted(intersection_points, key=intersection_points[0][1]))
    return intersection_points




def get_filter_ocr_coordinates(ocr_data, range):
    intersected_data: List = []

    for data in ocr_data:
        word_coordinates = data["word_coordinates"]
        text = data["text"]
        if get_intersection_percentage(range, word_coordinates) > 0.3:
            intersected_data.append((word_coordinates, text))
    sorted_coordinates = sort_the_coordinates(intersected_data)
    return sorted_coordinates


def merge_text(coordinates):
    merged_text = ""
    for _, text in coordinates:
        merged_text = merged_text + text
    return merged_text


def key_present_in_bbox_and_surround_tarun(self, documents: list = [],                                      keys: list = [], \
                                     results_extraction: dict = {},                                      lc_key_values: dict = {},
                                     source_documents: list = [],
                                     source_keys: list = [],
                                     dest_documents: list = [],
                                     dest_keys: list = [],
                                     results_classification: dict = {},
                                     condition: dict = {},
                                     status: bool = None,
                                     condition_dict: dict = None,
                                     ocr_data: str = None):
    doc_fail = {}
    docs_fail = []

    doc_name: str = ""
    key_name: str = ""

    # key value
    value = results_extraction[doc_name][key_name]["value"]

    coordinates = results_extraction[doc_name][key_name]["coordinate"]
    x1, y1, x2, y2 = coordinates
    # check the cropped part of an image
    padding: int = 2200
    x1, y1, x2, y2 = x1 - padding, x2 + padding, y1 - padding, y2 + padding

    ocr_coordinates = get_filter_ocr_coordinates(ocr_data, range=((x1, y1), (x2, y2)))
    merged_text = merge_text(ocr_coordinates)

    possible_reference_date = "(for on behalf of agent | for agent| by agent)[a-zA-Z0-9\s]*\n$"

    pattern_reference_date = '|'.join(map(re.escape, possible_reference_date))
    reference_data = re.findall(pattern_reference_date, value)[0] if re.findall(pattern_reference_date, value) else ""

    if value and reference_data:
        return True

def get_util(condition_dict:dict, ocr_path:str, results_extraction:dict, padding:str, doc_name=None, key_name=None,
             source_documents=None):
    word_exists = condition_dict.get("value", None)
    if word_exists is None:
        word_exists = results_extraction[doc_name][key_name]["value"]

    # key value
    with open(os.path.join(ocr_path, source_documents[0] + '.json'), 'r') as file_:
        ocr_data = json.load(file_)
        # ocr_data = '\n'.join(file_.readlines())
    # ocr_data = ocr_data.lower()

    # value = results_extraction[doc_name][key_name]["value"]

    coordinates = results_extraction[doc_name][key_name]["coordinate"]
    x1, y1, x2, y2 = coordinates

    # check the cropped part of an image

    x1, y1, x2, y2 = x1 - padding, x2 + padding, y1 - padding, y2 + padding
    range_coord = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    return word_exists,ocr_data,range_coord

def operation_check(self, value1, value2, operation):
    logger.debug(value1)
    logger.debug(f"operration : {operation}")
    logger.debug(value2)
    if operation in ["ne", "!=", "notequal"]:
        # logger.debug("hurray")
        return value1 != value2
    elif operation in ["eq", "==", "equal"]:
        # logger.debug("nothurray")
        return value1 == value2
    elif operation in ["gte", ">=", "greaterthanequal"]:
        # logger.debug("nothurray")
        return value1 >= value2
    elif operation in ["lte", "<=", "lessthanequal"]:
        # logger.debug("nothurray")
        return value1 <= value2
    elif operation in ["lt", "<", "lessthan"]:
        # logger.debug("nothurray")
        return value1 < value2
    elif operation in ["gt", ">=", "greaterthan"]:
        # logger.debug("nothurray")
        return value1 > value2

    return value1 == value2
def count_bbox_tokens_inside_key(self, documents: list = [], keys: list = [], \
                                         results_extraction: dict = {}, lc_key_values: dict = {},
                                         source_documents: list = [],
                                         source_keys: list = [],
                                         dest_documents: list = [],
                                         dest_keys: list = [],
                                         results_classification: dict = {},
                                         condition: dict = {},
                                         status: bool = False,
                                         condition_dict: dict = None,
                                         ocr_path: str = None, padding: int = 2200,mapping_data:dict ={}):
        doc_fail = {}
        docs_fail = []
        doc_name: str = source_documents[0]
        key_name: str = source_keys[0]

        avg_terms_and_condition = condition_dict.get("variable")
        avg_tac_count = mapping_data.get(avg_terms_and_condition)
        __operation = condition_dict.get("operation",None)

        word_exists, ocr_data, range_coord = get_util(condition_dict,ocr_path,results_extraction,padding)
        count_of_tokens = len(ocr_data)
        ocr_coordinates = get_filter_ocr_coordinates(ocr_data, range=range_coord)
        count_of_tokens_after_filter = len(ocr_coordinates)

        status = operation_check(value1=count_of_tokens_after_filter,value2=count_of_tokens_after_filter,operation=__operation)

        return status, docs_fail, doc_fail

def find_parties(party_types,merged_text):
    return [party for party in party_types if re.findall(re.escape(party),merged_text,flags=re.IGNORECASE)]

def behalf_of_extraction(self, documents: list = [],keys: list = [], results_extraction: dict = {},                                      lc_key_values: dict = {},
                                     source_documents: list = [],
                                     source_keys: list = [],
                                     dest_documents: list = [],
                                     dest_keys: list = [],
                                     results_classification: dict = {},
                                     condition: dict = {},
                                     status: bool = None,
                                     condition_dict: dict = None,
                                     ocr_path: str = None,party_name: list = None,   padding: int = 2200):
    doc_fail = {}
    docs_fail = []

    doc_name: str = ""
    key_name: str = ""
    found_party_list: list = []

    word_exists, ocr_data, range_coord = get_util(condition_dict, ocr_path, results_extraction, padding)

    ocr_coordinates = get_filter_ocr_coordinates(ocr_data, range=range_coord)
    merged_text = merge_text(ocr_coordinates)

    behalf_check = ["for on behalf of","for behalf of","for behalf"]
    party_types = ["carrier","agent","master"]
    party_types.extend(party_name)


    behalf_status = find_parties(party_types=behalf_check,merged_text = merged_text)
    if behalf_status:
        found_party_list = find_parties(party_types = party_types,merged_text = merged_text)

    return found_party_list



