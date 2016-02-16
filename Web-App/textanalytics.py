from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import collections
from string import maketrans,punctuation
import json                 
                 
def analyzeSentiment(sentences):
    neu = 0
    pos = 0
    neg = 0 
    
    #declare if each sentence carries a negative, neutral of positive sentiment    
    for sentence in sentences:
        vs = vaderSentiment(sentence)

        if (vs['neg'] > vs['pos']):
            neg+=1
        elif (vs['pos'] > vs['neg']):
            pos+=1
        else:
            neu+=1
   
    #output is in this format so chartJs can use it in the web-App
    return_data = [{'value': neg, 'label': 'Negative Tweets','color': '#D18177'},
    {'value': neu, 'label': 'Neutral Tweets','color': '#9CBABA'},
    {'value': pos, 'label': 'Positive Tweets','color': '#00688B'}]
  
        
    return return_data
 
def preProcessHistogram(documents):

    paragraph = ""
    for sentence in documents:
        paragraph = paragraph + " " + sentence.lower()
   
    #make all words lowercase and remove all punctuation         
    lowerCaseParagraph = paragraph.translate(maketrans("",""),punctuation) 
    
    words = lowerCaseParagraph.split()  
    
    
    lemmatizer = WordNetLemmatizer()
    #lemmatize every word.... (if it needs to be lemmatized) and remove words that are too long, because chances are they arent words.
    words = map(lambda x: lemmatizer.lemmatize(x,'v'), words)
    words = filter(lambda x: len(x) < 10 or x.isdigit() , words)
    
    return words
   
   
def wordHistogramWithStopWords(splitText):

    #list of stopwords taken from nltk (and I added a few of my own)
    stoplist = set(stopwords.words('english') + ['get', '!', ',','.','it','it\'s','-'])
    
    #removes stopwords
    resultWords = [word for word in splitText if word not in stoplist]
    
    #counts the amount of each word
    resulting_count = collections.Counter(resultWords)   
    
    return json.dumps(resulting_count)


def wordHistogramNoStopWords(splitText):
    
    #counts the amount of each word
    resulting_count = collections.Counter(splitText)   
    
    return json.dumps(resulting_count)


def processForBarGraph(histogramData):
    labels = []
    data = []
    
    dictHistogramData = json.loads(histogramData)
    
    #process the data for output such that the webapp and chartJs can make use of it
    for key in dictHistogramData:
        labels.append(key.encode('ascii','ignore'))
        data.append(json.loads(histogramData)[key])
   
    return [labels,data]
        

def ModelTopics(sentences):

    # Tokenize
    texts = [[word for word in document.lower().split()]
             for document in sentences]

    #load Model
    lda = gensim.models.LdaModel.load('lda.model')
    dictionary = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt')
    
    #transform words to mapping from ldaModels dictionary
    corpus = [dictionary.doc2bow(text) for text in texts]

    #apply the model on the new documents
    topic_vec = lda[corpus]
    
    topics = []
    
    for i in topic_vec:
        for j in i:
            topic.append(lda.print_topics(j[0]))
            
    return topics
            
    