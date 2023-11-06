import requests
from bs4 import BeautifulSoup
import openai
import settings

openai.api_key = settings.APIKEY

url = "https://arstechnica.com/gadgets/2023/07/with-macos-sonoma-intel-macs-are-still-getting-fewer-updates-than-they-used-to/"
page = requests.get(url).text

soup = BeautifulSoup(page,"html.parser")
item = soup.find_all('p')

print(url)
title = soup.title.get_text()
print(title)

article =""
for x in item:
    article += f" {x.get_text()}"

print(article)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a journalist."},
        {"role": "assistant", "content": "write a 20 word summary of this article"},
        {"role": "user", "content": article}
    ]
)
summary = response["choices"][0]["message"]["content"]

print(f"Summary:\n {summary}")

file = open("parse.html", "w")
file.write(f"<h1>{title}</h1>")
file.close()

file = open("parse.html", "a")
file.write(f"<p><strong>URL: </strong>{url}</p>")
file.write(f"<h2>Summary:</h2><p>{summary}</p>")
file.write(f"<h2>Article:</h2><p>{article}</p>")
file.close()
