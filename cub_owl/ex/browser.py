from selenium import webdriver
import time
#driver = webdriver.naver-whale()
driver = webdriver.Chrome("/home/junsuyoun/flask/cub_owl/ex/chromedriver")
url="http://localhost:8080/"
driver.get(url)

#driver.implicitly_wait(10)
while(1):
    driver.refresh()
    time.sleep(5)


