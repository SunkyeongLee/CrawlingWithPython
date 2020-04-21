#!/usr/bin/env python3
# Anchor extraction from HTML document
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


baseUrl = 'https://haemukja.com/recipes?utf8=✓&sort=rlv&name='
plusUrl = input("검색어를 입력하세요: ")
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all("strong")


for i in title:
    print(title)
    print("\n")