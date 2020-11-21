__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
import random
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
title = "风险测评"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class StartRiskTest:
    def Select_Risk_4Answers(driver):
        try:
            with allure.step('随机选择风测答案'):
                risk_answers = driver.find_elements_by_id("com.chtwm.mall:id/card_view")
                #获取所有四个题目
                select = risk_answers[random.randint(0,3)]
                time.sleep(2)
                select.click()
                time.sleep(2)

        except Exception as e:
            print("%s报错:"%title, e)

    def Select_Risk_3Answers(driver):
        try:
            with allure.step('随机选择风测答案'):
                risk_answers = driver.find_elements_by_id("com.chtwm.mall:id/card_view")
                #获取所有四个题目
                select = risk_answers[random.randint(0,2)]
                time.sleep(2)
                select.click()
                time.sleep(2)

        except Exception as e:
            print("%s报错:"%title, e)

    def Select_Risk_Q10(driver):
        try:
            with allure.step('第十题选择内容为第四题'):
                risk_answers = driver.find_elements_by_id("com.chtwm.mall:id/card_view")
                #获取所有四个题目
                select = risk_answers[3]
                time.sleep(2)
                select.click()
                time.sleep(2)

        except Exception as e:
            print("%s报错:"%title, e)


    def fin(driver):
        try:
            with allure.step('风险评测结果，点击查看详情，进入账户页面'):
                time.sleep(5)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm",21,3).click()


        except Exception as e:
            print("%s报错:"%title, e)
            with allure.step('风险评测结果，点击我知道了'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_cancle",21,3).click()
        finally:
            with allure.step('风测结果截图'):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)



