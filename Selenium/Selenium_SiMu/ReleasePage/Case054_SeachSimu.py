__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
SerchTitle = "私募"

class SeachSimu:
    def Into_SeachSimu(driver):
        try:
            with allure.step('点击输入私募产品名称'):
                time.sleep(5)
                #com.chtwm.mall:id/myself_item_tv
                Page.wait_elem(driver,"com.chtwm.mall:id/product_search_relative",20,3).click()

        except Exception as e:
            print("进入搜索公募报错:", e)


    #输入私募产品名称
    def SeachSimu_Input(driver):
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

    #选择已有的名字
    def SeachSimu_Select(driver):
        try:
            with allure.step('输入产品名'):
                time.sleep(3)
                #Page.wait_elem(driver,"com.chtwm.mall:id/history_search_grid",21,3).click()
                driver.find_element_by_xpath("//*[@text='私募']").click()

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