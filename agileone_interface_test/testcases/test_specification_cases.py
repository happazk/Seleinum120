import traceback
import unittest
from time import time

import requests

from agileone_interface_test.base.base_info import HEADERS
from agileone_interface_test.base.common_methond import get_cookie_with_login, exit_login
from agileone_interface_test.base.interface_url import ADD_SPECIFICATION_URL, DEL_SPECIFICATION_URL, QUERY_SPECIFICATION_URL, \
    EDIT_SPECIFICATION_URL
from agileone_interface_test.base.specification_operation import query_specification, query_specification_count, \
    add_specification
from agileone_interface_test.testdatas.specification_data import SPECIFICATION_ADD_DATA, SPECIFICATION_DEL_DATA, \
    SPECIFICATION_QUERY_DATA, SPECIFICATION_EDIT_DATA


class TestSpecificationInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 登录
        get_cookie_with_login()

    def test_add_specification(self):
        """
        function:增加规格用例测试集合
        :return:
        """
        # 获取测试数据
        test_fail_num = 0
        for data_list in SPECIFICATION_ADD_DATA:
            # 请求数据
            request_data = data_list[0]
            # 获取当前执行数据具体索引位置
            position = SPECIFICATION_ADD_DATA.index(data_list) + 1
            # 预期结果
            try:
                # 调用增加规格接口
                response = requests.request('POST', ADD_SPECIFICATION_URL, data=request_data, headers=HEADERS)

                if data_list[1].__class__.__name__ == "function":
                    # 如果是函数，则期望结果为函数查询出的结果
                    expect_result = str(data_list[1]())
                else:
                    # 如果是字符串，则期望结果为提示
                    expect_result = data_list[1]

                # 判决预期结果与实际结果
                # self.assertEqual(expect_result, response.text)
                self.assertIn(expect_result, response.text)

            except Exception as e:
                test_fail_num += 1
                print("第%s条用例错误\n 错误原因%s" % (str(position), str(traceback.format_exc())))
            finally:
                #恢复环境
                pass

        print("总共用例%s条，失败%s条" % (str(len(SPECIFICATION_ADD_DATA)), str(test_fail_num)))
        self.assertEqual(0, test_fail_num)

    def test_query_specification(self):
        """
        funciton:规格说明的查询测试用例
        :return:
        """
        # 获取测试数据
        test_fail_num = 0
        for data_list in SPECIFICATION_QUERY_DATA:
            # 请求数据
            request_data = data_list[0]
            # 获取当前执行数据具体索引位置
            position = SPECIFICATION_QUERY_DATA.index(data_list) + 1
            # 预期结果
            try:
                if data_list[1].__class__.__name__ == "function":
                    # 如果是函数，则期望结果为函数查询出的结果
                    expect_result = str(data_list[1]())
                else:
                    # 如果是字符串，则期望结果为提示
                    expect_result = data_list[1]

                # 调用查询规格接口
                response = requests.request('POST', QUERY_SPECIFICATION_URL, data=request_data, headers=HEADERS)

                # 判决预期结果与实际结果
                # self.assertEqual(expect_result, response.text)
                self.assertIn(expect_result, response.text)

            except Exception as e:
                test_fail_num += 1
                print("第%s条用例错误\n 错误原因%s" % (str(position), str(traceback.format_exc())))

        print("总共用例%s条，失败%s条" % (str(len(SPECIFICATION_QUERY_DATA)), str(test_fail_num)))
        self.assertEqual(0, test_fail_num)

    def test_del_specification(self):
        """
        funciton:进行规格的删除测试用例
        :return:
        """
        # 获取测试数据
        test_fail_num = 0
        for data_list in SPECIFICATION_DEL_DATA:
            # 请求数据
            request_data = data_list[0]
            # 获取当前执行数据具体索引位置
            position = SPECIFICATION_DEL_DATA.index(data_list) + 1
            # 预期结果
            try:

                if data_list[1].__class__.__name__ == "function":
                    # 如果是函数，则期望结果为函数查询出的结果
                    expect_result = str(data_list[1]())
                else:
                    # 如果是字符串，则期望结果为提示
                    expect_result = data_list[1]
                    # 根据期望结果判断是否需要新增一个规格，更新数据源，删除当前新增规格说明
                    if expect_result == '1':
                        data_dic = {
                            'userstoryid': '1',
                            'type': 'All-In-One',
                            'content': '钟凯'
                        }
                        request_data['specid'] = add_specification(data=data_dic)

                # 调用删除规格接口
                response = requests.request('POST', DEL_SPECIFICATION_URL, data=request_data, headers=HEADERS)

                # 判决预期结果与实际结果
                # self.assertEqual(expect_result, response.text)
                self.assertIn(expect_result, response.text)

            except Exception as e:
                test_fail_num += 1
                print("第%s条用例错误\n 错误原因%s" % (str(position), str(traceback.format_exc())))

        self.assertEqual(0, test_fail_num)

    def test_edit_specification(self):
        """
        funciton:进行规格的编辑测试用例
        :return:
        """
        # 获取测试数据
        test_fail_num = 0
        for data_list in SPECIFICATION_EDIT_DATA:
            # 请求数据
            request_data = data_list[0]
            # 获取当前执行数据具体索引位置
            position = SPECIFICATION_EDIT_DATA.index(data_list) + 1
            # 预期结果
            try:
                if data_list[1].__class__.__name__ == "function":
                    # 如果是函数，则期望结果为函数查询出的结果
                    expect_result = str(data_list[1]())
                else:
                    # 如果是字符串，则期望结果为提示
                    expect_result = data_list[1]
                    # 根据期望结果判断是否需要新增一个规格，更新数据源，删除当前新增规格说明
                    if expect_result == '1':
                        data_dic = {
                            'userstoryid': '1',
                            'type': 'All-In-One',
                            'content': '钟凯'
                        }
                        request_data['specid'] = add_specification(data=data_dic)

                # 调用增加规格接口
                response = requests.request('POST', EDIT_SPECIFICATION_URL, data=request_data, headers=HEADERS)

                # 判决预期结果与实际结果
                # self.assertEqual(expect_result, response.text)
                self.assertIn(expect_result, response.text)

            except Exception as e:
                test_fail_num += 1
                print("第%s条用例错误\n 错误原因%s" % (str(position), str(traceback.format_exc())))

        print("总共用例%s条，失败%s条" % (str(len(SPECIFICATION_EDIT_DATA)), str(test_fail_num)))
        self.assertEqual(0, test_fail_num)
        print("")

    # PHPSESSID为空，错误，不传
    def test_cookie_with_specification_01(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # 退出登录
        exit_login()


if __name__ == '__main__':
    unittest.main()
