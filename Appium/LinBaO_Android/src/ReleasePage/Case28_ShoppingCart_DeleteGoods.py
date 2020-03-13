__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class DeleteGoods:
    #管理商品→删除商品
    def DeleteGoods(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)

            driver.find_element_by_css_selector("wx-view[class=\"management\"]").click()
            #<wx-view class="management">管理</wx-view>
            #选择完商品后，点击管理
            time.sleep(5)

            driver.find_element_by_xpath("/html/body/wx-view[1]/wx-view[2]/wx-view[2]/wx-view").click()
            #/html/body/wx-view[1]/wx-view[2]/wx-view[2]/wx-view
            #点击删除按钮
            time.sleep(5)

            #切换上下文到NATIVE_APP
            try:
                driver.switch_to.context('NATIVE_APP')
                print("当前上下文================>", driver.current_context)
            except:
                pass

            time.sleep(5)
            driver.find_element_by_id("com.tencent.mm:id/b49").click()
            #确认删除，选择确定

            unittest_TestResult = True
        except Exception as e:
            print ("选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult