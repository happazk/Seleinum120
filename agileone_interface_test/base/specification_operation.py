import requests

from agileone_interface_test.base.base_info import HEADERS
from agileone_interface_test.base.common_methond import get_cookie_with_login
from agileone_interface_test.base.interface_url import QUERY_SPECIFICATION_URL, ADD_SPECIFICATION_URL


def add_specification(data=None):
    """
    function:添加一条规格说明
    :param:data = {
        'userstoryid':故事id
        'type':类型
        'content':内容
    }
    :return:返回编号 字符串形式
    """

    # get_cookie_with_login()
    response = None
    if data == None:
        return
    response = requests.request('POST', ADD_SPECIFICATION_URL, data=data, headers=HEADERS)
    return str(response.text)


def edit_specification():
    """
    function:编辑规格说明
    :return:
    """
    pass


def del_specification():
    """
    删除规格说明
    :return:
    """
    pass


def query_specification(data):
    """
    查询规格说明
    :return:
    """
    # get_cookie_with_login()
    response = requests.request('POST', QUERY_SPECIFICATION_URL, data=data, headers=HEADERS)
    return response.json()


def query_specification_count():
    """
    function:查询当前规格数
    :return:规格数量
    """
    # get_cookie_with_login()
    response = requests.request('POST', QUERY_SPECIFICATION_URL, headers=HEADERS)
    response_dic = response.json()[-1]

    return int(response_dic['totalRecord'])

def get_current_specification_numbers():
    """
    function:返回当前最新的规格说明编号
    :return:
    """
    # get_cookie_with_login()
    response = requests.request('POST', QUERY_SPECIFICATION_URL, headers=HEADERS)
    response_dic = response.json()
    specid = int(response_dic[0]['specid'])
    return specid



if __name__ == "__main__":
    # print(query_specification_count())
    # data_dic = {
    #     'userstoryid':'1',
    #     'type':'All-In-One',
    #     'content':'钟凯'
    # }
    # add_specification(data_dic)
    get_current_specification_numbers()
