# Twitter-Topic-Modelling <br />
Topic Modelling and Sentiment Analysis on Tweets Using LDA 

## Contents
 - [About](#about)
 - [How does it Work?](#how-does-it-work)
 - [Dependencies](#dependencies)
 - [Getting it to Work](#getting-it-to-work)
 - [Future-Plans](#future-plans)

## About

This project utilizes LDA to model topics amongst queried tweets, and performs sentiment analysis on the tweets. The potential use cases of some of the concepts utilized in this project are almost infinite.


## How does it Work? 

*Note: I'll give it my best explanation which is very simplified.*

Assume we had only 3 topics in the world, and that each topic is represented by a collection of probabilities of words that belong to them

1. Programming (0.10*Python + 0.10*C++ + 0.10*C .... = 1)
2. Animals (0.10*Panda + 0.10*Bear + .... = 1)
3. Video Games (0.10*Dota2 + 0.10LeagueofLegends + ... = 1)


Now if we had an article about programming:

> "Python is my favorite programming language. It is a dynamically typed language, whereas C++ is static and as a result you run into a lot more errors. However, pointers and references are life so I kinda like C++ a lot too"

As a Human, it is very obvious that this article is about Topic 1 (or programming) isnt it?

Well if we scrambled the text:

> "It errors. a lot programming However, and references a too static and typed kinda you is into pointers a more Python result run are is so I whereas like language. C++ life C++ a language, my dynamically as lot favorite is"

As a Human, we can still kind of tell what the text is about can't we?

LDA (latent dirichlet allocation) Works in a very similar way.

We feed it a bag of words which it assumes to be related (syntax, order, punctuation all don’t matter!). And it tries to generate what the topics might have been, which made up these bag of words.

For such a reason, it makes sense to train the model using Wikipedia Articles where all the words in each article, ARE related (to an extent).

## Dependencies

Requires [Python 2.7.x]

[Gensim] requires [NumPy] and [SciPy]

```
pip install numpy
pip install scipy
```
Requires [Gensim]
```
pip install gensim
```
Requires [Flask]
```
pip install flask
```
Rquires [VaderSentiment]
```
pip install vadersentiment
```
Requires [NLTK]
```
pip install nltk
```
Requires [Twython]
```
pip install twython
```
Requires [Langdetect]
```
pip install langdetect
```

## Getting it to Work

#### Downloading NLTK Data
After we have NLTK installed, we have to install its data. We do that by running:
```
import nltk
nltk.download()
```
and selecting download all data.

#### Preprocessing the Wikipedia Corpus

Navigate to:
> https://dumps.wikimedia.org/enwiki/latest/

Download the file named:
> "enwiki-latest-pages-articles.xml.bz2"

cd into the directory and run
```
python -m gensim.scripts.make_wiki enwiki-latest-pages-articles.xml.bz2 wiki_en
```
This will make a file that maps each word to unique id, and another one that stores a file that contains tf–idf (term frequency index document frequency) vectors. (we need these to train the model). **This process literally took 8-10 hours on my computer**

#### Training the LDA model

Run the script in this repo named:
> "ldatraining.py2"

with both all the filed obtained from the preprocessing step in the same directory

#### Twitter API

You need to obtain your own Twitter API keys and place them in the place holders
```
APP_KEY = 'hiE4tBmkZaf1wC5PT4hUBaxMz'
APP_SECRET = '7OEgCKwGrQYAwl5I1kYwXwk14wZc2HBC6GnXFUxZlrrTCnge3C'
twitter = Twython(APP_KEY, APP_SECRET)
```
The current keys, are just placeholders. **(They will not work)** 
Keys can be obtained from 
> https://dev.twitter.com/

## Future Plans

Surprisingly, some of my previous approaches where I didn't use the entire Wikipedia corpus, but instead used individual tweets themselves yielded better results. I'm going to try to change the chunk-size and the number of passes and the number of topics and see what happens. Unfortunately, the corpus is so large and it takes so much time to train the model that you don't really have the option to "play around" as much.

I've been experimenting with Word2Vec a lot recently, but I haven’t quite gotten the success I was looking for yet. I trained the tool using the brown corpus in the nltk library, but this corpus is way too small so I didn't get the results I was looking for. I tried to load a pre-trained vectors from the Google News Dataset, but this simply took far too much RAM and I couldn't get it to work properly on my computer. I'll definitely look into this more, and try to get some desirable results. 

While the current Flask-Application works well to visualize the calculated, much more could be done. I plan to build a REST-API, and build an express/angular/node Web-App that would communicate with the API and display the information in a much more visually pleasing way.


[Python 2.7.x]:https://www.python.org/downloads/
[Gensim]:https://pypi.python.org/pypi/gensim
[Numpy]:http://www.scipy.org/install.html
[SciPy]:http://www.scipy.org/install.html
[Flask]:http://flask.pocoo.org/
[NLTK]:http://www.nltk.org/install.html
[VaderSentiment]:https://pypi.python.org/pypi/vaderSentiment
[langdetect]:https://pypi.python.org/pypi/langdetect
[Twython]:https://twython.readthedocs.org/en/latest/usage/install.html
