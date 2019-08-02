import unittest

from time import sleep

from selenium import webdriver


class TestFriendlyLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)  # 页面元素识别时间15s
        self.driver.set_script_timeout(30)  # 异步脚本等待时间30s
        self.driver.set_page_load_timeout(30)  # 页面加载时间30s
        self.driver.maximize_window()  # 窗口最大化
        self.base_url = 'http://192.168.102.151/ThinkSNS/'  # 访问网址

    def test_switch_window(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("友情链接").click()
        driver.find_element_by_xpath("//a[@target='_blank' and contains(text(),'ThinkSNS')]").click()
        sleep(6)
        handle = driver.window_handles[1]
        driver.switch_to_window(handle)
        sleep(2)
        self.assertEqual('ThinkSNS开源社交系统-SNS社交网站_APP软件开发_社交系统源码', driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
