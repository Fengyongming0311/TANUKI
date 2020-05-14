__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class ChooseGoods:
    #智能购物车页面选择商品
    def ChooseGoods(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            all_handles = driver.window_handles
            now_handle = driver.current_window_handle
            for i in all_handles:
                if i != now_handle:
                    Detailpage_handles = i
                    break

            driver.switch_to.window(Detailpage_handles)

            time.sleep(5)
            driver.find_element_by_xpath("/html/body/wx-view[1]/wx-view[1]/wx-view/wx-view[2]/wx-view[1]/wx-view[1]/wx-view").click()
            #                             /html/body/wx-view[1]/wx-view[1]/wx-view/wx-view[3]/wx-view[1]/wx-view[1]/wx-view
            #选择一个购物车商品类别

            unittest_TestResult = True
        except Exception as e:
            print ("进入购物车执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult

    #家私产品选择商品
    def OrderChooseGoods(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            all_handles = driver.window_handles
            now_handle = driver.current_window_handle
            for i in all_handles:
                if i != now_handle:
                    Detailpage_handles = i
                    break

            driver.switch_to.window(Detailpage_handles)

            time.sleep(5)
            driver.find_element_by_xpath("/html/body/wx-view[1]/wx-view[1]/wx-view/wx-view[3]/wx-view[1]/wx-view[1]/wx-view").click()
            #                             /html/body/wx-view[1]/wx-view[1]/wx-view/wx-view[4]/wx-view[1]/wx-view[1]/wx-view
            #选择一个购物车商品类别

            unittest_TestResult = True
        except Exception as e:
            print ("进入购物车执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult