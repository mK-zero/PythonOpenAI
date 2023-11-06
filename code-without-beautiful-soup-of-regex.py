import requests
import openai
import settings

openai.api_key = settings.APIKEY

url = "https://arstechnica.com/science/2023/07/the-heat-wave-scorching-the-us-is-a-self-perpetuating-monster/"
page = requests.get(url).text

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a journalist."},
        {"role": "assistant", "content": "Write a 100 word summary of this article"},
        {"role": "user", "content": page}
    ]
)
summary = response["choices"][0]["message"]["content"]

print(url)
print(soup.title.get_text())
for x in article:
    print(x.get_text)
    