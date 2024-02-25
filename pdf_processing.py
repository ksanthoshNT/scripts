import sys

import cv2
import os
import fitz
from pdf2image import convert_from_path
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from ocr_coordinates_with_confidence import extract_text_and_coordinates
from struct_doc_keys_wise import informat_structed_doc
from test_classify_key_word_based import get_ocr_vision_api_charConfi
import pytesseract
import base64
import json
from itertools import chain

def get_coordinates(coords):
    if isinstance(coords,dict):
        return coords.get("word_coordinates",coords.get("coordinates"))
    if isinstance(coords,tuple) or (coords and isinstance(coords[0],list)):
        return list(chain.from_iterable(coords))
    return coords
def call_structure_document(img_path = None,doc_name = None,url = None,fieldIdInput = None,pagenum = None,img = None,do_ocr = True):
    if img_path:
        with open(img_path, 'rb') as file:
            img = file.read()
        imgb64 = base64.b64encode(img).decode('utf-8')
    else:
        imgb64 = base64.b64encode(img).decode('utf-8')
    # ocr_coords = extract_text_and_coordinates(img_path)
    if do_ocr:
        print("OCR API CALLED")
        gv_key = requests.post('http://192.168.170.11:8888/gv_ocr/',json = {
              "GvKey": {},
              "ImageBase64": imgb64
               })
        if gv_key.status_code != 200:
            print("OCR ERROR")
        else:
            gv_key = gv_key.json()
        print("OCR DONE")
        ocr_coords = gv_key['coordinates']
        text = gv_key['text']
        with open(f'{doc_name}+{pagenum}+coord.json','w') as f:
            json.dump(ocr_coords,f,indent=1)
        with open(f"{doc_name}+{pagenum}+text.txt",'w') as f:
            f.write(text)
    else:
        with open(f'{doc_name}+{pagenum}+coord.json','r') as f:
            ocr_coords = json.load(f)
        with open(f"{doc_name}+{pagenum}+text.txt",'r') as f:
            text = f.read()

    input_json = {
        "formName": doc_name,
        "formImage": imgb64,
        "ocrData": {'data': ocr_coords, 'text': text},
        'fieldIdInput': str(fieldIdInput) if fieldIdInput is not None else None,
        'pageNumber': pagenum
    }
    with open('input_SD.json', 'w') as f:
        json.dump(input_json, f, indent=1)

    print(f"Structure Document HIT for field: {'all' if fieldIdInput is None else fieldIdInput}, OCR CALL: {do_ocr}")
    res = requests.post(url, json=input_json).json()
    return res


def pdf_process(pdf_path,output_pdf_path = None):
    if not output_pdf_path:
        output_pdf_path = pdf_path.rsplit('.',1)[0]+'_output.pdf'

    images = convert_from_path(pdf_path)
    with fitz.open() as pdf_doc:
        for i, image_pil in enumerate(images):
            # if i!=1: continue
            page_number = f'page{i}'
            print(f" ##### START DOC EXTRACTION FOR PAGE: {page_number} ####")
            # if response.status_code == 200:
            # image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
            image = np.array(image_pil)
            # cv2.imshow('image', image)
            # cv2.imwrite("image_hit.jpg", image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            image_buffer = Image.fromarray(image)
            buffer   = BytesIO()
            image_buffer.save(buffer, format="PNG")
            original_image = buffer.getvalue()
            response = call_structure_document(img= original_image,
                                               url=url,
                                               doc_name='export_letter',
                                               fieldIdInput= str(field_id) if field_id is not None else None,
                                               pagenum=page_number,
                                               do_ocr=True if doc_ocr else False
                                               )
            # exit('+++++')
            draw_colors = [[(255,0,0,),(0,255,0),(0,0,255)],[(0,255,0),(0,0,255),(255,0,0)],[(0,0,255),(255,0,0),(0,255,0)]]
            for parent_key in response.keys():
                for i,(name, info) in enumerate(response[parent_key].items()):
                    field_coordinates = get_coordinates(info['Field_coordinates'])
                    if len(field_coordinates) == 4:
                        print(f"PARENTKEY :: {parent_key}, KEY :: {name}, VALUE :: {info['value']}")
                        x1,y1,x2,y2 = field_coordinates
                        # Draw red rectangle
                        index = (i)%3
                        cv2.rectangle(image, (x1, y1), (x2, y2), draw_colors[index][0], 2)
                        # Put text beside the rectangle
                        cv2.putText(image, name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, draw_colors[index][1], 1)
                        if info['value'] and isinstance(info['value'],str):
                            cv2.putText(image, info['value'], (x1, y1 + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, draw_colors[index][2], 1)
                        elif info['value']:
                            cv2.putText(image, "~".join(info.get("value",{}).values()), (x1, y1 + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, draw_colors[index][2], 1)

            # cv2.imshow('image',image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # exit('++++++++++++')
            img_buffer = BytesIO()
            Image.fromarray(image).save(img_buffer, format="PDF")
            img_bytes = img_buffer.getvalue()
            img = fitz.open("pdf", img_bytes)
            pdf_doc.insert_pdf(img)
            img.close()
            print(f" ##### COMPLETE DOC EXTRACTION FOR PAGE: {page_number} ####")
        pdf_doc.save(output_pdf_path)

    # Step 5: Merge back the images to PDF
    # with fitz.open() as pdf_doc:
    #     for image in images:
    #         img_buffer = BytesIO()
    #         Image.fromarray(image).save(img_buffer, format="PDF")
    #         img_bytes = img_buffer.getvalue()
    #         img = fitz.open("pdf", img_bytes)
    #         pdf_doc.insert_pdf(img)
    #         img.close()
    #     pdf_doc.save(output_pdf_path)

    print("Process complete. Output saved to:", output_pdf_path)

if __name__ == '__main__':
    url = 'http://0.0.0.0:8088/trade_finance/structuredDocumentExtraction'
    pdf_path = sys.argv[1]
    output_pdf_path = pdf_path.rsplit('.', 1)[0] + '_output.pdf'

    if len(sys.argv) == 4:
        field_id = sys.argv[2]
        doc_ocr = sys.argv[3]
    elif len(sys.argv) == 3:
        field_id = sys.argv[2]
        if field_id.lower() in ['true','false']:
            doc_ocr = field_id
            field_id = None
        else:
            doc_ocr = None
    elif len(sys.argv) == 2:
        field_id = None
        doc_ocr = None
    pdf_process(pdf_path,output_pdf_path)

