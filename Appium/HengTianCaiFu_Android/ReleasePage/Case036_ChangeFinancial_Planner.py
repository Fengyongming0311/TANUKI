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
title = "变更专属理财师"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
FinancialPlannernum = "029829"
#理财师工号
ChangeReason = "恒天理财生产环境上线测试变更专属理财师功能是否正常，填写的变更专属理财师，麻烦看到给拒绝掉，谢谢"

############
class ChangeFinancial_Planner:
    def ChangeFinancial_Planner(driver):
        try:
            with allure.step('理财师页面→点击变更专属理财师'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/mylcs_atonce_bt", 5).click()

            with allure.step('提示是否变更专属理财师→点击确认'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 5).click()

            with allure.step('点击变更的新理财师'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_new_tv", 5).click()

            with allure.step('输入新的理财师工号'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_input_ed",10,2).send_keys(FinancialPlannernum)

            with allure.step("点击查询"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_query_tv",10,2).click()

            with allure.step("选择查询出的员工"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_isshow_ll",10,2).click()

            with allure.step("选择变更原因"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_reasons_tv",10,2).click()

            with allure.step("前五个变更原因"):
                import random
                reason = random.choice(["one","two","three","four","five"])
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/cause_%s"%reason,10,2).click()

            with allure.step("点击提交按钮"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_finacial_bt",10,2).click()


        except Exception as e:
            print("%s报错:"%title, e)
            time.sleep(3)
            Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm",10,2).click()

    #生产环境变更专属理财师功能，原因选择其他填写线上上线测试看看能不能不打电话
    def Prod_ChangeFinancial_Planner(driver):
        try:
            with allure.step('理财师页面→点击变更专属理财师'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/mylcs_atonce_bt", 5).click()

            with allure.step('提示是否变更专属理财师→点击确认'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 5).click()

            with allure.step('点击变更的新理财师'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_new_tv", 5).click()

            with allure.step('输入新的理财师工号'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_input_ed").send_keys(FinancialPlannernum)

            with allure.step("点击查询"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_query_tv").click()

            with allure.step("选择查询出的员工"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/chooser_isshow_ll").click()

            with allure.step("选择变更原因"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_reasons_tv").click()

            with allure.step("选择第六个原因其他"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/cause_six").click()

            with allure.step("输入变更原因看看能不能不打电话"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/et_reason").send_keys(ChangeReason)

            with allure.step("点击提交按钮"):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/change_finacial_bt").click()


        except Exception as e:
            print("%s报错:"%title, e)



    def ChangeFinancial_Planner_CheckPoint(driver):
        try:
            with allure.step('截取变更理财师后页面截图'):
                time.sleep(8)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #如果截图页面还在变更专属理财师页面说明提交没有成功

            with allure.step('查看我的页面理财师的工号是否与提交工号一致'):
                job_number = Page.find_elem_id(driver,"com.chtwm.mall:id/financial_planner_job_number_tv")
                if job_number == "H" + FinancialPlannernum:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

        except Exception as e:
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
        finally:
            return pytest_TestResult





