import os
from random import choice, randint
import unittest
from configparser import *

from time import sleep, time

import jpype
from selenium import webdriver

from thinksns_test.thinksns_common import login_thinksns
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestUpImages(unittest.TestCase):
    def setUp(self):
        # 谷歌设置flash可用   (注意使用56的google)
        chrome_options = Options()
        prefs = {
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1
        }
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # 火狐设置flash可用
        # p = r"C:\Users\zhongkai\AppData\Roaming\Mozilla\Firefox\Profiles\av2teg2z.default"
        # profile = webdriver.FirefoxProfile(p)
        # profile.set_preference("plugin.state.flash", 2)
        # self.driver = webdriver.Firefox(profile)

        self.driver.implicitly_wait(15)  # 页面元素识别时间15s
        self.driver.set_script_timeout(30)  # 异步脚本等待时间30s
        self.driver.set_page_load_timeout(30)  # 页面加载时间30s
        self.driver.maximize_window()  # 窗口最大化
        self.base_url = 'http://192.168.102.151/ThinkSNS/'  # 访问网址
        self.base_path = os.path.dirname(os.getcwd())  # 定位到项目的thinksns目录
        # self.base_url = 'http://172.31.31.100:8200'  # 访问网址

    def test_up_imgs(self):
        """
        function:测试日志访问权限和评论权限
        :return:
        """
        driver = self.driver
        # 定义数据
        email = 'class120_A@qq.com'
        name = '钟凯A'
        password = '123456'
        # 用户登录
        login_thinksns(self.base_url, driver, email, password, name)
        # 点击右侧相册组件上传按钮
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("相册").click()
        # 获取相册初始数量
        pic_num = self.get_pictures_num(driver)
        # 点击"上传照片"
        driver.find_element_by_class_name("ico_add").click()
        sleep(1)

        # 启动JVM虚拟机 调用sikuli
        jvm_path = jpype.getDefaultJVMPath()
        sikuli_jar_path = "-Djava.class.path=" + os.path.dirname(os.getcwd()) + '\\Libs\\sikulixapi.jar'
        jpype.startJVM(jvm_path, sikuli_jar_path)
        # 生成对屏幕操作的python类
        Screen = jpype.JClass("org.sikuli.script.Screen")  # 找到sikulixapi.jar 中Screen类对应的路径
        # 实例化
        screen = Screen()

        # 谷歌点击设置flash可用
        # set_flash1_img_path = self.base_path + r"\imgs\sikuli_imgs\set_flash1.PNG"
        # screen.click(set_flash1_img_path)
        # sleep(10)
        # enable_flash_path = self.base_path + r"\imgs\sikuli_imgs\enable_flash.PNG"
        # screen.click(enable_flash_path)
        # sleep(10)
        # for i in range(3):
        #     blog_img_path = self.base_path + r"\imgs\sikuli_imgs\blog.png"
        #     screen.click(blog_img_path)
        #     sleep(2)
        #     gift_img_path = self.base_path + r"\imgs\sikuli_imgs\gift.png"
        #     screen.click(gift_img_path)

        # 定义添加图片按钮路径
        add_img_path = self.base_path + r"\imgs\sikuli_imgs\add.PNG"
        screen.click(add_img_path)
        input_img_path = self.base_path + r"\imgs\sikuli_imgs\input_file_path.PNG"
        screen.click(input_img_path)
        # 定义上传照片路径
        img1 = self.base_path + "\\imgs\\blog_imgs\\" + str(randint(0, 7)) + '.jpg'
        img2 = self.base_path + "\\imgs\\blog_imgs\\" + str(randint(0, 7)) + '.jpg'
        img_path = '"' + img1 + '" "' + img2 + '"'
        # 根据实例化对象，在输入框内输入上述路径
        screen.type(input_img_path, img_path)
        # 定义打开按钮的图片所在路径
        open_path = self.base_path + r"\imgs\sikuli_imgs\open.PNG"

        screen.click(open_path)
        sleep(1)
        jpype.shutdownJVM()

        # 上传图片
        driver.find_element_by_id('btnUpload').click()
        sleep(2)
        # 判断是否出现成功提示
        up_img_info = driver.find_element_by_name("save_upload_photos").text
        self.assertIn(" 照片上传成功！", up_img_info)
        driver.find_element_by_class_name("btn_b").click()
        sleep(1)

        # 点击左侧相册
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("相册").click()
        # 判断照片数量是否正确
        pic_num_res = self.get_pictures_num(driver)
        self.assertEqual(pic_num_res, pic_num + 1)

    def tearDown(self):
        self.driver.quit()

    def get_pictures_num(self, driver):
        """
        function:获取当前照片数量
        :param driver:
        :return:
        """

        res_str = driver.find_element_by_class_name("MenuSub").text
        res_str = '我的全部照片(0) ┊ 我的照片专辑'
        num = (res_str.split("(")[1]).split(")")[0]
        return int(num)


if __name__ == '__main__':
    unittest.main()
