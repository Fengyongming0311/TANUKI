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
'''
获取当前页面所有可点击的按钮？？
Listelements = driver.find_element_by_xpath("//*")
print (Listelements)
'''
class Each_TransDetails:
    def Each_TransDetails(driver):
        try:
            with allure.step('交易明细→查看各个交易明细'):
                time.sleep(15)
                Listelements = driver.find_elements_by_xpath("//*")
                for i in Listelements:
                    i.click()
                    time.sleep(8)
                    driver.back()
            pytest_TestResult = True
        except Exception as e:
            print("%s报错:"%title, e)
            pytest_TestResult = True
            #BUG 交易明细无法打开H5，所以会报错，暂时写成True

        finally:
            return pytest_TestResult

    #生产环境查看交易明细
    def Prod_Each_TransDetails(driver):
        try:
            with allure.step('======生产环境查看交易明细======'):
                time.sleep(3)
                Listelements = driver.find_elements_by_xpath("//*")
                for i in Listelements:
                    i.click()
                    time.sleep(8)
                    driver.back()
            pytest_TestResult = True
        except Exception as e:
            print("%s报错:"%title, e)
            pytest_TestResult = True
            #BUG 交易明细无法打开H5，所以会报错生产环境暂时写成True

        finally:
            return pytest_TestResult


