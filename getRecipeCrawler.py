import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class getRecipeCrawler:
    def __init__(self):
        self.url = 'https://www.haemukja.com/'
        self.nextPage = '//*[@id="content"]/section/div[2]/div/div[2]/a[2]'
        self.location = 'a.call_recipe > strong'
        #self.html = driver.page_source
        #self.soup = BeautifulSoup(html, 'html.parser')

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

    def launch_soup(self):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

    def get_recipe(self, element):
        recipeName = self.soup.select(element)
        for recipe in recipeName:
            print(recipe.text)

    def run(self):
        self.launch_crawler()
        
        key = input("재료를 입력하세요: ")
        self.find_recipe(key)

        #self.launch_soup()
        self.get_recipe(self.location)

        self.find_click(nextPage)
        self.get_recipe(self.location)

if __name__ == "__main__":
    crawler = getRecipeCrawler()
    crawler.run()