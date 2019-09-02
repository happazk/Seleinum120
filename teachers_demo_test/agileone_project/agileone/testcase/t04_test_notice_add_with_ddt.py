'''
Created on 2019年8月14日

@author: wangchaolin
'''
import unittest, requests, traceback
from time import time

from teachers_demo_test.agileone_project.agileone.base.base_info import HEADERS
from teachers_demo_test.agileone_project.agileone.base.common_method import get_last_notice_id
from teachers_demo_test.agileone_project.agileone.base.interface_url import NOTICE_ADD_URL
from teachers_demo_test.agileone_project.agileone.testdata.test_notice_add_data import TEST_NOTICE_ADD_DATA_LIST


class TestNoticeAddWithDDT(unittest.TestCase):

    def test_01(self):
        # 定义变量用来存失败的用例数
        failed_num = 0
        # 取得测试数据列表，并循环进行测试
        for data_list in TEST_NOTICE_ADD_DATA_LIST:
            # 得到用例的位置
            pos = TEST_NOTICE_ADD_DATA_LIST.index(data_list)+1
            try:
                # 判断期望结果类型是函数还是字符串
                if data_list[1].__class__.__name__ == "function":
                    # 如果是函数，则期望结果为函数查询出的结果+1
                    expect_result = str(data_list[1]()+1)
                else:
                    # 如果是字符串，则期望结果为提示
                    expect_result = data_list[1]
                # 模拟进行发包，并取得返回值
                response = requests.request("POST", NOTICE_ADD_URL, data=data_list[0], headers=HEADERS)
                # 判断测试结果
                self.assertEqual(expect_result, response.text)
            except Exception as e:
                # 失败用例数+1
                failed_num+=1
                # 打印报错信息
#                 print(f"第{pos}条用例执行失败，失败原因为：{str(e)}")
                print(f"第{pos}条用例执行失败，失败原因为：\n{traceback.format_exc()}")
        # 判断最终执行情况
        self.assertEqual(0, failed_num)
    
    # PHPSESSID为空
    def test_02(self):
        # 定义测试数据
        data = {
            "headline":"公告标题"+str(time()),
            "content":"公告内容"+str(time()),
            "scope":"1",
            "expireddate":"2019-09-14",
            }
        # 取得最后的公告id
        HEADERS["Cookie"] = "PHPSESSID="
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", NOTICE_ADD_URL, data=data, headers=HEADERS)
        # 判断测试结果
        self.assertEqual("no_permission", response.text)
    
    # PHPSESSID为错误的
    def test_03(self):
        # 定义测试数据
        data = {
            "headline":"公告标题"+str(time()),
            "content":"公告内容"+str(time()),
            "scope":"1",
            "expireddate":"2019-09-14",
            }
        # 取得最后的公告id
        HEADERS["Cookie"] = "PHPSESSID=80448e3c2b6ea94584ebb78c00000000"
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", NOTICE_ADD_URL, data=data, headers=HEADERS)
        # 判断测试结果
        self.assertEqual("no_permission", response.text)
        
    # 不传PHPSESSID
    def test_04(self):
        # 定义测试数据
        data = {
            "headline":"公告标题"+str(time()),
            "content":"公告内容"+str(time()),
            "scope":"1",
            "expireddate":"2019-09-14",
            }
        # 取得最后的公告id
        HEADERS["Cookie"] = ""
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", NOTICE_ADD_URL, data=data, headers=HEADERS)
        # 判断测试结果
        self.assertEqual("no_permission", response.text)