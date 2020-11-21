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
title = "公募产品"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class IntoGongMuProduct:
    def IntoGongMuProduct(driver):
        try:
            with allure.step('私募合格投资者认证→点击公募产品'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_button_left", 15).click()


        except Exception as e:
            print("%s报错:"%title, e)


    def IntoGongMuProduct_CheckPoint(driver):
        try:
            with allure.step('截取公募产品页面截图'):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            pytest_TestResult = True


        except Exception as e:

            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
        finally:
            return pytest_TestResult

    def IntoGongMuProduct_Back(driver):
        try:
            Page.wait_elem(driver,"com.chtwm.mall:id/miv_back", 15).click()
        except:
            driver.back()




