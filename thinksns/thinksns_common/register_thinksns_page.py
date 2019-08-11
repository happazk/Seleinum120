# 设置页面元素
import time
from unittest.case import TestCase

from selenium import webdriver

# 点击注册元素
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

REGISTER_ELEMENT_01 = [By.LINK_TEXT, '注册']
REGISTER_ELEMENT_02 = [By.XPATH, '//div[@class="alC"]/a']
# 用户邮箱，密码，用户名元素
REGISERT_EMAIL_ELEMENT = [By.NAME, 'email']
REGISERT_PASSWD_ELEMENT = [By.NAME, 'passwd']
REGISERT_REPASSWD_ELEMENT = [By.NAME, 'repasswd']
REGISERT_NAME_ELEMENT = [By.NAME, 'name']
# 设置性别元素
SEX_MALE_ELEMENT = [By.XPATH, "//input[@name='sex' and  @value='1']"]
SEX_FEMALEE_ELEMENT = [By.XPATH, "//input[@name='sex' and  @value='0']"]
# 出生日期元素
SELECT_BIRTHDAT_YEAR_ELEMENT = [By.NAME, 'birthday_year']
SELECT_BIRTHDAT_MONTH_ELEMENT = [By.NAME, 'birthday_month']
SELECT_BIRTHDAT_DAY_ELEMENT = [By.NAME, 'birthday_day']
# 选择地区元素
SELECT_REGION_ELEMENT = [By.XPATH, "//input[@class='btn_b']"]
SELECT_PROVINCE_ELEMENT = [By.LINK_TEXT, "四川"]
SELECT_CITY_ELEMENT = [By.LINK_TEXT, "成都市"]
SELECT_OK_ELEMENT = [By.XPATH, "//div[@id='f_button']/input[@class='btn_b']"]
SELECT_CANCEL_ELEMENT = [By.XPATH, "//div[@id='f_button']/input[@class='btn_w']"]
# 隐私设置元素
SELECT_PRIVACY_ELEMENT = [By.NAME, "baseinfoprivacy"]
# SNS社区网服务条款元素
TERMS_ELEMENT = [By.LINK_TEXT, "SNS社区网服务条款"]
# 提交注册元素
SUBMIT_ELEMENT = [By.CLASS_NAME, "btn_reg"]
# 注册成功跳转时的页面元素
REGISTER_INFO_ELEMENT = [By.XPATH, "//div[@class='message_box']/p[1]"]
BASE_URL = 'http://192.168.102.151/ThinkSNS/'

# 方法
def register_thinksns(driver, reg_username, reg_password, reg_email):
    """
    function:注册thinksns用户
    :return:
    """
    # 打开被测网站
    driver.get(BASE_URL)
    # 1、点击注册跳转页面
    # driver.find_element_by_link_text("注册").click()
    driver.find_element(*REGISTER_ELEMENT_01).click()
    # 2、注册界面内容填入
    # driver.find_element_by_name("email").send_keys(reg_email)
    # driver.find_element_by_name("passwd").send_keys(reg_password)  # password
    # driver.find_element_by_name("repasswd").send_keys(reg_password)  # 确认密码
    # driver.find_element_by_name("NAME).send_keys(reg_username)  # 姓名
    driver.find_element(*REGISERT_EMAIL_ELEMENT).send_keys(reg_email)
    driver.find_element(*REGISERT_PASSWD_ELEMENT).send_keys(reg_password)
    driver.find_element(*REGISERT_REPASSWD_ELEMENT).send_keys(reg_password)
    driver.find_element(*REGISERT_NAME_ELEMENT).send_keys(reg_username)
    # driver.find_element_by_xpath("//input[@name='sex' and  @value='1']").click()  # 性别
    driver.find_element(*SEX_FEMALEE_ELEMENT).click()

    # 地区选择
    # driver.find_element_by_class_name("btn_b").click()
    # driver.find_element_by_link_text("四川").click()
    # driver.find_element_by_link_text("成都市").click()
    # driver.find_element_by_name("input").click()  # 提交
    driver.find_element(*SELECT_REGION_ELEMENT).click()
    driver.find_element(*SELECT_PROVINCE_ELEMENT).click()
    driver.find_element(*SELECT_CITY_ELEMENT).click()
    driver.find_element(*SELECT_OK_ELEMENT).click()

    # 隐私设置,直接方式
    # driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
    # select_ele = driver.find_element_by_name('baseinfoprivacy')
    # sel = Select(select_ele)
    # sel.select_by_value('0')
    select_ele = driver.find_element(*SELECT_PRIVACY_ELEMENT)
    sel = Select(select_ele)
    sel.select_by_value('0')

    # 点击同意注册
    # driver.find_element_by_name("button").click()
    driver.find_element(*SUBMIT_ELEMENT).click()

    # 页面跳转判断
    # res_text = driver.find_element_by_xpath("//div[@class='message_box']/p[1]").text
    res_text = driver.find_element(*REGISTER_INFO_ELEMENT).text

    TestCase().assertEqual("注册成功!", res_text)

    # 查看注册后的页面信息是否正确
    # driver.find_element_by_link_text('资料')
    # driver.find_element_by_xpath("//div[@class='nav_sub']/a[contains(text(),'资料')]").click()
    # count_name_res = driver.find_element_by_xpath("//input[@name='NAME]").get_attribute('value')
    # self.assertEqual(reg_username, count_name_res)
