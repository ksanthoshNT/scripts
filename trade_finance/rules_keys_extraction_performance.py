import base64
import json
import os
import time

import pandas as pd
import requests
from fuzzywuzzy import  fuzz

def image_to_base64(path):
    try:
        with open(path,'rb')  as file:
            img_data = file.read()
            baseimg = base64.b64encode(img_data).decode('utf-8')
    except Exception as e:
        print(f"Not able to convert base64 for image: {path}")
    return baseimg
doc_ignore = ['PI','PO']
path = '/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/rules_keys_data_validation'
output_path = '/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/rules_keys_output'
rule_keys_path = '/home/ntlpt59/Documents/trade_finance/rule_documents_keys_final.json'
final_data_path = '/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery/final_data.json'
csv_save_path = '/media/ntlpt59/HI/D/DATA_LAKE/TradeFinanceFinalDelivery'
doc_sample = 10
os.makedirs(output_path,exist_ok=True)

#
# for doc in os.listdir(path):
#     if doc in doc_ignore: continue
#     count_doc = 0
#     for img in os.listdir(os.path.join(path,doc,'Master_Data')):
#         if img.endswith('.png'):
#             if count_doc >=doc_sample:
#                 break
#             imgb64 = image_to_base64(os.path.join(path,doc,'Master_Data',img))
#             input_json = {"docClass":doc,'image':imgb64}
#             print(f'Doc: {doc} , img: {img}')
#             res = requests.post(url='http://10.2.3.14:8198/transformer/trade-finance/extract/',json= input_json)
#             os.makedirs(os.path.join(output_path,doc),exist_ok=True)
#             if res.status_code == 200:
#                 with open(os.path.join(output_path,doc,img.rsplit(".",1)[0]+'_extractres.json') ,'w') as file:
#                     json.dump(res.json().get("keys_extraction",{}),file,indent=2)
#                 count_doc+=1
#             else:
#                 print(f"Issue for image {img}, response : {res.status_code}")


# final_data ={}
# for doc in os.listdir(output_path):
#     for img in os.listdir(os.path.join(output_path,doc)):
#         img_name= img.rsplit('_',1)[0]
#         if 'ground' in img_name: continue
#         with open(os.path.join(path,doc,'Master_Data',img_name+'_labels.txt'),'r') as file:
#             text = file.read()
#         data_label = json.loads(text)
#         with open(os.path.join(output_path,doc,img_name+'_ground_truth.json'),'w') as file:
#             json.dump(data_label,file,indent=2)
#         final_data.setdefault(doc,{}).update({img_name:{'extraction_result':os.path.join(output_path,doc,img),
#                                           'ground_truth':os.path.join(output_path,doc,img_name+'_ground_truth.json')}})

# with open(rule_keys_path,'r') as file:
#     key_dict = json.load(file)
#
# with open(final_data_path,'w') as file:
#     json.dump(final_data,file,indent=2)
#
# for doc, doc_info in final_data.items():
#     df = pd.DataFrame(columns=['Keys'])
#     df['Keys'] = key_dict[doc]
#
#     for img,img_info in doc_info.items():
#         with open(img_info.get('extraction_result'),'r') as file:
#             extraction_result = json.load(file)
#         with open(img_info.get('ground_truth'),'r') as file:
#             ground_truth = json.load(file)
#
#         df_data = {}
#         gt_data, er_data = [],[]
#         for k in key_dict[doc]:
#             if k in ground_truth:
#                 gt_data.append(ground_truth[k][0][0])
#             else:
#                 gt_data.append('Not Found')
#             if k in extraction_result:
#                 er_data.append(extraction_result[k].get('value'))
#             else:
#                 er_data.append('Not Found')
#
#         df[img+'_GT'] = gt_data
#         df[img+'_ER'] = er_data
#
#     df.to_csv(csv_save_path+f'/{doc}.csv')

metrics = ['Empty','NotFound','Value','>90','>85','>80','<80']
final_cm = {}
for doc in os.listdir(output_path):
    if doc in doc_ignore : continue
    csv_file = os.path.join(csv_save_path,f'{doc}.csv')
    df = pd.read_csv(csv_file)
    df.fillna("",inplace=True)
    cm = {}
    for index,rows in df.iterrows():
        key_info = rows.to_list()
        keys_name = key_info[1]
        confusion_matrix = {}
        for i in range(2,len(key_info),2):
            gt = key_info[i]
            er = key_info[i+1]
            fr = fuzz.ratio(gt.lower().strip(),er.lower().strip())
            for G in metrics:
                for P in metrics:
                    # if G=='Empty' and P == 'Empty' and gt == '' and er == '':
                    #     confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    # elif G=='Empty' and P == 'NotFound' and gt == '' and er == 'Not Found':
                    #     confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    # elif G=='Empty' and P == 'Value' and gt == '' and len(er)>0 and er!='Not Found':
                    #     confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1
                    # elif G=='NotFound' and P == 'Empty' and gt == 'Not Found' and er == '':
                    #     confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    # elif G=='NotFound' and P == 'NotFound' and gt == 'Not Found' and er == 'Not Found':
                    #     confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    if G=='NotFound' and P == 'Value' and gt == 'Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1
                    elif G=='Value' and P == 'Empty' and len(gt)>0 and gt!='Not Found' and er == '':
                        confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    elif G=='Value' and P == 'NotFound' and len(gt)>0 and gt!='Not Found' and er == 'Not Found':
                        confusion_matrix[G +'__' + P]  = confusion_matrix.get(G+'__'+P,0) + 1
                    elif G=='Value' and P == 'Value' and len(gt)>0 and gt!='Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1 if fr==100 else 0
                    elif G=='Value' and P == '>90' and len(gt)>0 and gt!='Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1 if fr>=90 and fr<100 else 0
                    elif G=='Value' and P == '>85' and len(gt)>0 and gt!='Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1 if fr>=85 and fr<90 else 0
                    elif G=='Value' and P == '>80' and len(gt)>0 and gt!='Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1 if fr>=80 and fr<85 else 0
                    elif G=='Value' and P == '<80' and len(gt)>0 and gt!='Not Found' and len(er)>0 and er!='Not Found':
                        confusion_matrix[G +'__' + P] = confusion_matrix.get(G + '__' + P, 0) + 1 if fr<80 else 0
        cm[keys_name] = confusion_matrix
    final_cm[doc] = cm

with open('confusion_matrix.json','w') as file:
    json.dump(final_cm,file,indent=2)














