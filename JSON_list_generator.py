import openai
from dotenv import load_dotenv
import json
import argparse

def create_playlist(count = "5", prompt=""):
    load_dotenv(".env")
    client = openai.OpenAI()


    message = [
        {"role": "system", "content": """you are a helpful playlist generator assistant. you should generate a play list 
        according to a text prompt. you should return a JSON array in format {"artist":<name of artist>,"title:<title>"}"""},
        {"role": "user", "content": f"generate 5 songs base on: <songs about love> prompt"},
        {"role": "assistant", "content": """[{"artist": "Ed Sheeran", "title": "Thinking Out Loud"}, {"artist": "Adele", "title": "Someone Like You"}, {"artist": "John Legend", "title": "All of Me"}, {"artist": "Taylor Swift", "title": "Love Story"}, {"artist": "The Beatles", "title": "Something"}]"""},
        {"role": "user", "content": f"generate {count} songs base on: <{prompt}> prompt"}

    ]

    response = client.chat.completions.create(messages=message, model="gpt-3.5-turbo", max_tokens=400)

    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    print(create_playlist(6, "songs about love"))
