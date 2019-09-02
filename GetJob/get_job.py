import unittest
from time import sleep

import os
from selenium import webdriver

from GetJob.excel_temp import ExcelOpreation
import logging


class GetJob(unittest.TestCase):
    def setUp(self):

        logging.basicConfig(  # 通过具体的参数来更改logging模块默认行为；
                level=logging.ERROR,  # 设置告警级别为ERROR；
                format="%(asctime)s---%(lineno)s----%(funcName)s: %(message)s",  # 自定义打印的格式；
                filename=os.path.join(os.getcwd(), "logs/job_log.txt"),  # 将日志输出到指定的文件中；
                filemode="a",  # 以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
        )

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)
        self.driver.maximize_window()

    def test_get51_job(self):
        # 工作地点
        work_locations = ["成都"]
        # 搜索内容
        search_content = "软件测试"

        driver = self.driver
        base_url = "https://login.51job.com/login.php?lang=c"
        driver.get(base_url)
        # 登录
        driver.find_element_by_name("loginname").send_keys("578863544@qq.com")
        driver.find_element_by_name("password").send_keys("1qaz2wsx")
        driver.find_element_by_id("login_btn").click()
        driver.find_element_by_id("login_btn").click()
        sleep(2)
        driver.find_element_by_link_text("首页").click()
        sleep(2)

        if driver.find_element_by_id("work_position_input").text not in work_locations:
            # 选择地区
            for location in work_locations:
                pass

        # 输入查询内容
        driver.find_element_by_id("kwdselectid").send_keys(search_content)
        sleep(2)
        div_element = driver.find_element_by_xpath('//div[@class="ush top_wrap"]')
        div_element.find_element_by_tag_name("button").click()
        sleep(2)

        # 展开所有候选项
        # driver.find_element_by_xpath('//div[@class="dw_filter"]/div[@class="op"]').click()
        driver.execute_script("collapseExpansionSearch('https://search.51job.com', 'dw_filter', this);")
        sleep(1)

        # 月薪范围-多选
        driver.execute_script("multipleChoiceShow('providesalary', true);")
        # 勾选6k-8k
        driver.find_element_by_xpath('//div[@id="multichoices_providesalary"]/ul/li[6]/a').click()
        # 勾选8k-10k
        driver.find_element_by_xpath('//div[@id="multichoices_providesalary"]/ul/li[7]/a').click()
        # 确定
        driver.find_element_by_id("submit_providesalary").click()
        sleep(2)

        # 工作年限 1-3年
        # driver.execute_script("multipleChoiceShow('workyear', true);")
        div_element = driver.find_element_by_id("filter_workyear")
        div_element.find_element_by_link_text("1-3年").click()

        # 学历要求  专科、本科
        # 展开多选
        driver.execute_script("multipleChoiceShow('degreefrom', true);")
        # 勾选专科、本科
        driver.find_element_by_xpath('//div[@id="multichoices_degreefrom"]/ul/li[4]/a').click()
        driver.find_element_by_xpath('//div[@id="multichoices_degreefrom"]/ul/li[5]/a').click()
        # 确定
        driver.find_element_by_id("submit_degreefrom").click()
        sleep(2)

        # 查看当前最多页码
        max_page_num = int(driver.find_elements_by_xpath("//div[@class='p_in']/ul/li")[-2].text)
        print(max_page_num)
        file_path = os.path.join(os.getcwd(), '各个网站职位信息.xls')
        excel = ExcelOpreation()
        # 生成表格对象
        for i in range(max_page_num):
            # # 解析每一页数据
            data_list = self.get_data_from_cur_page51()
            # # 写入数据到表格
            try:
                excel.excelwrite(file_path, sheet_name='51job职位信息页', data_list=data_list)
            except Exception as err:
                logging.error("err:%s"%str(err))
                logging.error("写入数据为 data_list:%s"%str(data_list))
            if i != max_page_num - 1:
                # 点击下一页
                driver.find_element_by_link_text("下一页").click()
                sleep(1)

    def test_getzhilian_job(self):
        pass
        # 登录
        driver = self.driver
        driver.get('https://www.zhaopin.com/')
        driver.find_element_by_xpath(
                "//div[@class='zp-passport-widget-by-username__input-box zp-passport-widget-by-username__username-box']/input").send_keys(
                "578863544@qq.com")
        driver.find_element_by_xpath(
                "//div[@class='zp-passport-widget-by-username__input-box zp-passport-widget-by-username__password-box']/input").send_keys(
                "159357zhong")
        sleep(1)
        driver.find_element_by_class_name("zp-passport-widget-by-username__submit").click()
        # 输入关键词查询
        driver.find_element_by_class_name("zp-searchbox__input").send_keys("软件测试")
        driver.find_element_by_class_name("zp-searchbox__button").click()
        # 设置筛选条件
        # 薪资不限
        driver.find_element_by_class_name("query-salary__all").click()
        # 经验1-3年
        driver.find_element_by_xpath("//div[@class='query-others__borders workExperience']/ul/li[4]").click()
        # 全职
        driver.find_element_by_xpath("//div[@class='query-others__borders employmentType']/ul/li[2]").click()
        # 查询页数
        max_page_num = len(driver.find_elements_by_xpath("//div[@class = 'soupager']/span"))
        # 循环页数
        for i in range(max_page_num):
            # # 解析每一页数据
            data_list = self.get_data_from_cur_page_zhilian()
            # # 写入数据到表格
            # excel.excelwrite(file_path, sheet_name='51job职位信息页', data_list=data_list)
            if i != max_page_num - 1:
                # 点击下一页
                driver.find_element_by_xpath("//button[@class = 'btn soupager__btn']").click()
                sleep(2)

                # 获取当前页所有工作数据
                # 下一页
                # 写入数据到表格

    def get_data_from_cur_page_zhilian(self):
        # data_list = [['公司', '职位名称', '工作地点', '薪资', '发布时间', '招聘人数', '招聘要求']]  # 列表中存列表
        data_list = []  # 列表中存列表
        driver = self.driver
        # 循环获取当前页面信息
        div_elements = driver.find_element_by_id("listContent").find_elements_by_class_name(
            "contentpile__content__wrapper clearfix")
        for div_element in div_elements:
            data_list.append([])
            # 职位名称
            job_name = div_element.find_element_by_class_name(
                "contentpile__content__wrapper__item__info__box__jobname__title").get_attribute('title')
            company_name = div_element.find_element_by_class_name(
                "contentpile__content__wrapper__item__info__box__cname__title company_title").text
            job_saray = div_element.find_element_by_class_name(
                "contentpile__content__wrapper__item__info__box__job__saray").text
            work_location = '成都'
            post_time = ""

            handle = driver.current_window_handle
            # 进入招聘详细页面,打开一个新的窗口
            try:
                div_element.find_element_by_class_name(
                    "contentpile__content__wrapper__item__info__box__jobname__title").click()
            except Exception as err:
                print(err)
            # 获取当前所有窗口句柄（窗口A、B）
            handles = driver.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:
                    # 切换到新打开的窗口B
                    driver.switch_to_window(newhandle)
                    # 在新打开的窗口B中操作
                    # 获取到详细信息并整合
                    sleep(2)
                    print("获取到详细信息并整合")
                    res_data_list = self.deal_job_page_data_zhilian()

                    # data_list[-1].append(res_data_list[0])
                    # data_list[-1].append(str(res_data_list[1]))
                    # 关闭当前窗口B
                    driver.close()
                    # 切换回窗口A
                    driver.switch_to_window(handles[0])
            sleep(2)
            print("关闭当前页面")

    def get_data_from_cur_page51(self):
        """
        :return data_dic: 数据源
        """

        # data_list = [['公司', '职位名称', '工作地点', '薪资', '发布时间', '招聘人数', '招聘要求']]  # 列表中存列表
        data_list = []  # 列表中存列表
        driver = self.driver
        # 获取所有招聘列表信息
        div_ele_jobs = driver.find_elements_by_xpath("//div[@class='el']")[2:]
        # 循环点击，获取整合数据源
        for job_ele in div_ele_jobs:
            job_info_list = (job_ele.text).split('\n')
            job_name = job_info_list[0]  # 职位名称
            company_name = job_info_list[1]  # 公司名字
            work_location = job_info_list[2]  # 工作地点
            money = job_info_list[3]  # 薪资
            post_time = job_info_list[4]  # 发布时间
            sleep(1)
            data_list.append([])
            data_list[-1].append(company_name)
            data_list[-1].append(job_name)
            data_list[-1].append(work_location)
            data_list[-1].append(money)
            data_list[-1].append(post_time)
            span_ele_job_page = None
            try:
                span_ele_job_page = job_ele.find_element_by_xpath(".//p[@class='t1 ']/span/a")
            except Exception as err:
                span_ele_job_page = job_ele.find_element_by_xpath("//p[@class='t1 tg1']/span/a")
                logging.error('点击工作元素时错误信息err:%s'%str(err))
                logging.error("公司名称：%s"%company_name)
            # temp =job_ele.find_element_by_xpath(".//span[@class='t2']/a").text
            # temp2 =job_ele.find_element_by_class_name('t2').find_element_by_tag_name('a').text
            # HP会快速回复的公司，需要单独获取
            handle = driver.current_window_handle
            # 进入招聘详细页面,打开一个新的窗口
            try:
                span_ele_job_page.click()
            except Exception as err:
                print(err)
                logging.error('点击跳转到【%s】工作详细页面失败'%company_name)
            # 获取当前所有窗口句柄（窗口A、B）
            handles = driver.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:
                    # 切换到新打开的窗口B
                    driver.switch_to_window(newhandle)
                    # 在新打开的窗口B中操作
                    # 获取到详细信息并整合
                    sleep(2)
                    print("获取到详细信息并整合")
                    res_data_list = self.deal_job_page_data51(company_name)
                    data_list[-1].append(res_data_list[0])
                    data_list[-1].append(str(res_data_list[1]))
                    # 关闭当前窗口B
                    driver.close()
                    # 切换回窗口A
                    driver.switch_to_window(handles[0])
                    sleep(1)
            print("关闭当前页面")
        return data_list

    def deal_job_page_data51(self,*args,**kwargs):
        data_list = []
        driver = self.driver
        # 招聘人数
        people_num = 0
        # 地区、经验、学历、招人数、最新发布时间等等
        # '成都-锦江区  |  2年经验  |  本科  |  招2人  |  08-20发布'
        job_msg = driver.find_element_by_xpath("//p[@class='msg ltype']").get_attribute("title")
        print(job_msg)
        job_msg_list = job_msg.split("|")
        # 招聘人数获取
        if job_msg.find('招'):
            start_pos = job_msg.find('招')
            end_pos = job_msg.find('人')
            people_num = job_msg[start_pos + 1:end_pos]

        # 工作职位信息和要求
        info_str = ''
        try:
            job_infos = driver.find_elements_by_xpath("//div[@class='bmsg job_msg inbox']/p")
            for item in job_infos:
                info_str += item.text + '\n'
            #上面的获取失败时采用第二种方式
            if len(info_str) == '':
                job_infos = driver.find_elements_by_xpath("//div[@class='bmsg job_msg inbox']/div")[:-3]
                for item in job_infos:
                    if item.text=='':
                        continue
                    info_str += item.text + '\n'
        except Exception as err:
            logging.error('获取【%s】招聘要求信息失败 err:%s'%(args[0],str(err)))

        data_list.append(people_num)
        data_list.append(info_str)

        return data_list

    def deal_job_page_data_zhilian(self):
        data_list = []
        driver = self.driver
        # 招聘人数
        people_num = 0
        # 地区、经验、学历、招人数、最新发布时间等等
        # '成都-锦江区  |  2年经验  |  本科  |  招2人  |  08-20发布'
        job_msg = driver.find_element_by_xpath("//ul[@class = 'summary-plane__info']/li[4]").text
        # 招聘人数获取
        if job_msg.find('招'):
            start_pos = job_msg.find('招')
            end_pos = job_msg.find('人')
            people_num = job_msg[start_pos + 1:end_pos]

        # 工作职位信息和要求
        info_str = '工作要求'
        job_infos = driver.find_element_by_xpath("//div[@class = 'describtion__detail-content']").text
        # for item in job_infos:
        #     info_str += item.text + '\n'
        # # print(info_str)

        # 发布时间

        data_list.append(people_num)
        data_list.append(info_str)

        return data_list

    def test_temp(self):
        driver = self.driver
        driver.get('https://jobs.51job.com/chengdu-gxq/112330014.html?s=01&t=0')
        # 工作职位信息和要求

        job_infos = driver.find_elements_by_xpath("//div[@class='bmsg job_msg inbox']/div")[:-3]
        info_str = ''
        for item in job_infos:
            if item.text=='':
                continue
            info_str += item.text + '\n'
        print(info_str)



    def tearDown(self):
        pass
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
