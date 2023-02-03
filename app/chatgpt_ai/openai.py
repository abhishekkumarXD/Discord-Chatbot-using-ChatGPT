# load_dotenv imports our environment variables placed 
# within the .env file
from dotenv import load_dotenv

import openai

# To interact with the operating system
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    # Creating an API request using the OpenAi library
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 1,
        max_tokens = 100
    )

    # Response given from this API request will be a 
    # JSON body. Thereby we need to extract the actual
    # response given by ChatGPT

    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response