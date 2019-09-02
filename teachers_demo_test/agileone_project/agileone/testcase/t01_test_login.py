'''
Created on 2019年8月14日

@author: wangchaolin
'''
import unittest, requests

class TestLogin(unittest.TestCase):

    def setUp(self):
        # 定义被测接口地址和头部信息
        self.url = "http://172.31.18.130/agileone/index.php/common/login"
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

    def test_01(self):
        # 定义测试数据
        payload = "username=admin&password=admin&savelogin=true"
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", self.url, data=payload, headers=self.headers)
        # 判断测试结果
        self.assertEqual("successful", response.text)
    
    def test_02(self):
        # 定义测试数据
        payload = "username=&password=admin&savelogin=true"
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", self.url, data=payload, headers=self.headers)
        # 判断测试结果
        self.assertEqual("用户名或密码错误", response.text)

    def test_03(self):
        # 定义测试数据
        payload = "username=xxxx&password=admin&savelogin=true"
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", self.url, data=payload, headers=self.headers)
        # 判断测试结果
        self.assertEqual("用户名或密码错误", response.text)
    
    # 以此类推，将所有的接口测试用例转换为上述用例

