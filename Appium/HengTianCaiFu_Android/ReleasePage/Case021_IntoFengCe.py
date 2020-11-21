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
title = "风险测评"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class IntoFengCe:
    def IntoFengCe(driver):
        try:
            with allure.step('点击基金风险评测'):
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_found_ll", 18,3).click()

        except Exception as e:
            print("进入基金风险评测报错:", e)



    def IntoFengCe_CheckPoint(driver):
        try:
            with allure.step('验证风险评测title'):
                time.sleep(5)
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title", 10)
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

        except Exception as e:
            print("进入风险评测报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult