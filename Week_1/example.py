#Decalre & initialize variables
# x=10
# y=20
# print(x+y)

# name="Annex"
# greeting="Hello"
# intro=greeting + name
# print(intro)

# greeting="Hello"
# name="Annex"
# intro=greeting + name
# print(greeting," ",name)

# a=35.0
# b=12.50
# c=a+b
# print(c)

hours=35.0
rate=12.50
pay=hours+rate
# print(pay)

import re
text="My email is user@examply.com,or contact@domain.com,or annexogeya2gmail.com"
pattern=r"\b\w*[@]w*\.com\b"
match=re.findall(pattern,text)
print(match)