from openai import OpenAI
import dotenv as dv
import os

dv.load_dotenv()


def check_content(content):
    client = OpenAI(
        api_key=os.environ.get(
            "OPENAI_API_KEY"
        ),  # This is the default and can be omitted
    )
    prompt = f"Check if the autor of the quote '{content}' is an extremist. if it is true return only 'True'. if not return 'False'"
    chat_completition = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o",
    )
    return chat_completition


if __name__ == "__main__":
    check_content(content="")
