from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.get("http://www.baidu.com")
driver.get("http://www.jd.com")
driver.back()
driver.forward()
driver.refresh()

print(driver.title)

print(driver.current_url)

driver.save_screenshot('jd.png')