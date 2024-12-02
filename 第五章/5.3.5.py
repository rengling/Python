from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('C:/Users/admin/Desktop/警告框.html')
element = driver.find_element_by_tag_name('button').click()
alert = driver.switch_to_alert
print(alert.text)
time.sleep(1)
alert.accept()

driver.get('C:/Users/admin/Desktop/确认框.html')
element = driver.find_element_by_tag_name('button').click()
alert = driver.switch_to_alert
time.sleep(1)
alert.dismiss()

driver.get('C:/Users/admin/Desktop/提示框.html')
element = driver.find_element_by_tag_name('button').click()
alert = driver.switch_to_alert
time.sleep(1)
alert.send_keys('张三')
alert.accept()