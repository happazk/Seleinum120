import os
from random import choice, randint
import unittest

from time import sleep, time

from selenium import webdriver

# from thinksns_test.thinksns_common.login import login_thinksns
from thinksns_test.thinksns_common import login_thinksns
from thinksns_test.thinksns_common.blog import post_log, check_access_permission
from thinksns_test.thinksns_common.common import exit_thinksns


class TestPublishBlog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)  # 页面元素识别时间15s
        self.driver.set_script_timeout(30)  # 异步脚本等待时间30s
        self.driver.set_page_load_timeout(30)  # 页面加载时间30s
        self.driver.maximize_window()  # 窗口最大化
        self.base_url = 'http://192.168.102.151/ThinkSNS/'  # 访问网址
        # self.base_url = 'http://172.31.31.100:8200'  # 访问网址

    def test_log_permission(self):
        """
        function:测试日志访问权限和评论权限
        :return:
        """
        driver = self.driver

        # 定义数据
        email_a = 'class120_A@qq.com'
        name_a = '钟凯A'
        password_a = '123456'
        email_b = 'class120_B@qq.com'
        name_b = '钟凯B'
        password_b = '123456'
        email_c = 'class120_C@qq.com'
        name_c = '林灿烂A'
        password_c = '123456'

        # 定义访问权限和评论权限的列表
        privacy_list = ['任何人可见', '仅好友可见', '私密日记', '凭密码访问']
        cc_list = ['任何人可评论', '好友可评论', '关闭评论']
        # 初始用户值
        user_infos = [
            {
                'user_name': name_a,
                'user_email': email_a,
                'user_password': password_a,
                'is_friend': True,
                'is_main_count': True,
            },
            {
                'user_name': name_b,
                'user_email': email_b,
                'user_password': password_b,
                'is_friend': True,
                'is_main_count': False,
            },
            {
                'user_name': name_c,
                'user_email': email_c,
                'user_password': password_c,
                'is_friend': False,
                'is_main_count': False,
            }]
        for privacy in privacy_list:
            for cc in cc_list:
                login_thinksns(self.base_url, driver, email_a, password_a, name_a)
                # 发表日志
                text_content = str(time())[:12]
                title_content = '%s:%s:%s' % (privacy, cc, text_content)
                num = str(randint(0, 8))
                file_path = os.path.dirname(os.getcwd()) + '\\imgs\\blog_imgs\\' + num + '.jpg'
                file_name = num + '.jpg'
                post_log(driver, text_content, title_content, privacy, cc, file_name, file_path)
                # 退出登录
                exit_thinksns(driver)
                # 其他用户登录访问评论权限判断
                #好友用户
                check_access_permission(driver, user_infos[1], privacy, cc, self.base_url, content=text_content,
                                        title=title_content, file_name=file_name)
                exit_thinksns(driver)
                #非好友用户
                check_access_permission(driver, user_infos[2], privacy, cc, self.base_url, content=text_content,
                                        title=title_content, file_name=file_name)
                exit_thinksns(driver)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
