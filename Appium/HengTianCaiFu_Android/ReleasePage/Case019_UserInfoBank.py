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
title = "银行卡"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class UserInfoBank:
    def IntoUserInfoBank(driver):
        try:
            with allure.step('进入银行卡页面'):
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_bank_ll", 10).click()
            with allure.step('%s检查点截图'%title):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
            return True
        except Exception as e:
            print("银行卡报错:", e)
            return False

    def Bank_PageBack(driver):
        try:
            with allure.step('点击"返回上一页面"，返回到个人信息页面'):
                Page.wait_elem(driver,"com.chtwm.mall:id/bankcard_back_img", 10).click()
        except:
            driver.back()