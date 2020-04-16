#!/usr/bin/env python3
# Anchor extraction from HTML document
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


baseUrl = 'https://m.search.naver.com/search.naver?sm=mtb_hty.top&where=m_view&tqi=UpltIdprvP4ssuJ0Q0NssssssCG-070019&query='
plusUrl = input("검색어를 입력하세요: ")
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines total_tit')


for i in title:
    print(title)
    print("\n")