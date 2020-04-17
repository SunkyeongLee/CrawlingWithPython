#!/usr/bin/env python3
# Anchor extraction from HTML document
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
import json
from collections import OrderedDict


url = 'https://haemukja.com/main#'
html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
soup = BeautifulSoup(html, 'html.parser')

file_data = OrderedDict()

j=0
for anchor in soup.select("strong"):
    print(anchor.get_text())
    j+=1
    file_data["Ingredient_ID"] = j
    file_data["Category_ID"] = 1
    file_data["Ingredient_Name"] = anchor.get_text()
    print(json.dumps(file_data, ensure_ascii=False, indent=""))

with open('words.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="")



# for i in range(j):
#    file_data["Ingredient_ID"] = i
#    file_data["Category_ID"] = 1
#    file_data["Ingredient_Name"] = anchor.get_text()
#     print(json.dumps(file_data, ensure_ascii=False, indent=""))

#     with open('words.json', 'w', encoding="utf-8") as make_file:
#         json.dump(file_data, make_file, ensure_ascii=False, indent="")



