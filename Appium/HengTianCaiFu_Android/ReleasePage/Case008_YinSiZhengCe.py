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
title = "隐私权政策协议"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############

class YinSiZhengCe:
    def IntoYinSiZhengCe(driver):
        #进入隐私政策
        try:
            with allure.step('点击隐私政策进入隐私政策页面'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_ys", 10).click()
        except Exception as e:
            print("进入隐私政策报错:", e)
            pass

    def YinSiZhengCe_CheckPoint(driver):
        time.sleep(8)
        #
        with allure.step('上滑查看隐私政策协议内容'):
            huadong.shanghua(driver,800)
        time.sleep(1)
        with allure.step('左滑查看页面是否偏移'):
            huadong.zuohua(driver,1000)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
        pytest_TestResult = True
        return pytest_TestResult

    def YinSiZhengCe_PageBack(driver):
        try:
            with allure.step('点击"返回上一页面"，返回到关于页面'):
                driver.back()
        except:
            Page.find_elem_id(driver,"goBack").click()



