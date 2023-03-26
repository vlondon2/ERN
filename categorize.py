import os
import openai
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def make_prompt(input):
        return f"Categorize the following text into one of the following categories: Natural Disaster, Medical, Safety\n\nText: {input}\n\nCategory options: Natural Disaster, Medical, Safety\n\nCategory:"

def generate(text):
    
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=make_prompt(text),
    )

    return response

def categorize_text(text):
    
    for i in range(3):
        cat = generate(text).choices[0].text.strip()

        if "Natural Disaster" in cat or "Medical" in cat or "Safety" in cat:
            break

    return cat
        