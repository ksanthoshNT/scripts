import json

data_path = "/home/ntlpt59/Documents/Trade-Finance-Demo-LC_DATA.postman_collection.json"

with open(data_path, 'r') as file:
    x = json.load(file)
item = x["item"][0].copy()
items_list = x["item"]
for i in range(2,114):
    items_cpy = x["item"][0].copy()
    items_cpy["name"] = "ucp_ae_sd_"+str(i)+'_lc'
    items_list.append(items_cpy)

x["item"] = items_list
with open("save.json",'w') as f:
    json.dump(x,f,indent=4)
