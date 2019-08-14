'''
Created on 2019年6月28日

@author: wangchaolin

备注：此模块提供注册页面相关的页面元素及逻辑操作
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageobject.page import doReg, Info
from unittest.case import TestCase

'''
页面元素部分
'''
EMAIL_ELEMENT = [By.NAME, "email"]
PASSWORD_ELEMENT = [By.NAME, "passwd"]
REPASSWORD_ELEMENT = [By.NAME, "repasswd"]
NAME_ELEMENT = [By.NAME, "name"]
SEX_MALE_ELEMENT = [By.XPATH, "//input[@name='sex' and @value='1']"]
SEX_FEMALE_ELEMENT = [By.XPATH, "//input[@name='sex' and @value='0']"]
SELECT_AREA_ELEMENT = [By.CLASS_NAME, "btn_b"]
PROVINCE_ELEMENT = [By.LINK_TEXT, "四川"]
CITY_ELEMENT = [By.LINK_TEXT, "成都市"]
OK_BUTTON_ELEMENT = [By.NAME, "input"]
PRIVACY_SELECT_ELEMENT = [By.NAME, "baseinfoprivacy"]
REGISTER_BUTTON_ELEMENT = [By.NAME, "button"]
ERROR_EMAIL_TIP_ELEMENT = [By.ID, "error_email"]
SUCCESS_TIP = "注册成功!"

'''
逻辑操作部分
'''
def input_necessary_parameters(driver, email, passwd, repasswd, name, sex=1, 
                               province=None, city=None):
    driver.find_element(*EMAIL_ELEMENT).send_keys(email)
    driver.find_element(*PASSWORD_ELEMENT).send_keys(passwd)
    driver.find_element(*REPASSWORD_ELEMENT).send_keys(repasswd)
    driver.find_element(*NAME_ELEMENT).send_keys(name)
    if sex == 1:
        driver.find_element(*SEX_MALE_ELEMENT).click()
    else:
        driver.find_element(*SEX_FEMALE_ELEMENT).click()
    driver.find_element(*SELECT_AREA_ELEMENT).click()
    if province != None:
        PROVINCE_ELEMENT[1] = province
    driver.find_element(*PROVINCE_ELEMENT).click()
    if city != None:
        CITY_ELEMENT[1] = city
    driver.find_element(*CITY_ELEMENT).click()
    driver.find_element(*OK_BUTTON_ELEMENT).click()

def select_birthday(driver):
    pass

def select_privacy(driver, privacy): 
    privacy_element = driver.find_element(*PRIVACY_SELECT_ELEMENT)
    privacy_select = Select(privacy_element)  
    privacy_select.select_by_visible_text(privacy)

def click_register_button(driver):
    driver.find_element(*REGISTER_BUTTON_ELEMENT).click()

def check_result(driver, case, name):
    # 实例化一个TestCase类
    tc = TestCase()
    if "正常测试" in case:
        # 判断注册成功的提示
        success_tip = doReg.get_success_tip(driver)
        tc.assertEqual(SUCCESS_TIP, success_tip)
        # 判断用户信息姓名是否正确
        Info.click_base_info_link(driver)
        actual_name = Info.get_name_from_info(driver)
        tc.assertEqual(name, actual_name)
    elif "异常测试" in case:
        if "邮箱" in case:
            tip = driver.find_element(*ERROR_EMAIL_TIP_ELEMENT).text
            tc.assertIn(tip, case)
        elif "密码" in case:
            pass
        else:
            raise TypeError(f"异常测试时，测试用例名称不符合规范，请检查case参数的值：{case}")
    else:
        raise TypeError(f"测试用例名称不符合规范，请检查case参数的值：{case}")
    
    