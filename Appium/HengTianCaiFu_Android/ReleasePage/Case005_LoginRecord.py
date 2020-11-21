__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
sys.path.append("../Screenshots")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
title = "登录日志查询"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############


class LoginRecord:
    def LoginRecord(driver):
        #登录日志查询
        try:
            with allure.step('点击登录日志查询'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_login_record", 15).click()
        except Exception as e:
            print("点击登录日志查询报错:", e)
            pass

    def LoginRecord_CheckPoint(driver):
        time.sleep(6)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
        pytest_TestResult = True
        return pytest_TestResult

    def LoginRecord_PageBack(driver):
        try:
            with allure.step('点击返回按钮'):
                Page.find_elem_id(driver,"goBack").click()
        except:
            driver.back()