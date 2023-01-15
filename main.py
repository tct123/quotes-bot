from twitter import *
from quotesgeneratorapi import quotes
import data

class Twitterbot():
    def __init__(self):
        quotes.getQuotes()
Twitterbot()