import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hi I am Vivek, and This is my first prompt engineering program!'}
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response['choices'][0]['message']['content'])