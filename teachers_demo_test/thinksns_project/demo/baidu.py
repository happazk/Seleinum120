from selenium import webdriver
import unittest
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
    
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("51testing")
        driver.find_element_by_id("su").click()
        sleep(3)
        self.assertEqual("51testing_百度搜索", driver.title)
    
    def tearDown(self):
        self.driver.quit()
