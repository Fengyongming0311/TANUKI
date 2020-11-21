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
title = "风测揭示"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class IntoRiskTest:
    def IntoRiskTest(driver):
        try:
            with allure.step('点击重新评测'):
                Page.wait_elem(driver,"com.chtwm.mall:id/risk_result_reset_btn", 10).click()
                time.sleep(3)
                #等待3s页面加载评测题目

        except Exception as e:
            print("%s报错:"%title, e)

    #重新风测原因
    def Rerisk_Reason(driver):
        try:
            with allure.step('选择输入重新风测原因'):
                Page.wait_elem(driver,"com.chtwm.mall:id/two_checkbox", 21).click()
                time.sleep(5)
                #等待3s页面加载评测题目
            with allure.step('选择完风测原因，点击确认按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/confirm_tv", 21).click()
                time.sleep(3)


        except Exception as e:
            print("%s报错:"%title, e)


    def FengCeShuoMing_CheckPoint(driver):
        with allure.step('获取风险揭示说明内容'):
            check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_content", 10)
            print ("UI自动化获取风险揭示说明内容为：",check.text)
        with allure.step('风险揭示点击确定'):
            time.sleep(2)
            Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 10).click()
        return True