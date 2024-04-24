mani_data= "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/Structure_Doc_Api/data/output/crop/LC_export0/complete_block_doc.json"
import json
with open(mani_data,"r") as file:
	mani = json.load(file)
tarun_data = "/home/ntlpt59/MAIN/tarun_nt_TFDelivery/client_code/trade_finance_structure_document/src/data/templates/export_letter.json"
with open(tarun_data,"r") as file:
	tarun = json.load(file)

tarun_ids = []
for field in tarun['page0'].keys():
	tarun_ids.append(tarun['page0'][field]['parent_id'])

mani_ids = []
for k in mani.keys():
	mani_ids.append(k)


for x in set(tarun_ids):
	print(x)

print('++++')

for x in mani_ids:
	print(x)


print('+++')	

