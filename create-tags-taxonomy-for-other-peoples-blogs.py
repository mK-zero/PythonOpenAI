import requests
from bs4 import BeautifulSoup
import openai
import settings

openai.api_key = settings.APIKEY #-- remember to use environment variable and include gitignore

url = "https://arstechnica.com/gadgets/2023/07/with-macos-sonoma-intel-macs-are-still-getting-fewer-updates-than-they-used-to/"
page = requests.get(url).text

soup = BeautifulSoup(page,"html.parser")
item = soup.find_all('p')

print(url)
title = soup.title.get_text()
print(title)

article = ""
for x in item:
    article += f" {x.get_text()}"

print(article)

response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a journalist."},
            {"role": "assistant", "content": "give me 10 tags for this blog post"},
            {"role": "assistant", "content": "return them in a python list"},
            {"role": "assistant", "content": "formatted like ['tag1','tag2','tag3']"},
            {"role": "user", "content": article}
            ]
)
tag = response["choices"][0]["message"]["content"]

print(f"Tags:\n {tag}")