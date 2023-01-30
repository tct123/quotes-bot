from twitter import *
from mastodon import *
from quotesgeneratorapi import quotes
from data import *

class Twitterbot():
    def __init__(self):
        t = Twitter(auth=OAuth(TOKEN,TOKENSECRET,CONSUMERKEY,CONSUMERSECRET))
        content = quotes.getQuotes()
        print(content)
        t.statuses.update(
            status = content)
        print(content)
Twitterbot()