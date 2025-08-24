import requests
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com/"
url="https://en.wikipedia.org/wiki/List_of_banks_in_Kenya"

response = requests.get(url)
print(response)

# if response.status_code == 200:
#     print("fetched successfully")
# else:print("error")

soup=BeautifulSoup(response.text, "html.parser")
# # one=soup.find("div", class_="quote")
# # print(one)

# soup=BeautifulSoup(response.text, "html.parser")
# one=soup.find_all("div", class_="quote")
# # print(one)

# one=soup.find("div", class_="tags")
# # print(one)

# one=soup.find_all("div", class_="tags")
# # print(one)

# one=soup.find("div", class_="tags")
# # print(one.text)

# # fone=soup.ind_all("div", class_="tags")
# # print(one.text)
# # for i in one:
# #     print(i.text)

# # link=one.find("a", class_="tag")
# #     # print(link)

# # link=one.find_all("a", class_="tag")
# # for j in link:
# #     print(link.text)
# #     print(link['href'])

# quotes=soup.find_all("span", class_="text")
# for quote in quotes:
#     print(quote.text)
    
# author=soup.find_all("small", class_="author")
# for auth in author:
#     print(auth.text)



# #scrape all top ten tags and the links to the tags
# tags = soup.find_all("span", class_="tags-item")
# print(tags)

# for tag in tags:
#     print(tag.text)
#     link=tag.find("a", class_="tag")
#     print(link['href'])


# main=soup.find("div",class_="mw-content-ltr mw-parser-output")
# print(main)
# items=main.find("ul")
# links=items.find_all("li")
# for link in links:
#     print(link.text)

page=1
while page<2:
    url=f"https://en.wikipedia.org/wiki/List_of_banks_in_Kenya/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    authors= soup.find_all("small", class_="author")
    for author in authors:
        print(author.text)
    
