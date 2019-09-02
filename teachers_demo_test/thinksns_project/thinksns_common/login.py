'''
Created on 2019年7月29日

@author: Administrator

备注：此模块提供登录相关的方法
'''
from unittest.case import TestCase

def login_thinksns(driver, email, password, name):
    # ********************登录ThinkSNS********************
    # 输入邮箱地址 
    driver.find_element_by_name("email").send_keys(email)
    # 输入登录密码 
    driver.find_element_by_name("passwd").send_keys(password)
    # 点击登录按钮 
    driver.find_element_by_name("button").click()
    # 取出首页显示的用户姓名，并进行对比  
    actual_name = driver.find_element_by_id("my_name").text
    TestCase().assertEqual(name, actual_name)
    