from flask import Flask, render_template, redirect, url_for, request
from twittersentiment import *

app = Flask(__name__)


@app.route('/welcome')
def welcome():
	topic = "python"
	top3 = Top3("python")
	tweet1 = top3[0]
	tweet2 = top3[1]
	tweet3 = top3[2]
	tweet4 = top3[3]
	tweet5 = top3[4]
	tweet6 = top3[5]
	item_list = list(ProcessOutput(ModelTopics("python")))
	return render_template("welcome.html",tweet1=tweet1, tweet2=tweet2, 
		tweet3=tweet3,tweet4=tweet4,tweet5=tweet5,tweet6=tweet6, topic=topic,item_list=item_list)


@app.route('/welcome', methods=['POST'])
def welcome_post():
	text = request.form['text']
	top3 = Top3(text)
	topic = text
	tweet1 = top3[0]
	tweet2 = top3[1]
	tweet3 = top3[2]
	tweet4 = top3[3]
	tweet5 = top3[4]
	tweet6 = top3[5]
	item_list = list(ProcessOutput(ModelTopics(str(text))))
	return render_template("welcome.html",tweet1=tweet1, tweet2=tweet2, 
		tweet3=tweet3,tweet4=tweet4,tweet5=tweet5,tweet6=tweet6, topic=topic, item_list=item_list)

if __name__ == '__main__':
	app.run(debug=True)
    
 
