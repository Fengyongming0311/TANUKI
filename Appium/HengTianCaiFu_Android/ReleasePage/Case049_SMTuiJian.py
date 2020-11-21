__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class SMTuiJian:
    def Into_SMTuiJian(driver):
        try:
            with allure.step('首页→上滑，显示私募推荐'):
                time.sleep(10)
                huadong.shanghua(driver, 2850)

                time.sleep(3)

            with allure.step('进入私募推荐内容'):
                elems = driver.find_elements_by_id("com.chtwm.mall:id/item_title_name")
                try:
                    time.sleep(3)
                    elems[0].click()
                    time.sleep(3)
                    huadong.shanghua(driver,500)
                    time.sleep(3)
                    driver.back()
                    time.sleep(3)
                except Exception as e:
                    print ("elems[0]报错：",e)
                elems = driver.find_elements_by_id("com.chtwm.mall:id/item_title_name")
                try:
                    time.sleep(3)
                    elems[1].click()
                    time.sleep(3)
                    huadong.shanghua(driver,500)
                    time.sleep(3)
                    driver.back()
                    time.sleep(3)
                except Exception as e:
                    print ("elems[1]报错：",e)

                elems = driver.find_elements_by_id("com.chtwm.mall:id/item_title_name")
                try:
                    time.sleep(3)
                    elems[2].click()
                    time.sleep(3)
                    huadong.shanghua(driver,500)
                    time.sleep(3)
                    driver.back()
                    time.sleep(3)
                except Exception as e:
                    print ("elems[2]报错：",e)

            pytest_TestResult = True

        except Exception as e:
            print("进入私募推荐报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult

