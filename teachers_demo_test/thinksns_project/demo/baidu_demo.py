from selenium import webdriver
from unittest.case import TestCase
from time import sleep

# 第一步：初始化相关参数
driver = webdriver.Chrome()
base_url = "https://www.baidu.com/"
# 第二步：打开被测网站
driver.get(base_url)
# 第三步：执行测试动作
driver.find_element_by_id("kw").send_keys("51testing")
driver.find_element_by_id("su").click()
sleep(3)
# 第四步：判断测试结果
# tc = TestCase()
# tc.assertEqual("51testing_百度搜索", driver.title, "期望的标题不是 51testing_百度搜索")
# TestCase.assertEqual(TestCase(), "51testing_百度搜索", driver.title, "期望的标题不是 51testing_百度搜索")
TestCase().assertEqual("51testing_百度搜索", driver.title, "期望的标题不是 51testing_百度搜索")
# 第五步：释放资源
driver.quit()