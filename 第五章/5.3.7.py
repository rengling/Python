from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.itcast.cn/')
driver.implicitly_wait(10)
driver.switch_to.frame('chatIframe')
element = driver.find_element_by_class_name('service')
print(element.text)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get('https://www.itcast.cn/')
driver.switch_to.frame('chatIframe')
element = WebDriverWait(driver,10).until(lambda x: x.find_element_by_class_name("service"))
print(element.text)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.itcast.cn/')
driver.switch_to.frame('chatIframe')
element = WebDriverWait(driver,10).until(EC.presence_of_elements_located((By.CLASS_NAME,"service")))
print(element.text)