import os

from fuzzywuzzy import fuzz

x  = input()
while(x.split()[0]!="end"):
    ans = []
    for i in os.listdir('data'):
        with open(os.path.join('data',i)) as _file:
            data = _file.read().splitlines()
        for v in data:
            ratio = fuzz.ratio(v,x.split()[0])
            if ratio>0:
                if len(x.split())>1:
                    if fuzz.ratio(x.split()[1],i)>30:
                        ans.append([v,ratio,i[:-4]])
                else:   
                    ans.append([v,ratio,i[:-4]])
                    
    sorted_data = sorted(ans,key=lambda x:x[1],reverse=True)
    print(sorted_data[:25])
    x = input()
