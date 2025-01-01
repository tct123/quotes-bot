from mastodon import Mastodon
import dotenv as dv
import os
import quotesgeneratorapi_wrapper as qg

dv.load_dotenv()


class Socialbot:
    def __init__(self):
        api_key = os.environ["apininjaskey"]
        category = "happiness"
        content = qg.getQuotes(api_key=api_key)  # category=category
        print(content)
        # Mastodon
        CLIENTKEY = os.environ["clientkey"]
        CLIENTSECRET = os.environ["clientsecret"]
        ACCESSTOKEN = os.environ["accesstoken"]
        mastodon = Mastodon(
            client_id=CLIENTKEY,
            client_secret=CLIENTSECRET,
            access_token=ACCESSTOKEN,
            api_base_url="https://mastodon.social",
        )
        mastodon.toot(content)


if __name__ == "__main__":
    Socialbot()
