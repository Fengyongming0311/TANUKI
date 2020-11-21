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
title = "输入新邮箱"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class IntoChangeEmail:
    def IntoChangeEmail(driver):
        try:
            with allure.step('点击"修改邮箱"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/current_email_submit_tv", 10).click()
            time.sleep(3)
        except Exception as e:
            print("进入修改邮箱页面报错:", e)
            pass

    def IntoChangeEmail_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为%s'%title):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        with allure.step('%s检查点截图'%title):
            allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
            #添加检查点截图，PrtScPath为图片位置
        if check.text == title:
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult