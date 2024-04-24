import os
import shutil
import zipfile
from PIL import Image,ImageSequence
from fitz import fitz
from loguru import logger
import time

def split_img(r,f,root,storeTop25PercentImage:str = True):
    src = os.path.join(r,f)
    f= f.split(".pdf",1)[0]
    os.makedirs(os.path.join(root,"output"),exist_ok=True)
    r= os.path.join(root,"output")

    if src.split(".")[-1].lower() in ["tiff", "tif","pdf"]:
        with fitz.open(src) as doc:
            for i, page in enumerate(doc):
                pix = page.get_pixmap()
                f_n = "_".join(f.split())
                output = f"{f_n}_%d.png" % i

                if storeTop25PercentImage:
                    width, height = pix.width, pix.height
                    cropped_image = Image.frombytes("RGB", [width, height // 4], pix.samples)
                    cropped_image.save(os.path.join(r,output))
                else:
                    pix.save(os.path.join(r,output))
    elif src.split(".")[-1].lower() in ["png", "jpeg", "jpg"]:
        im = Image.open(src)
        f_n = "_".join(f.split())
        output = f"{f_n}.png"
        output = os.path.join(r,output)
        im.save(output)






if __name__=="__main__":
    src_folder = "/home/ntlpt59/MAIN/trade_finance_codes/structure_documents/structured_docs/all_checked"
    dest_folder = src_folder.rsplit("/",1)[0]
    curr_folder_out = src_folder.rsplit("/",1)[1] + "_output"
    os.makedirs(os.path.join(dest_folder,curr_folder_out),exist_ok=True)
    storeTop25PercentImage: bool = False
    count_pdf,count_tiff,count_normal_img,count_zip = 0,0,0,0
    dc = {}
    for src in os.listdir(src_folder):
        logger.info('###  START SPLIT PDF ')
        start = time.time()
        file_name: str = src.split("/")[-1].split(".")[0]
        print(f"filename is {file_name}")
        print(f"source is {src}")
        src_name = src.rsplit(".")[0]
        if src.split(".")[-1].lower() in ["pdf","tiff","tif"]:
            if src.split(".")[-1].lower() == "pdf":
                count_pdf+=1
            else:
                count_tiff+=1
            with fitz.open(os.path.join(src_folder,src)) as doc:
                for i, page in enumerate(doc):
                    pix = page.get_pixmap()
                    output = f"{src_name}_%d.png" % i

                    if storeTop25PercentImage:
                        width, height = pix.width, pix.height
                        cropped_image = Image.frombytes("RGB", [width, height // 4], pix.samples)
                        cropped_image.save(os.path.join(dest_folder,curr_folder_out,output))
                    else:
                        pix.save(os.path.join(dest_folder,curr_folder_out,output))
        elif src.split(".")[-1].lower() in ["png","jpeg","jpg"]:
            count_normal_img+=1
            im = Image.open(os.path.join(src_folder, src))
            output = os.path.join(dest_folder,curr_folder_out,f"{src_name}.png")
            im.save(output)
        elif src.split(".")[-1].lower() in ["zip"]:
            count_zip+=1
            os.makedirs("zip_dummy")
            with zipfile.ZipFile(os.path.join(src_folder,src), 'r') as zip_ref:
                zip_ref.extractall(path="zip_dummy")
            for r,d,f in os.walk("zip_dummy"):
                for _f in f:
                    split_img(r,_f,"zip_dummy")
            for f in os.listdir(os.path.join("zip_dummy","output")):
                print(os.path.join("zip_dummy","output",f))
                shutil.copy(os.path.join("zip_dummy","output",f),os.path.join(dest_folder,curr_folder_out))
            shutil.rmtree("zip_dummy")



    print(count_normal_img,count_tiff,count_pdf,count_zip)
    print(dc.keys())






