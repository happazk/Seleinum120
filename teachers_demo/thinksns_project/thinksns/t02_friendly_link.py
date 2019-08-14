'''
Created on 2019年7月26日

@author: wangchaolin
'''
import unittest
from selenium import webdriver
from time import sleep

class TestFriendlyLink(unittest.TestCase):

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
        # 点击 友情链接
        driver.find_element_by_link_text("友情链接").click()
        # 点击 ThinkSNS
        driver.find_element_by_link_text("ThinkSNS").click()
        sleep(5)
        # 取得所有的窗口句柄，并取出第二个
        handle = driver.window_handles[1]
        # 切换到第二个窗口
        driver.switch_to_window(handle)
        sleep(1)
        # 第四步：判断测试结果
        self.assertEqual("ThinkSNS开源社交系统-SNS社交网站_APP软件开发_社交系统源码", driver.title)
    
    def test_02(self):
        print("hahahahahhahahhh")
    
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

