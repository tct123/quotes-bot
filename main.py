from mastodon import Mastodon
import dotenv as dv
import os
import time
from quotesgeneratorapi_wrapper.quotesgenerator import getQuotes

dv.load_dotenv()


class Socialbot:
    def __init__(self):
        api_key = os.getenv("APININJASKEY")
        category = "happiness"
        content = getQuotes(category=category, api_key=api_key)
        print(content)
        # Mastodon
        mastodon_email = os.getenv("MASTODON_EMAIL")
        mastodon_password = os.getenv("MASTODON_PASSWORD")
        CLIENTKEY = os.getenv("CLIENTKEY")
        CLIENTSECRET = os.getenv("CLIENTSECRET")
        ACCESSTOKEN = os.getenv("ACCESSTOKEN")
        mastodon = Mastodon(
            client_id=CLIENTKEY,
            client_secret=CLIENTSECRET,
            access_token=ACCESSTOKEN,
            api_base_url="https://mastodon.social",
        )
        mastodon.toot(content)


while True:
    Socialbot()
    time.sleep(3600)
