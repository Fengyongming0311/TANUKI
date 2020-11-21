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
title = "绑定邮箱"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class IntoUserinfo_Myemail:
    def IntoUserinfo_Myemail(driver):
        try:
            with allure.step('点击"我的邮箱"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_my_email_ll", 10).click()
            time.sleep(3)
        except Exception as e:
            print("进入我的邮箱报错:", e)
            pass

    def IntoUserinfo_Myemail_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为%s'%title):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        if check.text == title:
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult