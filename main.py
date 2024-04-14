from mastodon import *
import dotenv as dv
import os
import time
from quotesgeneratorapi_wrapper.quotesgenerator import getQuotes

dv.load_dotenv()


class Socialbot:
    def __init__(self):
        api_key = os.getenv("APININJASKEY")
        category = "happiness"
        # Mastodon
        mastodon_email = os.getenv("MASTODON_EMAIL")
        mastodon_password = os.getenv("MASTODON_PASSWORD")
        Mastodon.create_app(
            "InspiringQuotes",
            api_base_url="https://mastodon.social",
            to_file="pytooter_clientcred.secret",
        )
        mastodon = Mastodon(
            client_id="pytooter_clientcred.secret",
        )
        mastodon.log_in(
            f"{mastodon_email}",
            f"{mastodon_password}",
            to_file="pytooter_usercred.secret",
        )
        mastodon = Mastodon(access_token="pytooter_usercred.secret")
        # t = Twitter(auth=OAuth(TOKEN, TOKENSECRET, CONSUMERKEY, CONSUMERSECRET))  # Twitter
        # t.statuses.update(status=content)
        content = getQuotes(category=category, api_key=api_key)
        print(content)
        mastodon.toot(content)


while True:
    Socialbot()
    time.sleep(3600)
