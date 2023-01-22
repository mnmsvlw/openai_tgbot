import openai
from keys import API_KEY, ORG_ID

def openai_request(text):
    
    openai.organization = ORG_ID
    openai.api_key = API_KEY
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=2048,
        temperature=0
    )

    return response['choices'][0]['text']

