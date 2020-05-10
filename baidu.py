import requests
import time
from selenium import webdriver

start_url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url=start_url)

html = driver.page_source
print(html)
time.sleep(2)

driver.close()