import requests
from bs4 import BeautifulSoup

url="https://jumia.co.ke/"
response = requests.get(url)
# print(response)

soup=BeautifulSoup(response.text, "html.parser")
# one=soup.find("div", class_="quote")
# print(one)

soup=BeautifulSoup(response.text, "html.parser")
name=soup.find_all("div", class_=""itm col"")
print(name)