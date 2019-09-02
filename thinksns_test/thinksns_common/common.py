from random import choice
from time import sleep
from unittest import TestCase

from selenium.webdriver.support.select import Select


def login_thinksns(url,driver, email, password, name):
    """
    function:thinksns前台界面用户登录，不包含验证码功能
    :param driver:
    :param email:
    :param password:
    :param name:
    :return:
    """
    # 1、点击注册跳转页面
    driver.get(url)
    driver.find_element_by_link_text("登陆").click()
    # 2、注册界面内容填入
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("passwd").send_keys(password)
    driver.find_element_by_class_name("btn_b").click()
    TestCase().assertEqual('SNS社区', driver.title)

def exit_thinksns(driver):
    """
    function:退出thinksns
    :param driver:
    :return: None
    """
    driver.find_element_by_link_text("退出").click()

def register_thinksns(driver, reg_email, reg_password, reg_name, \
                      set_privacy='0', set_sex='1', province='四川', city='成都市'):
    """
    function:thinksns注册新用户功能，不包含验证码登录
    :param driver:浏览器驱动
    :param reg_email:注册邮箱
    :param reg_password:注册密码
    :param reg_name:注册用户名
    :param set_privacy:隐私设置
            '0':任何人能看见我的资料和内容
            '1':仅好友能看见我的资料和内容
            '2':隐藏我的资料和内容
    :param set_sex:性别设置 ，'1' 为男   '2'为女
    :param province:省份设置
    :param city:市设置
    :return:没有返回值
    """
    # 1、点击注册跳转页面
    driver.find_element_by_link_text("注册").click()
    # 2、注册界面内容填入
    driver.find_element_by_name("email").send_keys(reg_email)
    driver.find_element_by_name("passwd").send_keys(reg_password)  # password
    driver.find_element_by_name("repasswd").send_keys(reg_password)  # 确认密码
    driver.find_element_by_name("name").send_keys(reg_name)  # 姓名
    xpath = "//input[@name='sex' and  @value=%s]" % set_sex
    driver.find_element_by_xpath(xpath).click()  # 性别

    # 地区选择
    driver.find_element_by_class_name("btn_b").click()
    driver.find_element_by_link_text(province).click()
    driver.find_element_by_link_text(city).click()
    driver.find_element_by_name("input").click()  # 提交

    # 隐私设置,直接方式
    # driver.find_element_by_xpath("//select[@name='baseinfoprivacy']/option[@value='0']").click()
    select_ele = driver.find_element_by_name('baseinfoprivacy')
    sel = Select(select_ele)
    sel.select_by_value(set_privacy)

    # 点击同意注册
    driver.find_element_by_name("button").click()
    # 页面跳转判断
    res_text = driver.find_element_by_xpath("//div[@class='message_box']/p[1]").text
    TestCase().assertEqual("注册成功!", res_text)

    # 查看注册后的页面信息是否正确
    driver.find_element_by_link_text('资料')
    driver.find_element_by_xpath("//div[@class='nav_sub']/a[contains(text(),'资料')]").click()
    count_name_res = driver.find_element_by_xpath("//input[@name='name']").get_attribute('value')
    TestCase().assertEqual(reg_name, count_name_res)


def post_mood(driver,set_mood,mode=0 ):
    """
    function:发布心情
    :param mode: 0,在首页界面发布心情
                  1,在心情界面
    :return:
    """
    if mode == 0:
        pass
    elif mode == 1:
        # 点击左侧心情元素
        # driver.find_element_by_xpath("//div[@class='user_app_list']/ul/li/a[contains(text(),'心情')]").click()
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("心情").click()
        # 查找心情发布框元素
        textarea_ele = driver.find_element_by_id("mini-coment")
        textarea_ele.click()
        textarea_ele.send_keys(set_mood)  # 输入文本心情

        # 查找所有图标心情元素
        # driver.find_elements_by_class_name("ico_link")
        img_eles_list = driver.find_elements_by_xpath("//div[@class='ico_link']/img")
        img_res = choice(img_eles_list)  # 随机选择一个表情
        ims_src = img_res.get_attribute('src')
        img_res.click()  # 点击表情

        # 点击发布
        driver.find_element_by_class_name("btn_big").click()
        # driver.find_element_by_xpath("//input[@class='btn_big']")

        sleep(2)
        # 检查发布心情是否正确
        actu_mood_text = driver.find_element_by_id("mini-content").text

        TestCase().assertEqual(actu_mood_text, set_mood)  # 比较文本是否一致

        actu_src = driver.find_element_by_id("mini-content").find_element_by_tag_name('img').get_attribute('src')
        TestCase().assertEqual(actu_src, ims_src)  # 比较图表链接地址是否一致
    else:
        pass




