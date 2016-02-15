from flask import Flask, render_template, redirect, url_for, request
from textanalytics import *
from twitterquery import *

app = Flask(__name__)

APP_KEY = 'hiE4tBmkZaf1wC5PT4hUBaxMz'
APP_SECRET = '7OEgCKwGrQYAwl5I1kYwXwk14wZc2HBC6GnXFUxZlrrTCnge3C'
twitter = Twython(APP_KEY, APP_SECRET)

@app.route('/')
def home():
    
    topic = "python"
    sentences = fetchTweets(str(topic), twitter)
    
    pieData = analyzeSentiment(sentences)
    preProcessedBarData = preProcessHistogram(sentences)
    twod_barDataWithStopWords =  processForBarGraph(wordHistogramWithStopWords(preProcessedBarData))
    twod_barDataNoStopWords =  processForBarGraph(wordHistogramNoStopWords(preProcessedBarData))
    
    barDataWithStopWords = twod_barDataWithStopWords[1]
    barDataLabelsWithStopWords = twod_barDataWithStopWords[0]
    
    barDataNoStopWords = twod_barDataNoStopWords[1]
    barDataLabelsNoStopWords = twod_barDataNoStopWords[0]
    
    return render_template('welcome.html',pieData=pieData, barDataWithStopWords=barDataWithStopWords, barDataLabelsWithStopWords=barDataLabelsWithStopWords,
    barDataNoStopWords=barDataNoStopWords, barDataLabelsNoStopWords=barDataLabelsNoStopWords)



@app.route('/', methods=['GET','POST'])
def home_post():
    
    topic = request.form['text']
    sentences = fetchTweets(str(topic), twitter)
    
    pieData = analyzeSentiment(sentences)
    preProcessedBarData = preProcessHistogram(sentences)
    twod_barDataWithStopWords =  processForBarGraph(wordHistogramWithStopWords(preProcessedBarData))
    twod_barDataNoStopWords =  processForBarGraph(wordHistogramNoStopWords(preProcessedBarData))
    
    barDataWithStopWords = twod_barDataWithStopWords[1]
    barDataLabelsWithStopWords = twod_barDataWithStopWords[0]
    
    barDataNoStopWords = twod_barDataNoStopWords[1]
    barDataLabelsNoStopWords = twod_barDataNoStopWords[0]
    
    return render_template('welcome.html',pieData=pieData, barDataWithStopWords=barDataWithStopWords, barDataLabelsWithStopWords=barDataLabelsWithStopWords,
    barDataNoStopWords=barDataNoStopWords, barDataLabelsNoStopWords=barDataLabelsNoStopWords)

    
@app.route('/howitworks')
def howitWorks():
    
    return render_template('howitworks.html')
    
if __name__ == '__main__':
    app.run(debug=True)