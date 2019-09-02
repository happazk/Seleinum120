'''
Created on 2019年7月26日

@author: wangchaolin
'''
import unittest
from selenium import webdriver
from time import time
from random import choice
from selenium.webdriver.support.select import Select

class TestRegister(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
        self.driver = webdriver.Chrome()
        self.base_url ="http://172.31.31.100:8200/"
        # 设置元素识别超时时间
        self.driver.implicitly_wait(15)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(30)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(30)
        # 设置将谷歌浏览器最大化
        self.driver.maximize_window()

    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义测试数据
        email = str(time()*1000)[:13]+"@qq.com"
        password = "123456"
        name_list = ["艾","安","昂","敖","奥","巴","霸",
                     "白","柏","拜","班","包","保","葆",
                     "豹","鲍","暴","卑","贲","毕","闭",
                     "秘","边","鞭","彪","别","宾","邴",
                     "秉","薄","卜","布","部","才","王"]
        name = choice(name_list)+choice(name_list)
        # 点击 注册
        driver.find_element_by_link_text("注册").click()
        # 输入邮箱地址 
        driver.find_element_by_name("email").send_keys(email)
        # 输入登录密码 
        driver.find_element_by_name("passwd").send_keys(password)
        # 输入确认密码 
        driver.find_element_by_name("repasswd").send_keys(password)
        # 输入姓名 
        driver.find_element_by_name("name").send_keys(name)
        # 设置性别为男 
        driver.find_element_by_xpath("//input[@name='sex' and @value='1']").click()
        # 点击选择地区  
        driver.find_element_by_class_name("btn_b").click()
        # 点击 四川
        driver.find_element_by_link_text("四川").click()
        # 点击 成都市
        driver.find_element_by_link_text("成都市").click()
        # 点击确定 
        driver.find_element_by_name("input").click()
        # 将隐私设置为任何人可见 方式一：直接定位
        driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
#         # 方式二：通过Select类
#         select_element = driver.find_element_by_name("baseinfoprivacy")
#         sel = Select(select_element)
#         sel.select_by_value("0")
#         # 方式三：一级一级找
#         driver.find_element_by_name("baseinfoprivacy").\
#             find_element_by_xpath("//option[@value='0']").click()
        # 点击立即注册 
        driver.find_element_by_name("button").click()
        # 取得中转页面的提示，并判断：注册成功! 
        actual_tip = driver.find_element_by_xpath("//div[@class='message_box']/p[1]").text
        self.assertEqual("注册成功!", actual_tip)
        # 点击 基本资料
        driver.find_element_by_link_text("基本资料").click()
        # 定位出姓名输入框所在的input元素，并取出其value属性值进行判断
        actual_name = driver.find_element_by_name("name").get_attribute("value")
        # 第四步：判断测试结果
        self.assertEqual(name, actual_name)
    
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

