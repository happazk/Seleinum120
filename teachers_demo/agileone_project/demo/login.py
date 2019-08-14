'''
Created on 2019年8月14日

@author: wangchaolin
'''
import requests

url = "http://172.31.18.130/agileone/index.php/common/login"

payload = "username=admin&password=admin&savelogin=true"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "29c517f5-dc2b-4d40-a44a-46b82cf6e97e"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(f"响应的对象：{response}")
print(f"响应对象的类型为：{type(response)}") # <class 'requests.models.Response'>
print(f"响应的状态码：{response.status_code}")
print(f"响应状态码对应提示内容：{response.reason}")
print(f"响应的头部信息：{response.headers}")
print(f"响应数据的原始格式（HTTPResponse object）：{response.raw}")
print(f"请求的地址：{response.url}") 
print(f"响应内容的编码格式：{response.encoding}")
print(f"响应的Cookie缓存信息：{response.cookies}")
print(f"响应处理消耗的时间：{response.elapsed}")
print(f"响应的文本内容：{response.text}")
print(f"响应的字节码格式的内容：{response.content}")
print(f"返回json格式的数据：{response.json()}")