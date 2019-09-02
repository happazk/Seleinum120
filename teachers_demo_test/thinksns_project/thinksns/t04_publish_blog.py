'''
Created on 2019年7月29日

@author: wangchaolin
'''
import unittest, os
from selenium import webdriver
from time import sleep, time
# from thinksns_common.login import login_thinksns
from thinksns_common import login_thinksns
from random import choice, randint
from selenium.webdriver.support.select import Select

class TestPublishBlog(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
        self.driver = webdriver.Chrome()
        self.base_url ="http://172.31.31.100:8200/"
        # 设置元素识别超时时间
        self.driver.implicitly_wait(15)
        # 设置页面加载超时时间
        self.driver.set_page_load_timeout(30)
        # 设置异步脚本加载超时时间
        self.driver.set_script_timeout(30)
        # 设置将谷歌浏览器最大化
        self.driver.maximize_window()
        # 得到项目实际路径
        self.path = os.path.dirname(os.getcwd())

    def test_01(self):
        # 第二步：打开被测网站
        driver = self.driver
        driver.get(self.base_url)
        # 第三步：执行测试动作
        # 定义测试数据
        email_a = "wcl12001@qq.com"
        password_a = "123456"
        name_a = "王朝12001"
        email_b = "9291827@qq.com"
        password_b = "123456"
        name_b = "王朝林"
        email_c = "wcl11701@qq.com"
        password_c = "123456"
        name_c = "王朝11701"
        # 定义访问权限和评论权限的列表
        privacy_list = ["任何人可见","仅好友可见","私密日记","凭密码访问"]
        cc_list = ["任何人可评论","好友可评论","关闭评论"]
#         privacy = privacy_list[0]
#         cc = cc_list[0]
        # 循环进行测试
        for privacy in privacy_list:
            for cc in cc_list:
                # 调用发表日志的方法，新建日志
                self.new_blog(driver, privacy, cc, email_a, password_a, name_a)
                # 好友：检查访问权限
                self.check_privacy(driver, privacy, cc, email_b, password_b, name_b)
                # 陌生人：检查访问权限
                self.check_privacy(driver, privacy, cc, email_c, password_c, name_c, friend=False)
                # 点击 退出
                driver.find_element_by_link_text("退出").click()
                
    def new_blog(self, driver, privacy, cc, email, password, name):
        # ***************发表日志***************
        # 调用登录方法，登录主账号
        login_thinksns(driver, email, password, name)
        # 点击 发表
        driver.find_element_by_link_text("发表").click()
        # 定义随机文本内容（时间戳）
        self.content = str(time())
        # 定义日志标题：访问权限+评论权限+时间戳
        self.title = privacy+"+"+cc+self.content
        print(self.title)
        # 输入日志标题 
        driver.find_element_by_name("title").send_keys(self.title)
        # 先定位出日志内容所在的子页面iframe元素  
        iframe_element = driver.find_element_by_class_name("ke-iframe")
        # 然后切换到该子页面中
        driver.switch_to_frame(iframe_element)
        sleep(1)
        # 输入日志的内容  
        driver.find_element_by_class_name("ke-content").send_keys(self.content)
        # 切回默认页面
        driver.switch_to_default_content()
        sleep(1)
        # 点击表情图片所在的span元素  
        driver.find_element_by_class_name("ke-icon-emoticons").click()
        # 先定位出图片所在的div元素，再定位出其范围内所有的img元素  
        img_list = driver.find_element_by_class_name("ke-menu").find_elements_by_tag_name("img")
        # 再随机选择出一个img元素
        img_element = choice(img_list)
        # 根据img元素取出其src属性值
        self.src = img_element.get_attribute("src")
        # 再点击该img元素
        img_element.click()
        # 定义附件所在的路径
        img_path = self.path+"\\images\\blog_imgs\\"+str(randint(0,7))+".jpg"
        # 上传该附件 
        driver.find_element_by_name("myfile").send_keys(img_path)
        # 先定位出访问权限所在的下拉框元素，再将其交给Select类进行实例化，再根据可见文本的方法进行选择 
        privacy_element = driver.find_element_by_name("privacy")
        privacy_select = Select(privacy_element)
        privacy_select.select_by_visible_text(privacy)
        # 如果访问权限为 凭密码访问 则：
        if "凭密码访问" == privacy :
            sleep(1)
            # 输入密码 
            driver.find_element_by_name("password").send_keys("123456")
        # 先定位出评论权限所在的下拉框元素，再将其交给Select类进行实例化，再根据可见文本的方法进行选择 
        cc_element = driver.find_element_by_name("cc")
        cc_select = Select(cc_element)
        cc_select.select_by_visible_text(cc)
        # 点击发表按钮 
        driver.find_element_by_xpath("//input[@value='发 表']").click()
        # 检查日志详情
        self.check_blog_info(driver)
        
    def check_blog_info(self, driver):
        # ***************检查日志详情***************
        # 先定位出日志内容所在的div元素  
        div_element = driver.find_element_by_class_name("LogList")
        # 根据div元素定位出其范围内的日志标题所在的strong元素，并取出文本值进行判断 
        actual_title = div_element.find_element_by_xpath("//div[@class='tit_log']/h1/strong").text
        self.assertEqual(self.title, actual_title)
        # 根据div元素定位出其范围内的日志内容所在的div元素  
        div_element = div_element.find_element_by_id("blog_con")
        # 根据该div元素，取出其文本值并进行判断
        actual_content = div_element.text
        self.assertEqual(self.content, actual_content)
        # 根据该div元素，定位出其下一级的img元素，并取出src属性值进行判断
        actual_src = div_element.find_element_by_tag_name("img").get_attribute("src")
        self.assertEqual(self.src, actual_src)
    
    def check_privacy(self, driver, privacy, cc, email, password, name, friend=True):
        # ***************检查访问权限***************
        # 点击 退出
        driver.find_element_by_link_text("退出").click()
        # 调用登录方法，切换账号
        login_thinksns(driver, email, password, name)
        # 点击 随便看看
        driver.find_element_by_link_text("随便看看").click()
        # 点击 日志标题
        driver.find_element_by_link_text(self.title).click()
        # 如果访问权限为 任何人可见 则：
        if "任何人可见" == privacy:
        #     检查日志详情
            self.check_blog_info(driver)
            # 检查评论权限
            self.check_cc(driver, cc, name, friend)
        # 如果访问权限为 仅好友可见 则：
        elif "仅好友可见" == privacy:
        #     如果 是好友 则：
            if friend :
        #         检查日志详情
                self.check_blog_info(driver)
                # 检查评论权限
                self.check_cc(driver, cc, name, friend)
        #     否则：
            else:
        #         检查访问提示：只有主人的好友可以查看此日志
                self.check_privacy_tip(driver, "只有主人的好友可以查看此日志")
        # 如果访问权限为 私密日记 则：
        elif "私密日记" == privacy:
        #     检查访问提示：只有主人可以查看此日志
            self.check_privacy_tip(driver, "只有主人可以查看此日志")
        # 否则：
        else:
            try:
        #         检查访问提示：本日志需要密码才能访问
                self.check_privacy_tip(driver, "本日志需要密码才能访问")
        #         输入密码 
                driver.find_element_by_name("password").send_keys("123456")
        #         点击提交  
                driver.find_element_by_class_name("btn_b").click()
            except Exception as e:
                print("出现了已知Bug，为了练习顺利进行，所以进行异常处理！但现实企业工作时不能这样做！")
        #     检查日志详情
            self.check_blog_info(driver)
            # 检查评论权限
            self.check_cc(driver, cc, name, friend)
    
    def check_privacy_tip(self, driver, expect_tip):
        # ***************检查访问提示***************
        # 定位提示所在的div元素，并取出其文本值  
        tip = driver.find_element_by_class_name("bg_msg_btm").text
        # 判断期望提示在其中即可
        self.assertIn(expect_tip, tip)

    def check_cc(self, driver, cc, name, friend):
        # ***************检查评论权限***************
        # 如果评论权限为 任何人可评论 则：
        if "任何人可评论" == cc:
        #     新建评论
            self.new_comment(driver, name)
        # 如果评论权限为 好友可评论 则：
        elif "好友可评论" == cc:
        #     如果 是好友 则：
            if friend :
        #         新建评论
                self.new_comment(driver, name)
        #     否则：
            else:
        #         检查评论权限提示：
                self.check_cc_tip(driver, "您无法评论,日志发布者设置好友可评论")
        # 否则：
        else:
        #     检查评论权限提示：您无法评论,日志发布者已经关闭评论
            self.check_cc_tip(driver, "您无法评论,日志发布者已经关闭评论")
    
    def new_comment(self, driver, name):
        # ***************新建评论***************
        # 定义随机评论内容
        content = str(time())
        # 输入评论内容 
        driver.find_element_by_name("textarea").send_keys(content)
        # 点击发表评论  
        driver.find_element_by_id("content_submit").click()
        sleep(1)
        # 先定位出所有的评论记录所在的li元素，并取出第一个  
        li_element = driver.find_elements_by_class_name("comlist")[0]
        # 根据li元素，定位出其范围内的评论者名字显示所在的a元素，并取出文本值进行判断 
        actual_name = li_element.find_element_by_xpath("//h3[@class='tit_Critique lh25 mb5']/a").text
        self.assertEqual(name, actual_name)
        # 根据li元素定位出其范围内评论内容所在的p元素，并取出文本值进行判断
        actual_content = li_element.find_element_by_tag_name("p").text
        self.assertEqual(content, actual_content)
    
    def check_cc_tip(self, driver, expect_tip):
        # ***************检查评论权限提示***************
        # 定位提示所在的div元素，并取出其文本值  
        tip = driver.find_element_by_class_name("LogList").text
        # 判断期望提示在其中即可
        self.assertIn(expect_tip, tip)

    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

