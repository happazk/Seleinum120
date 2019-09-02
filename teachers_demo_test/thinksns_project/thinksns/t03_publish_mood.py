'''
Created on 2019年7月29日

@author: wangchaolin
'''
import unittest
from selenium import webdriver
from time import sleep, time
# from thinksns_common.login import login_thinksns
from thinksns_common import login_thinksns
from random import choice

class TestPublishMood(unittest.TestCase):

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
        email_a = "wcl12001@qq.com"
        password_a = "123456"
        name_a = "王朝12001"
        email_b = "9291827@qq.com"
        password_b = "123456"
        name_b = "王朝林"
        # 调用登录方法，登录主账号
        login_thinksns(driver, email_a, password_a, name_a)
        # 先定位出左侧心情列表，再点击 心情  
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("心情").click()
        # 先定位出心情内容输入框所在的textarea元素  
        textarea = driver.find_element_by_id("mini-coment")
        # 点击该textarea元素
        textarea.click()
        # 定义随机文本内容（时间戳）
        content = str(time())
        # 根据textarea元素输入随机文本内容
        textarea.send_keys(content)
        # 先定位出所有心情图片所在的div元素  
        div_list = driver.find_elements_by_class_name("ico_link")
        # 再随机选出一个div元素
        div_element = choice(div_list)
        # 根据该div元素定位出其下一级的img元素
        img_element = div_element.find_element_by_tag_name("img")
        # 取出该img元素的src属性值
        src = img_element.get_attribute("src")
        # 再点击该img元素
        img_element.click()
        # 点击发布按钮  
        driver.find_element_by_class_name("btn_big").click()
        sleep(1)
        # 先定位出心情内容所在的span元素  
        span_element = driver.find_element_by_id("mini-content")
        # 取出该span元素的文本内容，并进行判断
        actual_content = span_element.text
        self.assertEqual(content, actual_content)
        # 再根据span元素定位出其下一级的img元素，并取出src属性值进行判断
        actual_src = span_element.find_element_by_tag_name("img").get_attribute("src")
        self.assertEqual(src, actual_src)
        # 点击 退出
        driver.find_element_by_link_text("退出").click()
        # 调用登录方法，登录好友账号
        login_thinksns(driver, email_b, password_b, name_b)
        # 先定位出左侧心情列表，再点击 心情 class user_app_list
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("心情").click()
        # 先定位出所有心情记录所在的div元素，并取出第一个  
        div_element = driver.find_elements_by_class_name("bg01")[0]
        # 根据div元素定位出其范围内的strong元素，并取出其文本值进行判断
        actual_name =div_element.find_element_by_tag_name("strong").text
        self.assertEqual(name_a, actual_name)
        # 根据div元素定位出其下一级的p元素
        p_element = div_element.find_element_by_tag_name("p")
        # 根据p元素取出其文本值，并进行判断（去掉最后的空格和回复）
        actual_content = p_element.text[:-3]
        self.assertEqual(content, actual_content)
        # 根据p元素定位出其下一级的img元素，并取出src属性值进行判断
        actual_src = p_element.find_element_by_tag_name("img").get_attribute("src")
        self.assertEqual(src, actual_src)
            
    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

