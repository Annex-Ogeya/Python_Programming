# #data extraction based on pattern definition
# #modules ;re

# #methods of researching

import re
# text="we are learning regex in python"
# patern="python"
# match=re.search(patern,text)
# print(match)

# If match:print("match found")

# else:print("match not found")

# text='acb a1b aab bb'
# pattern="a.b"
# matches = re.findall(pattern,text)
# print(matches)

# pattern=r"a*b"
# matches= re.findall(pattern text)
# print(matches)

#pattern=r"a*b":a can be repeated 0 times or more
#pattern=r"a+b":a can be repeated 1 time or more,b is mandatory
#pattern=r"a?b":a can be repeated 0 or 1 time,b is mandatory
#pattern=r"a{2}b":a can be repeated 2 times,b is mandatory

# pattern=r"a?b"
# matches = re.findall(pattern, text)
# print(matches)

#character classes
#pattern=r"[a-z]":matches any character from a to z"

#.grouping

#anchors 
# text="we are learning regex in python"
# pattern= r"^python"
# match =re.search(pattern, text)

#special sequences
# pattern=r"[a-z0-9]"
# match=re.findall(pattern ,text)
# print(match)

# text="cat scatter category"
# pattern = r"cat"
# match=re.findall(pattern,text)
# print(match)

# text="cat scatter category"
# pattern=r"\bscatter\b"
# match=re.findall(pattern,text)
# print(match)

#word boundaries....\b

# text="cat scatter category"
# pattern=r"\bcat\b"
# match=re.findall(pattern,text)
# print(match)

#\B=Not a word boundary
#text="regex is fun"
# match=re.findall(r"\Bfun\B")
# print(match)

# find all words starting with py
# text="python is fun python programming"
# pattern=r"py\w*"
# match=re.findall(pattern,text)
# print(match)

#to get a standalone word
text="3pythen pyoo python is fun python programming"
pattern=r"\bpy\w*\b"
match=re.findall(pattern,text)
# print(match)

#find all words that have letters within them o or e in them
text="Hello world,I love python"
pattern=r"\w*[oe]\w*"
match=re.findall(pattern,text)
# print(match)

#find all 4 digit numbers
text="Year 2025 number 123456789"
pattern=r"\d{4}"
match=re.findall(pattern,text)
# 
text="my number is 0798745723,my email is ogeya23456"
pattern=r"\d{4}"
match=re.findall(pattern,text)
# print(match)

text="phone number is (254) 456-7890"
pattern=r"\(\d{3}\) \d{3}-\d{4}"
match=re.findall(pattern,text)
# print(match)

# text="phone number is (254) 456-7890"
# pattern=r"(\(\d{3}\))\s(\d{3}-\d{4})"
# match=re.search(pattern,text)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))

text=f"""
My email is user@example.com,or contact@domain.com"""
pattern=r"[\w\.-]+@[\w\.-]+\.\w+"
#pattern=r"\b[a-z]+@[a-z]+\.com\b"
#pattern=r"\b\w*[@]\w*\.com"
match=re.findall(pattern,text)
# print(match)

