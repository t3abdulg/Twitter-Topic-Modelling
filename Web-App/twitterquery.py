from twython import Twython
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from langdetect import detect
import re


def fetchTweets(queryTopic,twitter):
    
    raw_data = twitter.search(q=str(queryTopic), count= 10, lang='en')

    tweets = []

    for tweet in raw_data['statuses']:
        tweets.append((tweet['text']).encode('ascii', 'ignore'))
     
        
    for i in range(0,len(tweets)):
        #removing all links, because really its just gonna mess up topic modeling
        tweets[i] =re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweets[i])
        #removing #'s, '\n''s, and 'RT'
        tweets[i] = tweets[i].replace("#","")
        tweets[i] = tweets[i].replace("\n","")
        if tweets[i][:2] == "RT":
            while(tweets[i][:2] != ': '):
                tweets[i] = tweets[i][1:]
            tweets[i] = tweets[i][2:]
            
            
    tweets = filter(lambda x: len(x) > 3, tweets)
    
    return tweets
 