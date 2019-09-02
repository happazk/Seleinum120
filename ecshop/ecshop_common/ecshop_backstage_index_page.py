# 后台管理界面首页


# 菜单-商品管理
from selenium import webdriver
from selenium.webdriver.common.by import By

iframe_product_man = [By.ID, 'menu-frame']  # 菜单iframe框架
product_list_element = [By.LINK_TEXT, "商品列表"]  # 商品列表
add_new_item_element = [By.LINK_TEXT, "添加新商品"]  # 添加新商品
categories_element = [By.LINK_TEXT, "商品分类"]  # 商品分类
user_comment = [By.LINK_TEXT, "用户评论"]  # 用户评论
product_brand = [By.LINK_TEXT, "商品品牌"]  # 商品品牌
product_Types = [By.LINK_TEXT, "商品类型"]  # 商品类型


def get_product_Types(driver, *args, **kwargs):
    """
    进入商品类型
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    driver.find_element(*product_Types).click()


def get_product_brand(driver, *args, **kwargs):
    """
    进入商品品牌
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    driver.find_element(*product_brand).click()


def get_user_comment(driver, *args, **kwargs):
    """
    进入用户评论
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    driver.find_element(*user_comment).click()


def get_categories_element(driver, *args, **kwargs):
    """
    进入商品分类
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    driver.find_element(*categories_element).click()


def get_add_new_item(driver, *args, **kwargs):
    """
    进入添加新商品
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    # driver = webdriver.Firefox()


    # 进入框架
    iframe_ele = driver.find_element(*iframe_product_man)
    driver.switch_to_frame(iframe_ele)
    driver.find_element(*add_new_item_element).click()
    # 回到默认位置
    driver.switch_to_default_content()


def get_product_list(driver, *args, **kwargs):
    """
    进入商品列表
    :param driver:
    :param args:
    :param kwargs:
    :return:
    """
    driver.find_element(*product_list_element).click()
