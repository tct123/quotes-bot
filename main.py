from twitter import *
from mastodon import *
# from quotesgenerator.main import *
from data import *
import requests  # Will be replaced
import json  # Will be replaced


class Twitterbot():
    def __init__(self):
        # Mastodon
        t = Twitter(auth=OAuth(TOKEN, TOKENSECRET,
                    CONSUMERKEY, CONSUMERSECRET))  # Twitter
        content = getQuotes(self, category="happiness",
                            api_key="As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk")
        print(content)
        t.statuses.update(
            status=content)
        print(content)

    def getQuotes(self, category, api_key):
        api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code == requests.codes.ok:
            data = response.json()
            quote = data[0]["quote"]
            author = data[0]["author"]
            content = f"{quote}\n\n{author}"
            return content
        else:
            print("Error:", response.status_code, response.text)


Twitterbot()
