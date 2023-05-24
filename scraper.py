import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/History_of_Mexico"

page=requests.get(url)
print(page.content)
