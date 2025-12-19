import dotenv as dv
import os
from google import genai


def check_content(content):
    dv.load_dotenv()
    genai.configure(api_key=os.environ["geminiapikey"])
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Check if the autor of the quote '{content}' is an extremist. if the author is an extremist return only 'True'. if the author is not an extremist return 'False'. if you cant define it return 'None'."
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    print(check_content(content="Ursula von der Leyen"))
