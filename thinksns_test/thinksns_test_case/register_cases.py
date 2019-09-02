import unittest

from random import choice
from time import time

from selenium import webdriver

from thinksns_test.thinksns_common.register_thinksns_page import register_thinksns


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.driver.maximize_window()
    def test_register_01(self):
        """
        function:正常注册
        :return:
        """
        driver = self.driver
        reg_email = str(time() * 1000)[:13] + '@qq.com'
        reg_password = "123456"
        count_second_name_list = ["艾", "安", "昂", "敖", "奥", "巴", "霸", "白", "柏", "拜", "班", "包", "保", "葆", "豹", "鲍", "暴",
                                  "卑", "贲", "毕", "闭", "秘", "边", "鞭", "彪", "别", "宾", "邴", "秉", "薄", "卜", "布", "部", "才",
                                  "蔡", "仓", "苍", "操", "曹", "策", "岑", "柴", "镡", "昌", "苌", "常", "昶", "畅", "唱", "晁", "巢",
                                  "朝", "车", "陈", "谌", "成", "承", "晟", "乘", "程", "池", "迟", "充", "种"]
        reg_username = "钟" + choice(count_second_name_list)
        register_thinksns(driver, reg_username=reg_username, reg_password=reg_password, reg_email=reg_email)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
