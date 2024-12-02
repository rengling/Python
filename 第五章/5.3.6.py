from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = driver.find_element_by_link_text('新闻').click()
print(f'当前窗口句柄为:{driver.current_window_handle}')
print(f'所有窗口句柄为:{driver.window_handles}')
time.sleep(1)
driver.switch_to_window(driver.window_handles[0])