# @Author: Karthick <ramya>
# @Date:   2017-08-21T09:02:42+02:00
# @Last modified by:   ramya
# @Last modified time: 2017-08-21T20:16:06+02:00

from flask import Flask
from flask_ask import Ask, statement, question, session
import praw
import time
import pickle
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

with open("access/reddit_access.pkl", "rb") as handle:
    access_info = pickle.load(handle)

def get_jokes():
    with open("access/reddit_access.pkl", "rb") as handle:
        access_info = pickle.load(handle)
    r = praw.Reddit(client_id = access_info.get("client_id"),
                    client_secret = access_info.get("client_secret"),
                    password = access_info.get("password"),
                    user_agent = "trial with reddit",
                    username = access_info.get("username")
            )
    sub_reddit = r.subreddit("jokes")
    i = 0
    jokes= ""
    for submission in sub_reddit.submissions():
        try:
            joke = unidecode.unidecode(submission.title + "<br/>" + submission.selftext + "<br/><br/>")
            jokes += joke
            i+=1
            time.sleep(0.1)
            if i == 10:
                break
        except:
            time.sleep(1)
    #print(jokes)
    return jokes

@app.route('/')
def homepage():
    return "Hi, Welcome to Flask-Ask" #+ "<br/>" + get_jokes()

@ask.launch
def start_skill():
    welcome_message = "Hello MHP Lab, would you like to hear some jokes?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_jokes():
    jokes = get_jokes()
    jokes_txt = "Current jokes available at Reddit are {}".format(jokes)
    #print(jokes_txt)
    return statement(jokes_txt)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "I am not sure why you asked me to run. Okay. bye..."
    return statement(bye_text)

if __name__=="__main__":
    app.run(debug=True)
