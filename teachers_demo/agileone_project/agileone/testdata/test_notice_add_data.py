'''
Created on 2019年8月14日

@author: wangchaolin
'''
from time import time
from agileone.base.common_method import get_last_notice_id

TEST_NOTICE_ADD_DATA_LIST = [
    [{"headline":"公告标题"+str(time()),"content":"公告内容"+str(time()),"scope":"1","expireddate":"2019-09-14",},get_last_notice_id],
    [{"headline":"","content":"公告内容"+str(time()),"scope":"1","expireddate":"2019-09-14",},"公告标题不能为空"],
    [{"content":"公告内容"+str(time()),"scope":"1","expireddate":"2019-09-14",},"缺少必填参数：公告标题"],    
    ]
