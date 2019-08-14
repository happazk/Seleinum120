'''
Created on 2019年8月14日

@author: wangchaolin
'''

TEST_LOGIN_DATA_LIST = [
    ["username=admin&password=admin&savelogin=true","successful"],
    ["username=&password=admin&savelogin=true","用户名或密码错误"],
    ["username=xxxx&password=admin&savelogin=true","用户名或密码错误"],
    ["password=admin&savelogin=true","缺少必填参数：用户名"],
    ["username=admin&password=&savelogin=true","用户名或密码错误"],
    ["username=admin&password=123456&savelogin=true","用户名或密码错误"],
    ["username=admin&savelogin=true","用户名或密码错误"],
    ["username=admin&password=admin&savelogin=false","successful"],
    ["username=admin&password=admin&savelogin=xxx","successful"],
    ["username=admin&password=admin&savelogin=","successful"],
    ["username=admin&password=admin","successful"],
    ["savelogin=true","缺少必填参数：用户名、密码"],
    ]
