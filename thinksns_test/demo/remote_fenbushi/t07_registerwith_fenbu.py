
#分布式执行demo
import unittest
from selenium import webdriver
from time import time
from random import choice

from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from thinksns_test.thinksns_common.common import register_thinksns
from thinksns_test.thinksns_common.mysql_operation import get_verfied_code


class TestRegisterVerifyCode(unittest.TestCase):
    def setUp(self):
        # 初始化浏览器对象
        #选择执行用例的分布节点，注意:1、选择主节点 将由主节点随机分配给任意子节点执行
        #2、也可以自己选择子节点执行
        #desired_capabilities 选择浏览器
        self.driver = WebDriver(command_executor='http://172.31.20.86:4444/wd/hub',
                 desired_capabilities=desired_capabilities.DesiredCapabilities.CHROME)

        self.base_url = 'http://192.168.102.151/ThinkSNS/'
        # self.base_url = 'http://172.31.31.100:8200'  # 访问网址
        # 设置元素识别超时时间
        self.driver.implicitly_wait(15)
        # 设置页面加载时间
        self.driver.set_page_load_timeout(30)

        # 设置异步脚本加载时间
        self.driver.set_script_timeout(30)
        # 窗口最大化
        self.driver.maximize_window()

    def test_register_verifycode(self):
        # 打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 识别元素，操作元素
        # 0、定义测试数据
        count_email = str(time() * 1000)[:13] + '@qq.com'
        count_password = "123456"
        count_second_name_list = ["艾", "安", "昂", "敖", "奥", "巴", "霸", "白", "柏", "拜", "班", "包", "保", "葆", "豹", "鲍", "暴",
                                  "卑", "贲", "毕", "闭", "秘", "边", "鞭", "彪", "别", "宾", "邴", "秉", "薄", "卜", "布", "部", "才",
                                  "蔡", "仓", "苍", "操", "曹", "策", "岑", "柴", "镡", "昌", "苌", "常", "昶", "畅", "唱", "晁", "巢",
                                  "朝", "车", "陈", "谌", "成", "承", "晟", "乘", "程", "池", "迟", "充", "种"]
        count_name = "钟" + choice(count_second_name_list)
        # register_thinksns(self.driver,count_email,count_password,count_name)

        # 1、点击注册跳转页面
        driver.find_element_by_link_text("注册").click()
        # 2、注册界面内容填入
        driver.find_element_by_name("email").send_keys(count_email)
        driver.find_element_by_name("passwd").send_keys(count_password)  # password
        driver.find_element_by_name("repasswd").send_keys(count_password)  # 确认密码
        driver.find_element_by_name("name").send_keys(count_name)  # 姓名
        driver.find_element_by_xpath("//input[@name='sex' and  @value='1']").click()  # 性别

        # # 地区选择
        # driver.find_element_by_class_name("btn_b").click()
        # driver.find_element_by_link_text("四川").click()
        # driver.find_element_by_link_text("成都市").click()
        # driver.find_element_by_name("input").click()  # 提交

        #地区选择通过Js调用方法，以及处理弹窗
        driver.find_element_by_class_name("btn_b").click()
        driver.execute_script("save()")

        #判断警告框提示是否正确
        actual_tip = driver.switch_to_alert().text
        self.assertEqual("请选择地区",actual_tip)
        driver.switch_to_alert().accept()

        driver.execute_script('selectarea("2299","1","四川")')
        driver.execute_script('selectarea("2424","2","达州市")')
        driver.execute_script('save()')


        # 隐私设置,直接方式
        # driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
        select_ele = driver.find_element_by_name('baseinfoprivacy')
        sel = Select(select_ele)
        sel.select_by_value('0')
        #获取session,从后台获取验证码填入前台
        session = driver.get_cookie("PHPSESSID")['value']
        ver_code = get_verfied_code(session)
        # driver.find_element_by_class_name("verify").send_keys(ver_code)
        driver.find_element_by_xpath('//form[@id="regform"]/ul[3]/li[1]/div[2]/input').send_keys(ver_code)


        # 点击同意注册
        driver.find_element_by_name("button").click()
        # 页面跳转判断
        res_text = driver.find_element_by_xpath("//div[@class='message_box']/p[1]").text
        self.assertEqual("注册成功!", res_text)

        # 查看注册后的页面信息是否正确
        driver.find_element_by_link_text('资料')
        driver.find_element_by_xpath("//div[@class='nav_sub']/a[contains(text(),'资料')]").click()
        count_name_res = driver.find_element_by_xpath("//input[@name='name']").get_attribute('value')
        self.assertEqual(count_name, count_name_res)




    def tearDown(self):
        # 退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
