# @Author: Karthick <ramya>
# @Date:   2017-08-21T09:02:42+02:00
# @Last modified by:   ramya
# @Last modified time: 2017-08-21T09:18:12+02:00

from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

@app.route('/')
def homepage():
    return "Hi, Welcome to Flask-Ask"

@ask.launch
def start_skill():
    welcome_message = "Hello MHP Lab, would you like to hear some jokes?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_jokes():
    jokes = get_jokes()
    jokes_txt = "Current jokes available at Reddit are {}".format(jokes)
    return statement(jokes_txt)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "I am not sure why you asked me to run. Okay. bye..."
    return statement(bye_text)

if __name__=="__main__":
    app.run(debug=True)
