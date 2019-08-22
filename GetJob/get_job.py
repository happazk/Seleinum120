import unittest
from time import sleep

from selenium import webdriver


class GetJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
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

        #学历要求  专科、本科
        #展开多选
        driver.execute_script("multipleChoiceShow('degreefrom', true);")
        #勾选专科、本科
        driver.find_element_by_xpath('//div[@id="multichoices_degreefrom"]/ul/li[4]/a').click()
        driver.find_element_by_xpath('//div[@id="multichoices_degreefrom"]/ul/li[5]/a').click()
        # 确定
        driver.find_element_by_id("submit_degreefrom").click()
        sleep(2)

        # 查看当前最多页码
        max_page_num = int(driver.find_elements_by_xpath("//div[@class='p_in']/ul/li")[-2].text)
        print(max_page_num)
        for i in range(max_page_num):
            # 解析每一页数据
            self.get_data_from_cur_page()
            if i != max_page_num-1:
                # 点击下一页
                driver.find_element_by_link_text("下一页")
                sleep(2)


    def get_data_from_cur_page(self):
        driver = self.driver
        # 获取所有招聘列表信息
        div_ele_jobs = driver.find_elements_by_xpath("//div[@class='el']")[2:]
        # 循环点击，获取整合数据源
        for job_ele in div_ele_jobs:
            job_info_list = (job_ele.text).split('\n')
            job_name=job_info_list[0]#职位名称
            company_name =job_info_list[1]#公司名字
            work_location =job_info_list[2]#工作地点
            money =job_info_list[3]#薪资
            post_time =job_info_list[4]#发布时间
            sleep(1)
            span_ele_job_page=job_ele.find_element_by_xpath(".//p[@class='t1 ']/span")
            # temp =job_ele.find_element_by_xpath(".//span[@class='t2']/a").text
            # temp2 =job_ele.find_element_by_class_name('t2').find_element_by_tag_name('a').text
            # HP会快速回复的公司，需要单独获取
            # span_ele_job_page_quick=job_ele.find_element_by_xpath("//p[@class='t1 tg1']/span")

            handle = driver.current_window_handle
            #进入招聘详细页面,打开一个新的窗口
            span_ele_job_page.click()
            # 获取当前所有窗口句柄（窗口A、B）
            handles = driver.window_handles
            # 对窗口进行遍历
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle!=handle:
                    # 切换到新打开的窗口B
                    driver.switch_to_window(newhandle)
                    # 在新打开的窗口B中操作
                    #获取到详细信息并整合
                    sleep(2)
                    print("获取到详细信息并整合")
                    self.deal_job_page_data()
                    # 关闭当前窗口B
                    driver.close()
                    #切换回窗口A
                    driver.switch_to_window(handles[0])
            sleep(2)
            print("关闭当前页面")

    def deal_job_page_data(self):
        driver = self.driver
        #招聘人数
        people_num = 0
        #地区、经验、学历、招人数、最新发布时间等等
        # '成都-锦江区  |  2年经验  |  本科  |  招2人  |  08-20发布'
        job_msg = driver.find_element_by_xpath("//p[@class='msg ltype']").get_attribute("title")
        print(job_msg)
        job_msg_list = job_msg.split("|")
        #招聘人数获取
        if job_msg.find('招'):
            start_pos = job_msg.find('招')
            end_pos = job_msg.index('|', start_pos)
            end_pos = job_msg.find('人')
            people_num = job_msg[start_pos+1:end_pos]

        #工作职位信息和要求
        div_ele = driver.find_element_by_class_name("tCompany_main")
        job_infos = driver.find_elements_by_xpath("//div[@class='bmsg job_msg inbox']/p")
        info_str = ''
        for item in job_infos:
            info_str += item.text+'\n'
        print(info_str)
        #写入表格中
        pass






    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
