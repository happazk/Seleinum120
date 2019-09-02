'''
Created on 2019年6月28日

@author: wangchaolin

备注：此模块提供系统首页相关的页面元素及逻辑操作
'''
from selenium.webdriver.common.by import By

'''
页面元素部分
'''
REGISTER_ELEMENT = [By.LINK_TEXT, "注册"]

'''
逻辑操作部分
'''
def click_register_link(driver):
    driver.find_element(*REGISTER_ELEMENT).click()