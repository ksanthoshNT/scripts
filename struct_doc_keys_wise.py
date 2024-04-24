from test_classify_key_word_based import get_ocr_vision_api_charConfi, image_to_base64
import os
import json
import os
import base64
import requests
import json
import numpy as np

import cv2
import numpy as np


def informat_structed_doc(format1):
    format2 = []
    print('================================')
    print(format1)
    print('================================')

    for item in format1:
        new_item = {
            "word": item["word"],
            'confidence': item["confidence"],
            "word_coordinates": [
                item["x1"],
                item["y1"],
                item["x2"],
                item["y2"]
            ],
            "x1": item["x1"],
            "y1": item["y1"],
            "x2": item["x2"],
            "y2": item["y2"],
            "top": item["top"],
            "left": item["left"]
        }
        format2.append(new_item)

    return format2





def draw_coordinates_and_values(image_path, data_dict):
    # Read the image
    img = cv2.imread(image_path)

    # Loop through the dictionary
    for key, value_dict in data_dict.items():
        coordinates = value_dict['coordinates']
        x_min, y_min, x_max, y_max = coordinates

        # Draw a rectangle
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # Write the value on top of the rectangle
        value = value_dict['value']
        cv2.putText(img, value, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the image with drawn coordinates and values
    cv2.imwrite('result.png', img)

# Example usage









if __name__ == '__main__':


    page_no = 'page1'
    doc_class = 'lc_application'
    sample_image_path = '/home/ntlpt19/TF_testing_EXT/all_filled_data_samples/lc application/lc_app_filled_1.jpg'
    key_path='/home/ntlpt59/MAIN/rul_fix/spheric-time-383904-f1b421d86eef.json'
    coordinates, all_text = get_ocr_vision_api_charConfi(sample_image_path,KEY_PATH=key_path)
    base_64_img = image_to_base64(sample_image_path)
    url = 'http://0.0.0.0:8088/trade_finance/structuredDocumentExtraction'
    with open('export_letter.json', 'r') as exp:
        export_letter = json.load(exp)
    print(export_letter)
    export_letter = export_letter['page0']

    final_responce = {}
    extracting_keys = []
    non_extracting_keys = []
    for key_ in export_letter.keys():
        key_name = export_letter[key_]['name']
        # try:
        input_json_struct = {'formName': doc_class, 'formImage': base_64_img, 'pageNumber': page_no, 'ocrData': {'data': informat_structed_doc(coordinates), "text": all_text},'fieldIdInput': key_}
        with open('input_json.json', 'w') as jsonfile:
            json.dump(input_json_struct, jsonfile)
        exit('>>>>>>>>>>>>>>>>>>>')
        try:
            response = requests.post(url, json=input_json_struct)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            # Attempt to parse JSON if the response is not empty
            if response.text:
                result_with_doc_creation = response.json()
                first_key, first_value = next(iter(result_with_doc_creation.items()))
                print('first_value >>>>>>>>>>>>', first_value)
                first_value = first_value[0]
                first_key_, first_value_ = next(iter(first_value.items()))
                print('first_value ?????????????', first_value_)

                if first_value_['value'] in [None, '']:
                    print(result_with_doc_creation)
                    non_extracting_keys.append(key_name)
                else:
                    cordinates = first_value_['Field_coordinates']
                    final_responce[key_name] = {'value':first_value_['value'], "coordinates": [cordinates[0][0], cordinates[0][1], cordinates[1][0], cordinates[1][1]]}
                    extracting_keys.append(key_name)
                    print(result_with_doc_creation)
            else:
                non_extracting_keys.append(key_name)
                print("Empty response received.")
        except:
            non_extracting_keys.append(key_name)

    filename = 'extracting_keys.txt'
    with open(filename, 'w') as file:
        for key in extracting_keys:
            file.write(key + '\n')

    filename = 'non_extracting_keys.txt'
    with open(filename, 'w') as file:
        for key in non_extracting_keys:
            file.write(key + '\n')


    with open('final_resuls.json', 'w') as json_file:
        json.dump(final_responce, json_file)

    draw_coordinates_and_values(sample_image_path,final_responce)