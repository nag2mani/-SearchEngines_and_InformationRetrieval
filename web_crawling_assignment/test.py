import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Apple'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
paragraphs = soup.find_all()

for paragraph in paragraphs:
    print(paragraph.text)

# print(paragraphs)