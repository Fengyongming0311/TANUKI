__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class IntoUserInfo:
    def IntoUserInfo(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            #先进行句柄的切换

            all_handles = driver.window_handles
            now_handle = driver.current_window_handle
            #print ("未切换handle且没进入修改昵称页面前的handle是:",now_handle)

            for i in all_handles:
                if i != now_handle:
                    UserInfo_handles = i
                    break

            driver.switch_to.window(UserInfo_handles)

            #now_handle2 = driver.current_window_handle
            #print("已切换handle但是没进入修改昵称页面前的handle是:", now_handle2)

            time.sleep(3)

            driver.find_element_by_css_selector("wx-view[class=\"headImage\"]").click()
            #<wx-view class="headImage" style="background-image:url(https://wx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEKlBoiaY1E9jKBZouGoMpLuiaM25lcVtgiakceBl7O8Z9uwq3x28wfXuC7zPDLRL1wC5iaZgPtEVuib8AQ/132)"></wx-view>
            total_handles = driver.window_handles
            print ("case31中的所有句柄",total_handles)
            now_handle2 = driver.current_window_handle

            ###这里在所有句柄中排除两个已经用过的句柄，选第三个然后切换到第三个句柄
            usedtwo_handle = []
            usedtwo_handle.append(now_handle)
            usedtwo_handle.append(now_handle2)

            for i in total_handles:
                if i not in usedtwo_handle:
                    userinfo_handle = i
                    break

            time.sleep(3)
            driver.switch_to.window(userinfo_handle)
            ###切换第三句柄完成(确实是第三个句柄...)


            time.sleep(3)
            #进行页面验证验证元素为退出登录按钮，如果页面有退出登录按钮说明进入页面成功
            #<wx-view class="Logout">退出登录</wx-view>
            #check = driver.find_element_by_css_selector("wx-view[class=\"Logout\"]")
            check = driver.find_element_by_xpath("/html/body/wx-view/wx-view[2]")


            if check.text == "退出登录":
                unittest_TestResult = True
            else:
                raise Exception("没有定位到退出登录按钮，CheckPoint验证失败")


            unittest_TestResult = True
        except Exception as e:
            print ("下单执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult