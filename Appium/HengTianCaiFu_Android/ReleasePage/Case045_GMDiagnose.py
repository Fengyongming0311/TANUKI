__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class GM_Diagnose:
    def Into_GM_Diagnose(driver):
        try:
            with allure.step('首页→公募组合'):
                time.sleep(6)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "公募诊断":
                        i.click()
                        pytest_TestResult = True
                        break

            #005H5脚本不跳的话关闭driver.back()
            time.sleep(5)
            driver.back()

        except Exception as e:
            print("进入公募诊断报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def GM_Diagnose(driver):
        try:
            with allure.step('公募诊断→基金诊断'):
                time.sleep(3)
                Listelements = driver.find_elements_by_xpath("//*")
                #层级往下定位
                for i in Listelements:
                    i.click()
                    time.sleep(3)
            pytest_TestResult = True



        except Exception as e:
            print("基金诊断报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


