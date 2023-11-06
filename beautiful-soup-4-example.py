import requests
from bs4 import BeautifulSoup

url = "https://arstechnica.com/science/2023/07/the-heat-wave-scorching-the-us-is-a-self-perpetuating-monster/"
page = requests.get(url).text

soup = BeautifulSoup(page, "html.parser")
article = soup.find_all('p')

print(url)
print(soup.title.get_text())
for x in article:
    print(x.get_text())
    