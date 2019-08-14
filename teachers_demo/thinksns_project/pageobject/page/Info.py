'''
Created on 2019年6月28日

@author: wangchaolin

备注：此模块提供登录后用户信息页相关的页面元素及逻辑操作
'''
from selenium.webdriver.common.by import By

'''
页面元素部分
'''
BASE_INFO_ELEMENT = [By.LINK_TEXT, "基本资料"]
NAME_ELEMENT = [By.NAME, "name"]

'''
逻辑操作部分
'''
def click_base_info_link(driver):
    driver.find_element(*BASE_INFO_ELEMENT).click()
    
def get_name_from_info(driver):
    return driver.find_element(*NAME_ELEMENT).get_attribute("value")