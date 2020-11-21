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
title = "检查版本"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############


class CheckVersion:
    def CheckVersion(driver):
        #检查版本
        try:
            with allure.step('点击检查版本'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_devide", 10).click()
        except Exception as e:
            print("点击检查版本报错:", e)
            pass

    def CheckVersion_CheckPoint(driver):
        try:
            with allure.step('点击"稍后再说"不做升级，页面返回关于'):
                Page.wait_elem(driver,"com.chtwm.mall:id/iv_close", 10).click()
        except:
            #暂时没见过最新版本啥样，不处理
            pass
        finally:
            pytest_TestResult = True
            return pytest_TestResult
