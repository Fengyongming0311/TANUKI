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
title = "交易明细"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############

class Into_TransDetails:
    def Into_TransDetails(driver):
        try:
            with allure.step('我的→进入交易明细页面'):
                time.sleep(4)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/myself_item_tv")
                for i in elems:
                    if i.text == title:
                        i.click()
                        break

            pytest_TestResult = True

        except Exception as e:
            print("%s报错:"%title, e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult


