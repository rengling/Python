from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
element = driver.find_element_by_id('s-top-loginbtn')
ActionChains(driver).click(on_element=element).perform()

from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.itcast.cn/')
element = driver.find_element_by_class_name('a_gd')
ActionChains(driver).move_to_element(element).perform()

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://portal.fuyunfeng.top/plugins_v2''/index.html#/slider-verify-example')
element = driver.find_element_by_xpath("//div[@id='circle']")
action = ActionChains(driver)
action.click_and_hold(element)
action.drag_and_drop_by_offset(element,100,0)
time.sleep(2)
action.perform()