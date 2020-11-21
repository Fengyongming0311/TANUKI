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
title = "基本信息"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class Basic_Information:
    def IntoBasic_Information(driver):
        try:
            with allure.step('点击"基本信息"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_basic_information_tv", 10).click()
            time.sleep(3)
        except Exception as e:
            print("进入基本信息报错:", e)
            pass

    def Basic_Information_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为%s'%title):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        with allure.step('添加基本信息检查点截图_第一页'):
            allure.attach(driver.get_screenshot_as_png(),'%s_1' %PrtScPath,attachment_type=allure.attachment_type.PNG)
            #添加检查点截图，PrtScPath为图片位置
        huadong.shanghua(driver,500)
        with allure.step('添加基本信息检查点截图_第二页'):
            allure.attach(driver.get_screenshot_as_png(),'%s_2' %PrtScPath,attachment_type=allure.attachment_type.PNG)
            #添加检查点截图，PrtScPath为图片位置
        if check.text == title:
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult

    def Basic_Information_PageBack(driver):
        try:
            with allure.step('点击"返回上一页面"，返回到个人信息页面'):
                Page.find_elem_id(driver,"com.chtwm.mall:id/iv_back").click()
        except:
            driver.back()
