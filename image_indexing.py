import json
import  os
res = {}
cls = {}
for img in os.listdir("/home/ntlpt59/Desktop/extraction/extraction"):
    data = json.load(open(f"/home/ntlpt59/Desktop/extraction/extraction/{img}","r"))
    res.update({img.split(".")[0]+".png":data})
    cls.update({img.split(".")[0]+".png":{'class':data['docClass'],'docClass':data['docClass'],
                                          'confidenceScore':99.89234967454004,"statusCode":200}})

with open("output_extraction_results.json","w") as f:
    json.dump(res,f,indent=2)

with open("output_classification_results.json","w") as f:
    json.dump(cls,f,indent=2)
for x in os.listdir("/home/ntlpt59/Desktop/extraction"):
    if x== "extraction":
        continue
    print(x)