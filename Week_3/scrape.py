import requests
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com/"
response = requests.get(url)
print(response)

# if response.status_code == 200:
#     print("fetched successfully")
# else:print("error")

soup=BeautifulSoup(response.text, "html.parser")
# one=soup.find("div", class_="quote")
# print(one)

soup=BeautifulSoup(response.text, "html.parser")
one=soup.find_all("div", class_="quote")
# print(one)

one=soup.find("div", class_="tags")
# print(one)

one=soup.find_all("div", class_="tags")
# print(one)

one=soup.find("div", class_="tags")
# print(one.text)

# fone=soup.ind_all("div", class_="tags")
# print(one.text)
# for i in one:
#     print(i.text)

# link=one.find("a", class_="tag")
#     # print(link)

# link=one.find_all("a", class_="tag")
# for j in link:
#     print(link.text)
#     print(link['href'])

quotes=soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)
    
author=soup.find_all("small", class_="author")
for auth in author:
    print(auth.text)


