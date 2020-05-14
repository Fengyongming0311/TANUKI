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
class ChangeUserName:
    def ChangeUserName(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)

            all_handles = driver.window_handles
            now_handle = driver.current_window_handle
            print ("所有句柄为",all_handles)
            print ("用户信息页面当前句柄为",now_handle)
            #先找出修改昵称页面的句柄，然后等点击进入修改昵称页面后再进行句柄切换
            changeusname = all_handles[3]
            print (changeusname)


            driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-view[2]").click()
            #/html/body/wx-view/wx-view[1]/wx-view[2]
            #点击昵称进入设置昵称页面

            time.sleep(3)

            #username_allhandles = driver.window_handles
            #print ("进入username后的全部句柄",username_allhandles)



            driver.switch_to.window(changeusname)

            time.sleep(3)

            driver.find_element_by_xpath("/html/body/wx-view/wx-input/div/div[1]").click()
            #/html/body/wx-view/wx-input/div/div[1]
            #/html/body/wx-view/wx-input/div/div[1]

            time.sleep(5)


            driver.find_element_by_xpath("/html/body/wx-view/wx-button").click()



            unittest_TestResult = True
        except Exception as e:
            print ("下单执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult