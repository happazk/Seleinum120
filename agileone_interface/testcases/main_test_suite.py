'''
Created on 2019年8月3日

@author: Administrator
'''
import os, time
from unittest.suite import TestSuite
from unittest.runner import TextTestRunner
from unittest.loader import TestLoader
# from agileone_interface.base.HTMLTestRunner import HTMLTestRunner
from agileone_interface.base.HTMLTestRunner_PY3 import HTMLTestRunner


# 第一部分：收集脚本
from agileone_interface.send_email.send_email_main import send_email_qq

'''
方式一：通过TestSuite类
'''
# 实例化一个TestSuite对象
# suite = TestSuite()
# 通过addTest(test)方法，test参数格式是：测试用例类名('用例方法名')
# suite.addTest(TestRegister('test_01'))
# suite.addTest(TestFriendlyLink('test_01'))
# 通过addTests(tests)方法，tests代表的是含有单元测试脚本的可迭代对象
# suite.addTests([TestRegister('test_01'), TestFriendlyLink('test_01'), 
#                 TestFriendlyLink('test_02')])
'''
方式二：通过TestLoader类
'''
# 实例化一个TestLoader对象
loader = TestLoader()
# 根据测试用例类名进行加载
# suite = loader.loadTestsFromTestCase(TestFriendlyLink)
# 根据指明的模块名进行加载
# suite = loader.loadTestsFromModule(t02_friendly_link)
# 通过discover方法：根据指定的工程目录下文件（模块）的命名规则来进行自动扫描加载测试用例，返回值为：TestSuite对象
# test*.py 指的是:
# 1、先加载包的配置文件中已经声明的模块中符合规则的测试用例：
# （第一必须继承TestCase类，第二必须有以test开头的方法）（如果没有符合规则的，会取得内容为空 的suite对象）
# 2、再去扫描所有以test开头的模块，并加载用例（如果没有符合规则的，则不录入，就是不收集起来）
#注意，根据1条件查找执行后，依然会根据2条件再次查找执行符合条件的用例
project_path = os.path.dirname(os.getcwd())
suite = loader.discover(project_path, "specification*.py")

# 第二部分：执行脚本
'''
方式一：通过TextTestRunner类
'''
# # 实例化一个TextTestRunner对象
# runner = TextTestRunner()
# # 调用run方法执行测试集合
# runner.run(suite)
'''
方式二：通过HTMLTestRunner类
'''
# 定义报告文件的路径
report_path = project_path+"\\reports\\"+time.strftime("%Y%m%d%H%M%S")+".html"
# strftime方法的参数格式有：
#     %Y  Year with century as a decimal number.
#     %m  Month as a decimal number [01,12].
#     %d  Day of the month as a decimal number [01,31].
#     %H  Hour (24-hour clock) as a decimal number [00,23].
#     %M  Minute as a decimal number [00,59].
#     %S  Second as a decimal number [00,61].
#     ............

# 打开报告文件（如果不存在会新建），得到文件对象
fp = open(report_path, "wb")
# mode参数格式如下：
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
# 'U'       universal newline mode (deprecated)

# 实例化HTMLTestRunner类，得到执行器
runner = HTMLTestRunner(stream=fp, title="Agileone项目自动化测试报告",
                        description="测试项为规格说明接口")


# 执行收集到的脚本
runner.run(suite)
send_email_qq()

