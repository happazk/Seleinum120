from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME_ELEMENT =[By.NAME,'username']
PASSWORD_ELEMENT = [By.NAME,'password']
REMEMBER_ELEMENT = [By.NAME,'remember']
SUBMIT = [By.CLASS_NAME,'button']

LOGIN_URL = 'http://172.31.21.138/admin/privilege.php?act=login'
USERNAME='admin'
PASSWORD = 'abc123456'

def loggin_back(driver, *args, **kwargs):
    driver.get(LOGIN_URL)
    driver.find_element(*USERNAME_ELEMENT).send_keys(USERNAME)
    driver.find_element(*PASSWORD_ELEMENT).send_keys(PASSWORD)
    #勾选保存登录信息
    driver.find_element(*REMEMBER_ELEMENT).click()
    #点击登录
    driver.find_element(*SUBMIT).click()


#
# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     loggin_back(driver=driver)



