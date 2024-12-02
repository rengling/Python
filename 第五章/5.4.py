from selenium import webdriver
import time
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class JiXinDa:
    def __init__(self):
        self.url = 'http://jxd.itheima.net/#/login'
        self.driver = webdriver.Chrome()
    def login_to_find(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('el-button').click()
        self.driver.find_element_by_id('button').click()
        sms_service_element = self.driver.find_element_by_xpath('//div[contains(@class,"sider-bar") and contains(@class,"scole-bar")]/ul/li[2]/div/div/span')
        webdriver.ActionChains(self.driver).move_to_element(sms_service_element).click(sms_service_element).perform()
        service_log = self.driver.find_element_by_xpath('//div[contains(@class,"sider-bar") and contains(@class,"scole-bar")]/ul/li[2]/ul/li/ul/li[5]')
        webdriver.ActionChains(self.driver).move_to_element(service_log).click(service_log).perform()
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="ReceiveLog"]/div/form/div/div[1]//div/input')))
        self.driver.find_element_by_xpath('//div[@class="ReceiveLog"]/div/form/div/div[1]//div/input').send_keys('黑马头条')
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="ReceiveLog"]/div/form/div/div[4]//div/input')))
        self.driver.find_element_by_xpath('//div[@class="ReceiveLog"]/div/form/div/div[4]//div/input').send_keys('黑马头条')
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="el-row"]/div[5]//div/button[1]/span[1]')))
        self.driver.find_element_by_xpath('//div[@class="el-row"]/div[5]//div/button[1]/span[1]').click()
    def get_data(self):
            title_li= []
            for i in range(1, 9):
                title = self.driver.find_element_by_xpath(f'//div[@class="ReceiveLog"]/div[2]//thead//th[(i)]').text
                title_li.append(title)
            content_info= []
            num = self.driver.find_elements_by_xpath('//div[@class="ReceiveLog"]//table[@class="el-table body"]//tr')
            for i in range(1, len(num) + 1):
             content = self.driver.find_element_by_xpath(f'//div[@class="ReceiveLog"]//'f'table[@class="el-table body"]//tr[(i)]').text
             content_info.append(dict(zip(title_li, content.splitlines()))) 
            return content_info
    def save_data(self, data):
        try:
            with open('jixinda.json',mode='a+',encoding='utf-8')as f:
                f.write(json.dumps(data,ensure_ascii=False))
        except Exception as e:
            print(e)
        return False
    def run(self):
        self.login_to_find()
        num = 1
        while True:
            button = self.driver.find_element_by_xpath('//div[@class="ReceiveLog"]//div/button[@class="btn-next"]')
            if button.is_enabled():
                data = self.get_data()
                self.save_data(data)
                print(f'正在保存第{num}页数据')
                print(data)
                num += 1
                button.click()
            else:
                end_data = self.get_data()
                print(f'正在保存第{num}页数据')
                self.save_data(end_data)
                print(end_data)
                self.driver.close()
                break
if __name__ == '__main__':
   jixinda = JiXinDa()
   jixinda.run()
