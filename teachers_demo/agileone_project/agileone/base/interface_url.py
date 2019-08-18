'''
Created on 2019年8月14日

@author: wangchaolin
'''

from teachers_demo.agileone_project.agileone.base.base_info import IP

# 登录接口的地址
LOGIN_URL = IP+"/agileone/index.php/common/login"

# 查询公告接口的地址
NOTICE_QUERY_URL = IP + "/agileone/index.php/notice/query"
# 新增公告接口的地址
NOTICE_ADD_URL = IP + "/agileone/index.php/notice/add"