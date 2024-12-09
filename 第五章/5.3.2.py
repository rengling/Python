from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://news.baidu.com")
element = driver.find_element(By.ID,'header-wrapper')
print(element.text)

driver.get("https://movie.douban.com/subject/30279836/comments?status=P")
element = driver.find_element(By.CLASS_NAME,'short')
print(element.text)

from selenium.webdriver.common.by import By
element = driver.find_element(by=By.CLASS_NAME,value='short')
print(element.text)
