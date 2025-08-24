import requests
from bs4 import BeautifulSoup

url=https://en.wikipedia.org/wiki/List_of_banks_in_Kenya

main=soup.find("div",class_="mw-content-ltr mw-parser-output")
print(main)