from openai import OpenAI
from openai import api_key
from openai import organization

api_key = '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'
organization = 'org-F138ahY8KG6sHQI1mNWEHKuX'
client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={"type": "json_object"},
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)