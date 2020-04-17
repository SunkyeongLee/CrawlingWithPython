#!/usr/bin/env python3
# Anchor extraction from HTML document
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


url = 'https://haemukja.com/refrigerator'
html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
soup = BeautifulSoup(html, 'html.parser')

for anchor in soup.find_all("strong"):
    print(anchor.get_text())