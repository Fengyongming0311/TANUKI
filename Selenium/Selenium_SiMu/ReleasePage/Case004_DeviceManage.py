__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
sys.path.append("../Screenshots")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
title = "设备管理"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############


class DeviceManage:
    def DeviceManage(driver):
        # 恒天财富APP进入设备管理页面
        try:
            with allure.step('点击设备管理'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_devide_shebei", 15).click()
        except Exception as e:
            print("点击设备管理报错:", e)
            pass

    def DeviceManage_CheckPoint(driver):
        time.sleep(2)
        #driver.get_screenshot_as_file(PrtScPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
            #添加检查点截图，PrtScPath为图片位置
        with allure.step('验证标题为设备管理'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_above")
        if check.text == title:
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult

    def DeviceManage_PageBack(driver):
        try:
            with allure.step('点击返回按钮'):
                Page.find_elem_id(driver,"com.chtwm.mall:id/img_back").click()
        except:
            Page.wait_elem(driver,"com.chtwm.mall:id/img_back", 5).click()