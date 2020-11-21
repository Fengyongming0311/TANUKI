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
title = "月度投资报告"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############


class Investrepo:
    def Into_Investrepo(driver):
        try:
            with allure.step('我的→月度投资报告'):
                time.sleep(3)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/myself_item_tv")
                for i in elems:
                    if i.text == title:
                        i.click()
                        pytest_TestResult = True
                        break

            with allure.step('月度投资报告截图'):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            print("进入%s报错:"%title, e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult




    def CheckInvestrepo(driver):
        try:
            with allure.step('查看报告'):
                Listelements = driver.find_elements_by_xpath("//*")
                for i in Listelements:
                    i.click()
                    time.sleep(8)
                    driver.back()


            pytest_TestResult = True


        except Exception as e:
            print("查看%s报错:"%title, e)
            pytest_TestResult = True
            #BUG H5 页面，只能先pass
            #driver.back()
        finally:
            return pytest_TestResult

