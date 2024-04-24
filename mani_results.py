import base64
import json
import os

import cv2
import requests
def mani_result():
    url ="http://10.2.3.12:8000/documentExtraction"
    image_path  = "/home/ntlpt59/MAIN/TF_FINAL_TESTING/struct_docs/all_filled_data_samples"
    mani_resp = {}
    for img in os.listdir(image_path):
        print(f"Running for {img}")
        img_read = cv2.imread(os.path.join(image_path,img))
        _,img_encoded = cv2.imencode(".png",img_read)
        img_b64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')
        resp = requests.request(method="POST",
                                url=url,
                                headers={"Content-Type": "application/json"},
                                json={"filename":img,"filedata":img_b64})
        if resp.status_code == 200:
            resp = resp.json()
            mani_resp[img] = resp

    with open("mani_resp.json","w") as file:
        json.dump(mani_resp,file,indent=2)

def view():
    data = json.load(open("mani_resp.json","r"))
    for img,v in data.items():
        for img_name in data[img].keys():
            print('####################')
            print(img_name)
            if img_name != "status":
                for parent in data[img][img_name].keys():
                    print(f"parent is : {parent}")
                    for values in data[img][img_name][parent]:
                        if 'label' in values:
                            print(f"    {values['label']}")




if __name__ == "__main__":
    view()