from twitter import *
from quotesgeneratorapi import quotes
from data import *

class Twitterbot():
    def __init__(self):
        t = Twitter(auth=OAuth(APIKEY,APIKEYSECRET,BEARERTOKEN,ACCESSTOKENSECRET))
        content = quotes.getQuotes()
        t.statuses.update(
            status = content)
        print(content)
Twitterbot()