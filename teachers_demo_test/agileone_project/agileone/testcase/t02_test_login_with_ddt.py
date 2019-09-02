'''
Created on 2019年8月14日

@author: wangchaolin
'''
import unittest, requests, traceback

from teachers_demo_test.agileone_project.agileone.base.base_info import HEADERS
from teachers_demo_test.agileone_project.agileone.base.interface_url import LOGIN_URL
from teachers_demo_test.agileone_project.agileone.testdata.test_login_data import TEST_LOGIN_DATA_LIST

class TestLoginWithDDT(unittest.TestCase):

    def test_01(self):
        # 定义变量用来存失败的用例数
        failed_num = 0
        # 取得测试数据列表，并循环进行测试
        for data_list in TEST_LOGIN_DATA_LIST:
            # 得到用例的位置
            pos = TEST_LOGIN_DATA_LIST.index(data_list)+1
            try:
                # 模拟进行发包，并取得返回值
                response = requests.request("POST", LOGIN_URL, data=data_list[0], headers=HEADERS)
                # 判断测试结果
                self.assertEqual(data_list[1], response.text)
            except Exception as e:
                # 失败用例数+1
                failed_num+=1
                # 打印报错信息
#                 print(f"第{pos}条用例执行失败，失败原因为：{str(e)}")
                print(f"第{pos}条用例执行失败，失败原因为：\n{traceback.format_exc()}")
        # 判断最终执行情况
        self.assertEqual(0, failed_num)

