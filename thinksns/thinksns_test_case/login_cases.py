import unittest

from selenium import webdriver

from thinksns.thinksns_common.login_thinksns_page import THINKSNS_BASE_URL, login_thinksns


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.driver.maximize_window()
        self.base_url = THINKSNS_BASE_URL

    def test_login_01(self):
        """
        function:成功登录
        :return:
        """
        driver = self.driver
        #准备数据源
        username = ''
        password = ''
        login_thinksns(driver,)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
