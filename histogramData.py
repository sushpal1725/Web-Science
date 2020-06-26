import requests
import json

dicts={}
redirect={}
histogramdata = open('histogramdata', 'w')
histogramLinkData = open('histogramLinkdata', 'w')
histogramStatusData =  open('histogramStatusdata', 'w')
for i in range(1,11):
    filepath = "statusoutputs"
    filepath+=`i`
    fh=open(filepath,'r')
    for line in fh:
        eachJson=json.loads(line)
        for status in eachJson['statuscodes']:
            histogramStatusData.write(str(status)+'\n')
            if status in dicts:
                dicts[status]+=1
            else:
                dicts[status] =1
            statuslen = len(eachJson['statuscodes'])-1
            histogramLinkData.write(str(statuslen) + '\t'+str(eachJson['finalurl'])+'\n')
            if statuslen in redirect:
                redirect[statuslen]+=1
            else:
                redirect[statuslen]=1
finalJson={}
finalJson['statusfinaldata']=dicts
finalJson['redirectdata']=redirect
histogramdata.write(json.dumps(finalJson) + '\n')

    
        
                