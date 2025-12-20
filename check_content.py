import dotenv as dv
import os
from google import genai


def check_content(content):
    dv.load_dotenv()
    client = genai.Client(api_key=os.environ["geminiapikey"])
    model = "gemini-2.5-flash"
    prompt = f"Check if the autor of the quote '{content}' is an extremist. if the author is an extremist return only 'True'. if the author is not an extremist return 'False'. if you cant define it return 'None'."
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text.strip()


if __name__ == "__main__":
    print(check_content(content="Ursula von der Leyen"))
