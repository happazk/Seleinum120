import unittest
from time import sleep

from selenium import webdriver

#添加商品
from ecshop_test.ecshop_common.ecshop_backstage_index_page import get_add_new_item
from ecshop_test.ecshop_common.ecshop_backstage_page import loggin_back


class AddNewItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)
        self.driver.maximize_window()

    def test01(self):
        driver = self.driver
        #登录后台管理
        loggin_back(driver=driver)
        #进入添加新商品界面
        get_add_new_item(driver)


        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
