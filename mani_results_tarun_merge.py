lc_amen_0 = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_amen0/complete_block_doc.json"
lc_amen_1 = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_amen1/complete_block_doc.json"
lc_app_0 = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_app0/complete_block_doc.json"
lc_exp_0 = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_export0/complete_block_doc.json"
lc_exp_1 = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_export1/complete_block_doc.json"

import json
for amen in [lc_amen_0,lc_amen_1,lc_app_0,lc_exp_0,lc_exp_1]:
	print('##############################')
	print(amen)
	data = json.load(open(amen,"r"))
	print(data.keys())
	for k in data.keys():
		print(f"parent key : {k}")
		for _ in data[k]:
			print(f"  {_['label']}")
