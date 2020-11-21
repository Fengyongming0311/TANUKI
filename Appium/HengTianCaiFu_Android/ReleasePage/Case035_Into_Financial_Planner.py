__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
title = "我的理财师"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class Into_Financial_Planner:
    def Into_Financial_Planner(driver):
        try:
            with allure.step('我的页面→点击理财师工号进入理财师页面'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/financial_planner_job_number_tv", 15).click()


        except Exception as e:
            print("%s报错:"%title, e)


    def Into_Financial_Planner_CheckPoint(driver):
        try:
            with allure.step('截取我的理财师页面截图'):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
            with allure.step("检查页面标题"):
                check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

        except Exception as e:
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
        finally:
            return pytest_TestResult





