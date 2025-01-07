from openai import OpenAI
import dotenv as dv
import os
import google.generativeai as genai


def check_content(content):
    dv.load_dotenv()
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Check if the autor of the quote '{content}' is an extremist. if the author is an extremist return only 'True'. if the author is not an extremist return 'False'"
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    print(check_content(content="Olaf Scholz"))
