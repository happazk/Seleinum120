'''
Created on 2019年6月28日

@author: wangchaolin

备注：此模块提供注册跳转页相关的页面元素及逻辑操作
'''
from selenium.webdriver.common.by import By

'''
页面元素部分
'''
SUCCESS_TIP_ELEMENT = [By.XPATH, "//div[@class='message_box']/p[1]"]

'''
逻辑操作部分
'''
def get_success_tip(driver):
    return driver.find_element(*SUCCESS_TIP_ELEMENT).text