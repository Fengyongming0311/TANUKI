__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class Orders:
    #管理商品→勾选商品→下单
    def Orders(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)

            driver.find_element_by_css_selector("wx-view[class=\"cart_pay\"]").click()
            #<wx-view class="cart_pay" data-id="undefined">下单(2)</wx-view>
            #点击下单

            unittest_TestResult = True
        except Exception as e:
            print ("下单执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult