import unittest
from unittest.loader import TestLoader

import os

from thinksns.demo.t01_register import TestRegister
#第一种方式
suite = unittest.TestSuite()
# 构建测试集
# suite.addTest(TestRegister('test_register_01'))
# suite.addTests([TestRegister('test_register_01')])#以列表的方式

#第二种方式
loader = TestLoader()
#根据类名进行加载
# suite = loader.loadTestsFromTestCase(TestFri)
#根据模块(py文件)名进行加载
# suite = loader.loadTestsFromModule()
#通过discover实现，注意，discover 首先回去读取__init__中符合规则的
project_path = os.path.dirname(os.getcwd())
suite = loader.discover(project_path,'test*.py')



if __name__ == "__main__":
    #第一种方式
    # 运行测试集合
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #第二种方式
    # HTML
