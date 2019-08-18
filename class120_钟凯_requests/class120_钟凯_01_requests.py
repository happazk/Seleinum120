import unittest

import requests


class MyTestCase(unittest.TestCase):
    def test_login_sucess(self):
        log_url = 'http://192.168.102.149/Agileone/index.php/common/login'
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        data = "username=admin&password=admin&savelogin=true"
        response = requests.request("POST", log_url, data=data, headers=headers)
        res_text = response.text
        print(response)
        self.assertEqual('successful',res_text)
        print("登录成功")


if __name__ == '__main__':
    unittest.main()
