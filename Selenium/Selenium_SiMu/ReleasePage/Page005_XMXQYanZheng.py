__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait



class XMXQYanZheng:
    def XiangMuXiangQing(driver):
        #营销项目——项目详情
        try:

            with allure.step('从项目附件往前查看'):
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-attachment\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-attachment\"]").click()
                #<div id="tab-attachment" aria-controls="pane-attachment" role="tab" aria-selected="true" tabindex="0" class="el-tabs__item is-top is-active">项目附件</div>
                #进入项目附件功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-relaProduct\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-relaProduct\"]").click()
                #<div id="tab-relaProduct" aria-controls="pane-relaProduct" role="tab" tabindex="-1" class="el-tabs__item is-top">相关产品</div>
                #进入相关产品功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-modifyFlow\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-modifyFlow\"]").click()
                #<div id="tab-modifyFlow" aria-controls="pane-modifyFlow" role="tab" tabindex="-1" class="el-tabs__item is-top">资料修改流水</div>
                #进入资料修改流水功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-accDetail\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-accDetail\"]").click()
                #<div id="tab-accDetail" aria-controls="pane-accDetail" role="tab" tabindex="-1" class="el-tabs__item is-top">到账明细</div>
                #进入到账明细功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-reserQueueup\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-reserQueueup\"]").click()
                #<div id="tab-reserQueueup" aria-controls="pane-reserQueueup" role="tab" tabindex="-1" class="el-tabs__item is-top">预约排队</div>
                #进入预约排队功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-reserManage\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-reserManage\"]").click()
                #<div id="tab-reserManage" aria-controls="pane-reserManage" role="tab" tabindex="-1" class="el-tabs__item is-top">预约管理</div>
                #进入预约管理功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-relaPerson\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-relaPerson\"]").click()
                #<div id="tab-relaPerson" aria-controls="pane-relaPerson" role="tab" tabindex="-1" class="el-tabs__item is-top">相关人员</div>
                #进入相关人员功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-issuePlan\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-issuePlan\"]").click()
                #<div id="tab-issuePlan" aria-controls="pane-issuePlan" role="tab" tabindex="-1" class="el-tabs__item is-top">发行方案</div>
                #进入发行方案功能
                time.sleep(3)
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("div[id=\"tab-detail\"]"))
                driver.find_element_by_css_selector("div[id=\"tab-detail\"]").click()
                #<div id="tab-detail" aria-controls="pane-detail" role="tab" aria-selected="true" tabindex="0" class="el-tabs__item is-top is-active">基本信息</div>
                #进入基本信息功能


                pytest_TestResult = True
        except Exception as e:
            print("验证项目详情中功能列表报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
