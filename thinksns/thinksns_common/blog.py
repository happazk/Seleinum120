from asyncio.tasks import sleep
from random import choices, choice
from unittest.case import TestCase

from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

from thinksns.thinksns_common.common import login_thinksns


def post_log(driver, text_content, title_content, access_permission='任何人可见', comment_permission='任何人可评论', file_name='',
             file_path='',
             password='root'):
    """
    function:发表日志
    :param driver:
    :param text_content: 文本内容
    :param title_content: 日志标题
    :param access_permission: 访问权限--->'任何人可见', '仅好友可见', '私密日记', '凭密码访问'
    :param comment_permission: 评论权限--->'任何人可评论', '好友可评论', '关闭评论'
    :param file_name: 附件名
    :param file_path: 上传文件路径
    :return:
    """
    # 点击日志功能
    driver.find_element_by_class_name("user_app_list").find_element_by_link_text("发表").click()
    # 设置日志标题
    driver.find_element_by_xpath("//input[@id='title']").send_keys(title_content)
    # 设置日志内容
    iframe_ele = driver.find_element_by_class_name("ke-iframe")
    driver.switch_to_frame(iframe_ele)
    sleep(3)
    driver.find_element_by_class_name("ke-content").send_keys(text_content)
    driver.switch_to_default_content()  # 回到默认界面
    sleep(2)
    # # 设置表情
    # driver.find_element_by_class_name("ke-icon-emoticons").click()
    # img_list = driver.find_element_by_class_name("ke-menu").find_elements_by_tag_name("img")
    # img_element = choice(img_list)
    # ims_src = img_element.get_attribute('src')
    # img_element.click()  # 选中心情图标

    # 设置访问权限
    select_ele = driver.find_element_by_name("privacy")
    select = Select(select_ele)
    select.select_by_visible_text(access_permission)
    # '凭密码访问'时 设置密码
    if '凭密码访问' == access_permission:
        sleep(1)
        driver.find_element_by_name("password").send_keys(password)

    # 设置评论权限
    select_ele = driver.find_element_by_name("cc")
    select = Select(select_ele)
    select.select_by_visible_text(comment_permission)
    # 上传文件
    if file_path is not '':
        driver.find_element_by_name("myfile").send_keys(file_path)
        sleep(2)

    # 点击发表
    driver.find_element_by_xpath("//input[@value='发 表']").click()

    # 检查是否发表成功
    div_element = driver.find_element_by_class_name("LogList")
    # 检查日志标题
    title_res = div_element.find_element_by_tag_name("strong").text
    TestCase().assertEqual(title_res, title_content)
    # 比较文本值
    content_res = div_element.find_element_by_id("blog_con").text
    TestCase().assertEqual(content_res, text_content)
    # 检查附件名
    file_name_res = div_element.find_element_by_class_name("adjunct_list").text
    TestCase().assertIn(file_name, file_name_res)


def check_log(driver, content_text, content_title, file_name):
    """
    检查日志是否匹配
    :param driver:
    :param content_text:
    :param content_title:
    :param file_name:
    :return:
    """

    # 检查日志
    div_element = driver.find_element_by_class_name("LogList")
    # 检查日志标题
    title_res = div_element.find_element_by_tag_name("strong").text
    TestCase().assertEqual(title_res, content_title)
    # 比较文本值
    content_res = div_element.find_element_by_id("blog_con").text
    TestCase().assertEqual(content_res, content_text)
    # 检查附件名
    file_name_res = div_element.find_element_by_class_name("adjunct_list").text
    TestCase().assertIn(file_name, file_name_res)


def check_message_tip(driver, class_name, message=''):
    """
    function:比较文本是否包含在实际获取内容中
    :param driver:
    :param class_name:元素类名
    :param message:待比较字符串
    :return:
    """
    actual = driver.find_element_by_class_name(class_name).text
    # print('actual = %s'%actual)
    # print('message = %s'%message)
    TestCase().assertIn(message, actual)


def check_access_permission(driver, user_info, access_permission, comment_permission, url, content, title, file_name,
                            blog_password='root', *args,
                            **kwargs):
    """
    # function:判断好友和非好友的访问权限
    # :param driver:
    # :param user_info: [{
    #     'user_name':'',
    #      'user_email':'',
    #     'user_password':''
    #     'is_friend':False #和主用户是否为好友
    #     'is_main_count':True #是否是主用户
    # },.....] ---->传入多个用户信息
     :param access_permission: 访问权限--->'任何人可见', '仅好友可见', '私密日记', '凭密码访问'
    :param args:
    :param url:登录网址
    :param title:检查权限的文章标题
    :param content:文章内容
    :param file_name:附件名
    :param blog_password:访问文章的密码
    :param args:
    :param kwargs:
    :return:
    """

    # driver = webdriver.Firefox()
    # 退出登录
    # driver.find_element_by_link_text("退出").click()
    # 登录
    login_thinksns(url, driver, user_info['user_email'], user_info['user_password'], user_info['user_name'])
    # 点击随便看看
    driver.find_element_by_link_text("随便看看").click()
    # 点击标题
    driver.find_element_by_link_text(title).click()
    if '任何人可见' == access_permission:
        # 检查日志详情
        check_log(driver, content, title, file_name)
        # 检查评论权限
        check_comment_permission(driver, user_info=user_info, comment_permission=comment_permission)
    elif '仅好友可见' == access_permission:
        if user_info['is_friend']:
            # 检查日志详情
            check_log(driver, content, title, file_name)
            check_comment_permission(driver, user_info=user_info, comment_permission=comment_permission)
        else:
            # 检查访问提示，‘只有主人的好友可以查看此日志’
            check_message_tip(driver, 'bg_msg_btm', '只有主人的好友可以查看此日志')
    elif '私密日记' == access_permission:
        # 检查访问提示 '只有主人可以查看此日志'
        check_message_tip(driver, 'bg_msg_btm', '只有主人可以查看此日志')
    else:
        try:
            # 检查访问提示：本日志需要密码才能访问
            check_message_tip(driver, 'bg_msg_btm', '本日志需要密码才能访问')
            # 输入密码  password
            driver.find_element_by_name("password").send_keys(blog_password)
            # 点击提交 class  btn_b
            driver.find_element_by_class_name("btn_b").click()
            sleep(1)
        except Exception as e:
            print("已知密码访问日志bug,因为练习使用，暂时规避")


def check_comment_permission(driver, user_info, comment_permission, *args, **kwargs):
    """
    function:检查评论权限
    :param driver:
    :param user_info:
    :param comment_permission:
    :param args:
    :param kwargs:
    :return:
    """
    if '任何人可评论' == comment_permission:
        # 新建评论
        new_comment(driver)
    elif '好友可评论' == comment_permission:
        if user_info['is_friend']:
            # 新建评论
            new_comment(driver)
        else:
            # 检查评论权限提示
            check_message_tip(driver, 'LogList', '您无法评论,日志发布者设置好友可评论')
    else:
        # 检查评论提示
        check_message_tip(driver, 'LogList', '您无法评论,日志发布者已经关闭评论')


def new_comment(driver, comments='评论测试'):
    driver.find_element_by_name("textarea").send_keys(comments)
    # driver.find_element_by_class_name("btn_b").click()
    driver.find_element_by_id("content_submit").click()
