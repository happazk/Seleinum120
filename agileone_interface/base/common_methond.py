import requests

from agileone_interface.base.base_info import HEADERS, ADMIN_NAME, ADMIN_PASSWORD
from agileone_interface.base.interface_url import LOGIN_URL, LOGOUT_URL


def get_cookie_with_login():
    """
    funtion:登录并且保持cookie
    :return:
    """

    data = {
        'username': ADMIN_NAME,
        'password': ADMIN_PASSWORD,
        'savelogin': 'true'
    }
    response = requests.request("POST", LOGIN_URL, data=data, headers=HEADERS)
    phsession = ((response.headers['Set-Cookie']).split(";"))[0]
    HEADERS["Cookie"]=phsession


def exit_login():
    """
    function:退出登录，并取消cookie的保存
    :return:
    """
    try:
        requests.request('POST',LOGOUT_URL,headers=HEADERS)
        HEADERS["Cookie"]=''
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_cookie_with_login()

