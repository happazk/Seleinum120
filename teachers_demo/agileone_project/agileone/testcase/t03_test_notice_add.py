'''
Created on 2019年8月14日

@author: wangchaolin
'''
import unittest, requests
from agileone.base.interface_url import NOTICE_ADD_URL
from agileone.base.base_info import HEADERS
from time import time
from agileone.base.common_method import get_last_notice_id

class TestNoticeAdd(unittest.TestCase):

    def test_01(self):
        # 定义测试数据
        data = {
            "headline":"公告标题"+str(time()),
            "content":"公告内容"+str(time()),
            "scope":"1",
            "expireddate":"2019-09-14",
            }
        # 取得最后的公告id
        last_notice_id = get_last_notice_id()
        # 模拟进行发包，并取得返回值
        response = requests.request("POST", NOTICE_ADD_URL, data=data, headers=HEADERS)
        # 判断测试结果
        self.assertEqual(last_notice_id+1, int(response.text))
    