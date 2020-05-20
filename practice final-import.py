#!/usr/bin/env python3
# Anchor extraction from HTML document
# convert text into list
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup


def getRecipeCrawler(element):
    baseUrl = 'https://haemukja.com/recipes?sort=rlv&name='
    #plusUrl = input("검색어를 입력하세요: ")
    url = baseUrl + urllib.parse.quote_plus(element)
    html = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
    soup = BeautifulSoup(html, 'html.parser')

    result = []
    i = 0
    for anchor in soup.select('a.call_recipe > strong'):
        print(anchor.get_text())
        i += 1

        recipe_obj = {
        'recipe_ID': i,
        'recipe_Name': anchor.get_text(),
        'ingredient_Key': element
        }

        result.append(recipe_obj)
        
    return result

if __name__=='__main__':
    crawler = getRecipeCrawler("감자")
    print(crawler)
