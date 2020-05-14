__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append("..")



############################################
class MyOrder:
    def MyOrder(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)

            all_handles = driver.window_handles
            now_handle = driver.current_window_handle
            # print ("未切换handle且没进入修改昵称页面前的handle是:",now_handle)

            for i in all_handles:
                if i != now_handle:
                    WoDe_handles = i
                    break

            driver.switch_to.window(WoDe_handles)

            time.sleep(3)
            driver.find_element_by_css_selector("wx-view[data-paystate=\"1\"]").click()
            #<wx-view data-paystate="1"><wx-image src="../../images/obligation.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/obligation.png&quot;);"></div><span></span></wx-image><wx-view class="msg">待付款</wx-view></wx-view>



            unittest_TestResult = True
        except Exception as e:
            print ("下单执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult