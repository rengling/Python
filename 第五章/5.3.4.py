from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('C:/Users/sun/Desktop/下拉列表框.html')
element = driver.find_element_by_tag_name('select')
select = Select(element)
select.select_by_index(1)