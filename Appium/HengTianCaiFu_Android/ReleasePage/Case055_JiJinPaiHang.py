__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
SerchTitle = "私募"

class JiJinPaiHang:
    def Into_JiJinPaiHang(driver):
        try:
            with allure.step('点击进入基金排行'):
                time.sleep(8)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "基金排行":
                        i.click()
                        break
            pytest_TestResult = True

        except Exception as e:
            print("进入基金排行报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def SwitchDingTou(driver):
        try:
            with allure.step('选择定投排行'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/top_tab2",18,3).click()
        except Exception as e:
            print("进入基金排行报错:", e)





    def JiJinPaiHang(driver):
        try:
            with allure.step('输入产品名'):
                import os
                os.popen("adb shell settings put secure default_input_method com.baidu.input_huawei/.ImeService")
                time.sleep(3)
                serch = Page.wait_elem(driver,"com.chtwm.mall:id/search_et_input",30,3)
                #.send_keys(SerchTitle)
                serch.send_keys(SerchTitle)
                time.sleep(3)
                from selenium.webdriver.common.keys import Keys
                #serch.send_keys(Keys.ENTER)
                time.sleep(2)

                os.popen("adb shell input keyevent 66")
                #driver.keyevent(84)
                #serch.keyevent(66)
                #time.sleep(3)
                #serch.press_keycode(66)

            with allure.step('选择搜索出的第一条私募'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/search_suggestions_tv",18,3).click()
                time.sleep(15)

            pytest_TestResult = True


        except Exception as e:
            print("基金诊断报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult

