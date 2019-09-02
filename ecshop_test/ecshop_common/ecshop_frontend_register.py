from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

REGISTER_USERNAME_ELEMENT = [By.ID, 'username']  # 用户名
REGISTER_EMAIL_ELEMENT = [By.ID, 'email']  # 邮箱
REGISTER_PASS_ELEMENT = [By.ID, 'password']  # 密码
REGISTER_REPASS_ELEMENT = [By.ID, 'conform_password']  # 确认密码
REGISTER_MSN_ELEMENT = [By.NAME, 'extend_field1']  # MSN
REGISTER_QQ_ELEMENT = [By.NAME, 'extend_field2']  # QQ
REGISTER_WORKPHONE_ELEMENT = [By.NAME, 'extend_field3']  # 办公电话
REGISTER_FAMILY_PHONE_ELEMENT = [By.NAME, 'extend_field4']  # 家庭电话
REGISTER_PHONE_ELEMENT = [By.NAME, 'extend_field5']  # 手机
REGISTER_SELECT_ELEMENT = [By.NAME, 'sel_question']  # 下拉框，密码提示问题
REGISTER_SELECT_ANSER_ELEMENT = [By.NAME, 'passwd_answer']  # 密码问题答案


def register_ecshop(driver, username='', password='', email='', msn='', qq='', work_phone='', work_family_phone='',
                    phone='', select_value='motto', anser=''):
    """

    :param driver:
    :param username:
    :param password:
    :param email:
    :param msn:
    :param qq:
    :param work_phone:
    :param work_family_phone:
    :param phone:
    :param select:
    :param anser:
    :return:
    """
    driver.get(REGISTER_URL)
    # 填写信息
    driver.find_element(*REGISTER_USERNAME_ELEMENT).send_keys(username)
    driver.find_element(*REGISTER_EMAIL_ELEMENT).send_keys(email)
    driver.find_element(*REGISTER_PASS_ELEMENT).send_keys(password)
    driver.find_element(*REGISTER_REPASS_ELEMENT).send_keys(password)
    driver.find_element(*REGISTER_MSN_ELEMENT).send_keys(msn)
    driver.find_element(*REGISTER_QQ_ELEMENT).send_keys(qq)
    driver.find_element(*REGISTER_WORKPHONE_ELEMENT).send_keys(work_phone)
    driver.find_element(*REGISTER_FAMILY_PHONE_ELEMENT).send_keys(work_family_phone)
    driver.find_element(*REGISTER_PHONE_ELEMENT).send_keys(phone)
    #下拉框
    select_element = driver.find_element(REGISTER_SELECT_ELEMENT)
    select = Select(select_element)
    select.select_by_value(select_value)
    #提示问题答案
    driver.find_element()

REGISTER_URL = 'http://172.31.21.138/user.php?act=register'
