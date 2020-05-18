import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from random import randint

class getRecipeCrawlerRand:
    def __init__(self):
        self.url = 'https://www.haemukja.com/'
        self.nextPage = [
            '//*[@id="content"]/section/div[2]/div/div[2]/a[2]',
            '//*[@id="content"]/section/div[2]/div/div[2]/a[5]',
            '//*[@id="content"]/section/div[2]/div/div[2]/a[6]',
            '//*[@id="content"]/section/div[2]/div/div[2]/a[7]'
            ]
        self.location = 'a.call_recipe > strong'
        self.ingKey = ['감자', '양파', '옥수수', '마늘', '식빵']

    def launch_crawler(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)

    def find_click(self, xpath, sleep_interval=3):
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()
        time.sleep(sleep_interval)
    
    def find_recipe(self, ingredient):
        search_box = self.driver.find_element_by_name('name')
        search_box.send_keys(ingredient)
        search_box.submit()

    def get_recipe(self, element):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, 'html.parser')
        recipeName = self.soup.select(element)
        for recipe in recipeName:
            print(recipe.text)

    def run(self):
        self.launch_crawler()
        
        key = self.ingKey[randint(0, len(self.ingKey)-1)]
        self.find_recipe(key)

        for i in range(len(self.nextPage)):
            self.get_recipe(self.location)
        
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    crawler = getRecipeCrawlerRand()
    crawler.run()