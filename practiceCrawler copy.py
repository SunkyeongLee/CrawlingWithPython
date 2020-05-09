import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.haemukja.com');   	# 해먹남녀 접속
time.sleep(2)					# 2초간 동작하는 걸 봅시다

search_box = driver.find_element_by_name('name')   # element name이 q인 곳을 찾아
search_box.send_keys('감자')		# 키워드를 입력하고
search_box.submit()				# 실행합니다.

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

recipeName = soup.select('a.call_recipe > strong')

for recipe in recipeName:
    print(recipe.text)

time.sleep(2)

search_box = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/div[2]/a[2]')
search_box.click()

time.sleep(2)

recipeNames = soup.select('a.call_recipe > strong')

for recipe in recipeNames:
    print(recipe.text)


time.sleep(10)					# 2초간 동작하는 걸 봅시다
driver.quit()

