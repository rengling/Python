from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = driver.find_element_by_id('header-wrapper')
print(element.text)

driver.get("https://movie.douban.com/subject/30279836/comments?status=P")
element = driver.find_element_by_class_name('short')
print(element.text)

from selenium.webdriver.common.by import By
element = driver.find_element(by=By.CLASS_NAME,value='short')
print(element.text)