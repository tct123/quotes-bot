#from twitter import *
from mastodon import *
# from quotesgenerator.main import *
import dotenv as dv
import requests  # Will be replaced
import json  # Will be replaced
import time
dv.load_dotenv()


class Socialbot():
    def __init__(self):
        api_key = "As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk"
        category = "happiness"
        # Mastodon
        Mastodon.create_app(
            'InspiringQuotes',
            api_base_url='https://mastodon.social',
            to_file='pytooter_clientcred.secret'
        )
        mastodon = Mastodon(client_id='pytooter_clientcred.secret',)
        mastodon.log_in(
            f'{mastodon_email}',
            f'{mastodon_password}',
            to_file='pytooter_usercred.secret')
        mastodon = Mastodon(access_token='pytooter_usercred.secret')
        # t = Twitter(auth=OAuth(TOKEN, TOKENSECRET, CONSUMERKEY, CONSUMERSECRET))  # Twitter
        api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        if response.status_code == requests.codes.ok:
            data = response.json()
            quote = data[0]["quote"]
            author = data[0]["author"]
            content = f"{quote}\n\n{author}"
            print(content)
            mastodon.toot(content)
        else:
            print("Error:", response.status_code, response.text)

        # t.statuses.update(status=content)

    def getQuotes(self, category, api_key):
        pass


while True:
    Socialbot()
    time.sleep(3600)
