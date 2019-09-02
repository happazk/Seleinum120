'''
Created on 2019年7月31日

@author: wangchaolin
'''
import unittest, os
from selenium import webdriver
from time import sleep
from thinksns_common import login_thinksns
from random import randint
from selenium.webdriver.chrome.options import Options
import jpype

class TestUploadPictures(unittest.TestCase):

    def setUp(self):
        # 第一步：初始化相关参数
        chrome_options = Options()
        prefs= {
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1
        }
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
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
        email = "wcl12001@qq.com"
        password = "123456"
        name = "王朝12001"
        # 登录主账号
        login_thinksns(driver, email, password, name)
        # 先定位到左侧应用列表，再点击 相册  
        driver.find_element_by_class_name("user_app_list").find_element_by_link_text("相册").click()
        # 得到当前照片数量 我的全部照片(2) 
        number = self.get_pictures_number(driver, "我的全部照片(", ")")
        # 点击 上传
        driver.find_element_by_link_text("上传").click()
        sleep(1)
        # 定义jvm和sikuli jar包所在的路径
        jvm_path = r"C:\Program Files\Java\jdk1.8.0_151\jre\bin\server\jvm.dll"
        jar_path = "-Djava.class.path="+self.path+r"\libs\sikulixapi.jar"
        # 启动JVM
        jpype.startJVM(jvm_path, jar_path)
        # 找到能够进行屏幕操作的Screen类（相当于将Java版本的Screen类转换成Python的）
        Screen = jpype.JClass("org.sikuli.script.Screen")
        # 实例化该Screen类
        screen = Screen()
        # 定义添加照片按钮图片所在的路径
        add_path = self.path+r"\images\sikuli_imgs\add.png"
        # 根据实例化对象，点击该图片
        screen.click(add_path)
        # 定义文件名输入框图片所在的路径
        input_path = self.path+r"\images\sikuli_imgs\input.png"
        # 根据实例化对象，点击该图片
        screen.click(input_path)
        # 定义两张需要上传的照片的路径 "c:\灯塔.jpg" "c:\八仙花.jpg" 
        img1 = self.path+"\\images\\blog_imgs\\"+str(randint(0,7))+".jpg"
        img2 = self.path+"\\images\\blog_imgs\\"+str(randint(0,7))+".jpg"
        img_path = '"'+img1+'" "'+img2+'"'
        # 根据实例化对象，在输入框内输入上述路径
        screen.type(input_path, img_path)
        # 定义打开按钮的图片所在的路径
        open_path = self.path+r"\images\sikuli_imgs\open.png"
        # 根据实例化对象，点击该图片
        screen.click(open_path)
        sleep(1)
        # 关闭JVM
        jpype.shutdownJVM()
        # 点击开始上传  
        driver.find_element_by_id("btnUpload").click()
        sleep(2)
        # 判断是否出现成功的提示，判断在其中即可： 照片上传成功！  
        actual_tip = driver.find_element_by_name("save_upload_photos").text
        self.assertIn("照片上传成功！", actual_tip)
        # 点击完成上传  
        driver.find_element_by_class_name("btn_b").click()
        # 得到当前照片数量 共4张 
        actual_number = self.get_pictures_number(driver, "共", "张")
        # 判断照片数量的变化是否正确
        self.assertEqual(number+2, actual_number)
    
    def get_pictures_number(self, driver, start_tag, end_tag):
        # *********************获取当前的照片数量*********************
        # 定位出照片数量所在的div元素，并取出其文本值  
        text = driver.find_element_by_class_name("MenuSub").text
        # 根据开始标记计算出开始的位置
        start_pos = text.index(start_tag)+len(start_tag)
        # 根据结束标记计算出结束的位置
        end_pos = text.index(end_tag)
        # 根据开始位置和结束位置截取出照片数量
        number = text[start_pos:end_pos]
        # 最后返回照片数量
        return int(number)

    def tearDown(self):
        # 第五步：释放资源
        self.driver.quit()

