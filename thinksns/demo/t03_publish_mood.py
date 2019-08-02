from random import choice
import unittest

from time import sleep, time

from selenium import webdriver

# from thinksns.thinksns_common.login import login_thinksns
from thinksns.thinksns_common import login_thinksns


class TestPublishMood(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)  # 页面元素识别时间15s
        self.driver.set_script_timeout(30)  # 异步脚本等待时间30s
        self.driver.set_page_load_timeout(30)  # 页面加载时间30s
        self.driver.maximize_window()  # 窗口最大化
        self.base_url = 'http://192.168.102.151/ThinkSNS/'  # 访问网址

    def test_mood(self):
        driver = self.driver
        driver.get(self.base_url)
        # 定义数据
        email_a = 'class120_A@qq.com'
        name_a = '钟凯A'
        password_a = '123456'
        email_b = 'class120_B@qq.com'
        name_b = '钟凯B'
        password_b = '123456'
        # 心情文本内容
        mood_text = str(time())

        # 主用户登录
        login_thinksns(driver, email_a, password_a, name_a)
        # 主用户发布心情成功
        # 点击左侧心情元素
        # driver.find_element_by_xpath("//div[@class='user_app_list']/ul/li/a[contains(text(),'心情')]").click()
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("心情").click()
        # 查找心情发布框元素
        textarea_ele = driver.find_element_by_id("mini-coment")
        textarea_ele.click()
        textarea_ele.send_keys(mood_text)  # 输入文本心情

        # 查找所有图标心情元素
        # driver.find_elements_by_class_name("ico_link")
        img_eles_list = driver.find_elements_by_xpath("//div[@class='ico_link']/img")
        img_res = choice(img_eles_list)  # 随机选择一个表情
        ims_src = img_res.get_attribute('src')
        img_res.click()  # 点击表情

        # 点击发布
        driver.find_element_by_class_name("btn_big").click()
        # driver.find_element_by_xpath("//input[@class='btn_big']")

        sleep(2)
        # 检查发布心情是否正确
        actu_mood_text = driver.find_element_by_id("mini-content").text
        self.assertEqual(actu_mood_text, mood_text)  # 比较文本是否一致

        actu_src = driver.find_element_by_id("mini-content").find_element_by_tag_name('img').get_attribute('src')
        self.assertEqual(actu_src, ims_src)  # 比较图表链接地址是否一致

        self.driver.find_element_by_link_text("退出").click()

        # 好友用户登
        login_thinksns(driver, email_b, password_b, name_b)
        # 查看主用户心情显示

        # 点击心情元素
        # driver.find_element_by_xpath("//div[@class='user_app_list']/ul/li/a[contains(text(),'心情')]").click()
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("心情").click()

        # 点击心情
        # driver.find_element_by_xpath("//div[@class='tab-menu']/a[contains(text(),'好友的心情')]").click()

        # 查找心情元素，并获取相应心情文本和图表链接
        div_element = driver.find_elements_by_class_name("bg01")[0]  # 获取第一条心情
        actu_name = div_element.find_element_by_tag_name("strong").text  # 好友用户名
        self.assertEqual(actu_name, name_a)

        p_element = div_element.find_element_by_tag_name('p')
        actual_content = (p_element.text).split(' ')[0]  # 获取好友A的心情内容
        self.assertEqual(actual_content, mood_text)  # 文本心情比较

        actual_src = p_element.find_element_by_tag_name('img').get_attribute('src')  # 获取图表链接
        self.assertEqual(actual_src, actu_src)  # 比较表情链接地址是否一致

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
