import os

import pytesseract
from pytesseract import Output
from PIL import Image
import json
import sys


def ocr_perform(input_image_path,file_name,dest_path):
    print(f"{file_name}")
    image = Image.open(input_image_path)
    text_data = pytesseract.image_to_string(image)
    print(f"dest_path: {dest_path}/{file_name}_ocr.txt")
    with open(os.path.join(dest_path,f"{file_name}_ocr.txt"),'w') as f:
        f.write(text_data)



if __name__ == "__main__":
    src_path = sys.argv[1]
    print(src_path)
    if src_path.split('.')[-1] in ["jpg","jpeg","png"]:
    	file_name = src_path.split('/')[-1].split('.')[0]
    	dest_path  = src_path.rsplit('/',1)[0]
    	ocr_perform(src_path,file_name,dest_path)
    	exit()
    if len(sys.argv)==2:
        os.makedirs(os.path.join(src_path.rsplit("/")[0],"output"),exist_ok=True)
        dest_path = os.path.join(src_path.rsplit("/")[0],"output")
    elif len(sys.argv)==3:
        dest_path = sys.argv[2]

    for r,d,f in os.walk(src_path):
        for file_name in f:
            if file_name.rsplit(".",1)[-1] in ["png","jpg","jpeg"]:
                ocr_perform(os.path.join(r,file_name),file_name,dest_path)

