__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
SerchTitle = "私募"

class NewFund:
    def Into_NewFund(driver):
        try:
            with allure.step('点击进入新发基金'):
                time.sleep(8)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "新发基金":
                        i.click()
                        break
            pytest_TestResult = True

        except Exception as e:
            print("进入新发基金报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def ClickFund(driver):
        try:
            with allure.step('点击基金名称进入新发基金'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_title",18,3).click()
                time.sleep(8)
                driver.back()
                pytest_TestResult = True
        except Exception as e:
            print("进入基金排行报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



