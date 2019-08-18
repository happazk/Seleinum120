import unittest
from time import sleep, time

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.driver.maximize_window()
        self.base_url = 'http://192.168.102.149/Agileone/index.php'

    def test_commite(self):
        driver = self.driver
        driver.get(self.base_url)


        #填写用户名
        driver.find_element_by_class_name("login-username").send_keys("admin")
        #填写密码
        driver.find_element_by_class_name("login-password").send_keys("admin")
        #点击登录
        driver.find_element_by_class_name("loginbt").click()
        sleep(1)
        #新增会议
        time_res = str(int(time()))
        div_element = driver.find_element_by_class_name("left-menu")
        div_element.find_element_by_link_text("※ 会议记录 ※").click()
        #
        driver.find_element_by_id("minutesid").send_keys("编号"+time_res)
        #举行时间
        pass
        #主持人
        driver.find_element_by_id("organizer").send_keys("主持人"+time_res)
        #会议地点
        driver.find_element_by_id("venue").send_keys("上海"+time_res)
        #主题
        driver.find_element_by_id("topic").send_keys("51testing"+time_res)
        #与会人员
        driver.find_element_by_id("attendee").send_keys("钟凯"+time_res)
        #写入文本内天
        # iframe_element = driver.find_element_by_class_name("ke-iframe")
        # driver.switch_to_frame(iframe_element)
        # sleep(3)
        # driver.find_element_by_tag_name("body").send_keys("添加内容"+time_res)
        # driver.switch_to_default_content()  # 回到默认界面
        # sleep(2)
        #点击新增
        driver.find_element_by_xpath("//span[@id='actionButton']/input[@id='add']").click()
        sleep(1)

        #检查会议是否正确显示
        tbody_element = driver.find_element_by_id("dataPanel")
        tr_elemnt = tbody_element.find_elements_by_tag_name("tr")[0]
        td_elements = tr_elemnt.find_elements_by_tag_name("td")
        #检查会议标题
        self.assertEqual("51testing"+time_res,td_elements[2].text)
        #检查会议地点
        self.assertEqual("上海"+time_res,td_elements[3].text)
        #检查主持人
        self.assertEqual("主持人"+time_res,td_elements[4].text)

        #点击编辑
        td_elements[-1].find_elements_by_tag_name("label")[0].click()
        # driver.find_element_by_id("organizer").clear()
        driver.find_element_by_id("organizer").send_keys("变更主持人"+time_res)
        sleep(1)

        #判断主持人内容是否biang
        driver.find_element_by_xpath("//span[@id='actionButton']/input[@id='edit']").click()
        tbody_element = driver.find_element_by_id("dataPanel")
        tr_elemnt = tbody_element.find_elements_by_tag_name("tr")[0]
        td_elements = tr_elemnt.find_elements_by_tag_name("td")
        self.assertEqual("主持人"+time_res+"变更主持人"+time_res,td_elements[4].text)

        #点击删除
        td_elements[-1].find_elements_by_tag_name("label")[1].click()
        driver.switch_to_alert().accept()
        tishi = driver.find_element_by_class_name("message").text
        self.assertNotEqual("成功啦:删除数据成功",tishi)
        sleep(1)










    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
