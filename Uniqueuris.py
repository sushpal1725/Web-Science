import requests
import json


histogramdata = open('histogramdata', 'w')
histogramLinkData = open('histogramLinkdata', 'w')
histogramStatusData =  open('histogramStatusdata', 'w')
url_list = set()
for i in range(1,11):
    filepath = "statusoutputs"
    filepath+=`i`
    fh=open(filepath,'r')
    for line in fh:
        eachJson=json.loads(line)
        for status in eachJson['finalurl']:
            url_list.add(status)
print len(url_list)