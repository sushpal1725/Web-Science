#import human_curl as hurl
import requests
import json
from requests.exceptions import ConnectionError

fh=open("urlspart1")
totalstatuscodes={}
tweetFile = open('statusoutputs1', 'w')
for line in fh:
    eachJson=json.loads(line)
    try:
        r = requests.head(eachJson['link'], allow_redirects=True)
        totalstatuscodes['finalurl']=r.url
        totalstatuscodes['createdDate']=eachJson['createdDate']
        arr = []
        arr.append(r.status_code)
        history = r.history
        for rs in history:
            arr.append(rs.status_code)
        totalstatuscodes['statuscodes'] = arr
        tweetFile.write(json.dumps(totalstatuscodes) + '\n')
    except:    # This is the correct syntax
       continue


        