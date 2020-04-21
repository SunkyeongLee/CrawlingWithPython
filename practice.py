#!/usr/bin/env python3
# Anchor extraction from HTML document
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


baseUrl = 'https://haemukja.com/recipes?sort=rlv&name='
plusUrl = input("검색어를 입력하세요: ")
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
soup = BeautifulSoup(html, 'html.parser')

for anchor in soup.find_all("a", class_="call_recipe"):
    print(anchor.get_text())
    #print(url + anchor.attrs['href'])