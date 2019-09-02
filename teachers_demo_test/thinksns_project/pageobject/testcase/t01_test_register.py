'''
Created on 2019年6月28日

@author: wangchaolin
'''
import unittest
from selenium import webdriver
from time import time, sleep
from random import choice
from pageobject.page import index, reg

class TestRegister(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
        self.driver = webdriver.Chrome()
        self.base_url = "http://172.31.31.100:8200/"
        # 设置元素识别超时时间
        self.driver.implicitly_wait(15)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(20)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(20)
        # 针对谷歌浏览器，将其最大化
        self.driver.maximize_window()

    def test_01(self):
        # 定义测试用例的名称
        case = "正常测试：输入所有必填项，可以成功注册！"
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义测试数据
        email = str(time()*1000)[:13] + "@qq.com"
        passwd = repasswd ="123456"
        name_list = ["艾","安","昂","敖","奥","巴","霸",
                     "白","柏","拜","班","包","保","葆",
                     "豹","鲍","暴","卑","贲","毕","闭",
                     "秘","边","鞭","彪","别","宾","邴",
                     "秉","薄","卜","布","部","才","王"]
        name = choice(name_list)+choice(name_list)
        # 点击首页注册
        index.click_register_link(driver)
        # 输入所有必填参数
        reg.input_necessary_parameters(driver, email, passwd, repasswd, name)
        # 点击注册
        reg.click_register_button(driver)
        # 检查结果
        reg.check_result(driver, case, name)
    
    def test_02(self):
        # 定义测试用例的名称
        case = "正常测试：输入所有必填项，并选择隐私为任何人可见，可以成功注册！"
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义测试数据
        email = str(time()*1000)[:13] + "@qq.com"
        passwd = repasswd ="123456"
        name_list = ["艾","安","昂","敖","奥","巴","霸",
                     "白","柏","拜","班","包","保","葆",
                     "豹","鲍","暴","卑","贲","毕","闭",
                     "秘","边","鞭","彪","别","宾","邴",
                     "秉","薄","卜","布","部","才","王"]
        name = choice(name_list)+choice(name_list)
        privacy = "任何人能看见我的资料和内容"
        # 点击首页注册
        index.click_register_link(driver)
        # 输入所有必填参数
        reg.input_necessary_parameters(driver, email, passwd, repasswd, name)
        # 进行隐私设置
        reg.select_privacy(driver, privacy)
        # 点击注册
        reg.click_register_button(driver)
        # 检查结果
        reg.check_result(driver, case, name)
    
    def test_03(self):
        # 定义测试用例的名称
        case = "异常测试：邮箱为空时进行注册，应提示：重要！请填有效邮箱地址，以收邮件完成注册"
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义测试数据
        email = ""
        passwd = repasswd ="123456"
        name_list = ["艾","安","昂","敖","奥","巴","霸",
                     "白","柏","拜","班","包","保","葆",
                     "豹","鲍","暴","卑","贲","毕","闭",
                     "秘","边","鞭","彪","别","宾","邴",
                     "秉","薄","卜","布","部","才","王"]
        name = choice(name_list)+choice(name_list)
        # 点击首页注册
        index.click_register_link(driver)
        # 输入所有必填参数
        reg.input_necessary_parameters(driver, email, passwd, repasswd, name)
        # 检查结果
        reg.check_result(driver, case, name)
        
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()



