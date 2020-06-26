import tweepy
import json
import time
import sys
import re
# Authentication Keys to Connect to Twitter API
CONSUMER_KEY = "qhJBwYCG9nYR7d5a5ZNfJD3Wy"
CONSUMER_SECRET = "gWAh87ScdyhUE5weUNc7PvLsc2Lax2yLm6sGKOjIbxELnfcKBS"
OAUTH_TOKEN = "2801896164-B9QLY4qwRBDKzi0LH1e1utgywvPrYdDOHJHnG0i"
OAUTH_TOKEN_SECRET = "ATnP7537AG1Q6tNgvwnekprYz5vpYgj7jykxRGYEgo8nX"

tweetFile = open('tweetLink', 'w')                             #Open a file to write the output
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)      #Get OAuth handler from tweepy
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)         
url_list = set()
api = tweepy.API(auth)                                        #Getting Tweepy API
search_results = tweepy.Cursor(api.search,q="http:").items()

while True:                                                   # Infinite loop through tweets
    try:
        tweet = search_results.next()
        item= tweet._json
        eachitem={}
        created_date= item['user']['created_at']
        tweet_id= item['id_str']
        eachitem['id'] = tweet_id
        eachitem['createdDate'] = created_date
        for link in item['entities']['urls']:
            url_list.add(link['url'])
            eachitem['link']=link['url']
            tweetFile.write(json.dumps(eachitem) + '\n')
            print link['url']
        if len(url_list) == 10000:                           # Break at 10000
            break
    except tweepy.TweepError:
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break
print len(url_list)
print url_list
    
     
     
    