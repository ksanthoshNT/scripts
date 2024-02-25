import base64
import json
import sys

import requests
from PIL import  Image

from ocr_coordinates_with_confidence import extract_text_and_coordinates
from struct_doc_keys_wise import informat_structed_doc
from test_classify_key_word_based import get_ocr_vision_api_charConfi
import pytesseract

def call_structure_document(img_path,doc_name,url,fieldIdInput = None,pagenum = None):
    with open(img_path, 'rb') as file:
        img = file.read()
    imgb64 = base64.b64encode(img).decode('utf-8')
    # ocr_coords = extract_text_and_coordinates(img_path)
    if str(do_ocr)=='True':
        print("OCR API CALLED")
        gv_key = requests.post('http://192.168.170.11:8888/gv_ocr/',json = {
              "GvKey": {},
              "ImageBase64": imgb64
               }).json()
        print("OCR DONE")
        ocr_coords = gv_key['coordinates']
        text = gv_key['text']
        input_json = {
        "formName": doc_name,
        "formImage": imgb64,
        "ocrData": {'data': ocr_coords, 'text': text},
        'fieldIdInput': fieldIdInput,
        'pageNumber': pagenum
        }
        with open('input_SD.json','w') as f:
            json.dump(input_json,f,indent=1)

    else:
        with open('input_SD.json','r') as f:
            input_json = json.load(f)


    print("Structure Document HIT")
    res = requests.post(url, json=input_json).json()
    return res

if __name__ == '__main__':
    img_path = sys.argv[1]
    doc_name = sys.argv[2]
    try:
        fieldIdInput = sys.argv[4]
    except:
        fieldIdInput = None
    try:
        pagenum = sys.argv[3]
    except:
        pagenum = None
    try:
        do_ocr = sys.argv[5]
    except:
        do_ocr = True

    url = 'http://0.0.0.0:8088/trade_finance/structuredDocumentExtraction'
    res = call_structure_document(img_path,doc_name,url,fieldIdInput= fieldIdInput,pagenum = pagenum)
    print(res)
