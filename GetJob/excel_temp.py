# -*- coding:utf-8 -*-
import os
from pandas.core.frame import DataFrame
import pandas as pd
import logging

class ExcelOpreation():
    def __init__(self):
         logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
                level=logging.ERROR,  # 设置告警级别为ERROR；
                format="%(asctime)s---%(lineno)s----%(funcName)s: %(message)s",  # 自定义打印的格式；
                filename=os.path.join(os.getcwd(), "logs/job_log.txt"),  # 将日志输出到指定的文件中；
                filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
        )


    def excelwrite(self, filename, sheet_name, data_list):
        sheet_data = pd.read_excel(filename, sheet_name=sheet_name)
        # sheet_data = pd.read_excel(filename, sheet_name=sheet_name)
        row_ser = sheet_data.shape
        # print(sheet_data.head(10))
        # row_ser = sheet_data.shape  # 获取当前(行，列)
        start_row = row_ser[0]
        try:
            for i in range(len(data_list)):
                # 增加行数据，在第row行新增
                sheet_data.loc[start_row] = data_list[i]
                start_row += 1
                # sheet_data.loc[row_ser] = data_list[i]
            # 增加列数据，给定默认值None
            # sheet_data['profession'] = None
            # 保存数据
            # DataFrame(sheet_data).to_excel(filename, sheet_name=sheet_name, index=False, header=True)
            DataFrame(sheet_data).to_excel(filename, sheet_name=sheet_name, index=False, header=True)
        except Exception as err:
            logging.error("err:%s"%str(err))
            logging.error("写入数据为 data_list=%s"%str(data_list[i]))

if __name__ == "__main__":
    data_list = [['深圳市风云实业有限公司', '软件测试工程师', '成都-青羊区', '0.6-1万/月', '08-30', '5',
                  '岗位职责：\n1. 编写测试用例；\n2. 执行测试用例，提交BUG；\n3. 提交测试记录及总结文档。\n\n任职要求：\n1. 计算机、电子、通信等相关专业本科及以上学历；\n2. 两年以上网络设备测试经验；\n3. 熟悉TCP/IP协议体系；\n4. 熟练掌握边界值、等价类等测试用例设计方法；\n5. 熟练常用测试工具；\n6. 能熟练应用下列脚本语言中的一种或多种者优先：tcl、python、vbs；\n7. 英文阅读能力良好。\n'],
                 ['成都主导科技有限责任公司', '软件测试工程师', '成都-青羊区', '8-15万/年', '08-30', '4',
                  '1.根据项目需求，确定测试软件的功能和性能要求，制定测试策略及用例；\n2.负责编写测试脚本，设计和搭建测试环境，执行软件测试、验收、反馈及跟踪、发布；\n3.负责测试流程维护，测试结果统计分析，改进测试效率质量。\n任职要求：\n1.计算机、软件工程、信息工程或相关专业，本科及以上学历；2年及以上软件测试工作经验； \n2.掌握至少一门编程语言，有编程经验的优先；\n3.掌握至少一种自动化测试框架/工具（Selenium、QTP、TD、LR、WR、MQC、JMeter），熟悉Git、Jenkins、SonarQube等开发、覆盖率、静态分析工具、测试平台，熟悉Mysql/Mycat中间件、熟悉TCP、HTTP/S等协议；\n4．具有脚本编写能力，能够独立解决性能测试或自动化测试中复杂的技术问题；\n5.工作责任心强，逻辑清晰，有较强的团队意识和沟通能力。\n'],
                 ['拙思信息科技（上海）有限公司', '软件测试工程师', '成都-锦江区', '0.8-1.2万/月', '08-30', '3',
                  '岗位职责\n●参与平台产品的需求分析、测试案例、测试执行、缺陷管理等整个测试流程；\n●对测试实施过程中发现的软件问题进行跟踪分析和报告，推动测试中发现的问题及时合理解决；\n●善于学习及尝试新方法、新工具提高整个Web平台的测试效率及质量；\n●善于从用户角度评审需求及最终设计，提高产品的易用性；\n●完成公司安排的其它测试工作。\n岗位要求\n●两年以上测试经验，熟悉测试理论、流程与方法；\n●能熟练编写项目测试计划和测试用例，至少熟悉一种缺陷管理软件（禅道、Jira、QC等）；\n●熟悉jmeter或loadrunner等测试工具 ；\n●熟练掌握黑盒测试方法，能够独立完成功能测试、接口测试等测试任务；\n●熟练SQL语句，熟悉MySql/Oracle等常用数据库使用，熟悉Linux/Unix操作系统；\n●良好的沟通能力,积极协助解决问题,高效的执行能力,保证项目质量和进度的达成；\n●有接口、自动化、性能测试经验者优先考虑。\n'],
                 ['成都美创医疗科技股份有限公司','软件测试工程师员', '成都', '0.6-1万/月', '08-30', '1',
                  '\n任职要求：\n岗位职责：\n1、学习并掌握不同类型医疗器械；\n2、能够根据提供的软件需求规格说明书和软件，得到测试项，制定测试方案；\n3、能根据测试项编写手工测试用例，将测试用例录入用例管理系统，并执行测试用例；\n4、根据测试结果，将相关软件bug录入缺陷管理系统，能够识别，跟踪和定位问题；\n5、根据执行测试结果编写测试报告和测试版本发布；\n6、上级领导安排的其它工作。\n']]
    file_path = os.path.join(os.getcwd(), '各个网站职位信息.xls')
    excel = ExcelOpreation()
    excel.excelwrite(file_path, sheet_name='51job职位信息页', data_list=data_list)