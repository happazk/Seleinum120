'''
Created on 2019年8月14日

@author: wangchaolin
'''
import requests

from teachers_demo.agileone_project.agileone.base.base_info import ADMIN_NAME,ADMIN_PASSWORD, HEADERS
from teachers_demo.agileone_project.agileone.base.interface_url import LOGIN_URL,NOTICE_QUERY_URL

def get_phpsessid_with_login():
    # 定义登录时所需的账号信息
    payload = f"username={ADMIN_NAME}&password={ADMIN_PASSWORD}&savelogin=true"
    # 模拟登录，并取得返回的头部信息
    response = requests.request("POST", LOGIN_URL, data=payload, headers=HEADERS)
    # 取得cookie信息
    cookie = response.headers["Set-Cookie"]
    # 切割cookie取得session的值
    phpsessid = cookie.split(";")[0]
    # 加入头部信息中
    HEADERS["Cookie"] = phpsessid

def get_last_notice_id():
    # 先登录，并取得session信息
    get_phpsessid_with_login()
    # 模拟查询公告，默认会返回第一页内容
    response = requests.request("POST", NOTICE_QUERY_URL, headers=HEADERS)
    # 解析返回的JSON数据
    last_notice_id = response.json()[0]["noticeid"]
    # 返回最后的公告id
    return int(last_notice_id)

if __name__ == "__main__":
    print(get_last_notice_id())
#     print(get_last_notice_id.__class__.__name__ == "function")