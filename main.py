from twitter import *
from mastodon import *
from quotesgenerator.main import *
from data import *

class Twitterbot():
    def __init__(self):
        #Mastodon
        t = Twitter(auth=OAuth(TOKEN,TOKENSECRET,CONSUMERKEY,CONSUMERSECRET)) #Twitter
        content = getQuotes(self, category="happiness", api_key="As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk")
        print(content)
        t.statuses.update(
            status = content)
        print(content)
Twitterbot()