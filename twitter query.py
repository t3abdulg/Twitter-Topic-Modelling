# Programmed by: Tawfeeq Abdul Gaffoor
# t3abdulg@uwaterloo.ca

# Dependencies
from twython import Twython
from gensim import corpora, models, similarities
from gensim.models import hdpmodel, ldamodel ,lsimodel
from itertools import izip
from nltk.corpus import stopwords
from langdetect import detect
from textblob import TextBlob
import re
import nltk

def ModelTopics(init_topic):
    # Variable Declarations   
    tweets = []
    documents = []
    sentiment = 0;
    
    # API Keys
    APP_KEY = 'Input Here'
    APP_SECRET = 'Input Here'
    
    # Performning the search.
    twitter = Twython(APP_KEY, APP_SECRET)
    
    x = twitter.search(q=str(init_topic), count = 100)
    
    # Iterating through all the tweets, placing in array
    for tweet in x['statuses']:
        tweets.append((tweet['text']).encode('ascii', 'ignore'))
    
    # Iterating throught array, removing links.
    for i in range(0,len(tweets)):
        #removing all links, because really its just gonna mess up topic modeling
        tweets[i] = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', tweets[i])
        tweets[i] = re.sub(r'(?i)\b((?:http?://\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', tweets[i])
        #removing all new-line characters and hashtags
        tweets[i] = tweets[i].replace("#","")
        tweets[i] = tweets[i].replace("\n","")
        #removing the "RT: " from retweeted tweets
        if tweets[i][:2] == "RT":
            while(tweets[i][:2] != ': '):
                tweets[i] = tweets[i][1:]
            tweets[i] = tweets[i][2:]
    
    # Detecting Languages via Twitter API results is unfavourable, so instead we filter out Non-English tweets after.
    for i in range(0, len(tweets)):
        if detect(tweets[i]) == 'en':
            documents.append(tweets[i])

        
    # this list of stopwords is a bunch taken from the python library nltk.
    stoplist = set(stopwords.words('english') + ['get', '!', ',','.','it','it\'s'])
    
    # remove common words and tokenize
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in documents]
    
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # apply the LDA Model. 
    lda = ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=1, 
                            chunksize=10000, passes=10)
    
    # print the probabilistic model
    topics =lda.print_topics(10)
    
    for i in range(0,len(topics)):
        print topics[i]
        