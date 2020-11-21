__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class GMGroup:
    def Into_GMGroup(driver):
        try:
            with allure.step('我的→公募组合'):
                time.sleep(6)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "公募组合":
                        i.click()
                        pytest_TestResult = True
                        break

            #003脚本不跳的话关闭driver.back()
            time.sleep(5)
            driver.back()

        except Exception as e:
            print("进入公募组合报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def GMGroup(driver):
        try:
            with allure.step('公募组合→查看组合投资方案'):
                time.sleep(3)
                Listelements = driver.find_elements_by_xpath("//*")
                #层级往下定位
                for i in Listelements:
                    i.click()
                    time.sleep(3)
                    huadong.shanghua(driver,500)
                    time.sleep(2)
                    huadong.shanghua(driver,500)
                    time.sleep(2)
                    driver.back()
                driver.back()
                #回到首页

            pytest_TestResult = True


        except Exception as e:
            print("进入查看组合投资方案报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult












