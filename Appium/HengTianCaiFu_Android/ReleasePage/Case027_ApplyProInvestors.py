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
title = "普通投资者转专业投资者认证"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class ApplyProInvestors:
    def ApplyProInvestors(driver):
        try:
            with allure.step('上滑屏幕显示出申请转为专业投资者按钮'):
                time.sleep(5)
                huadong.shanghua(driver, 1000)

            with allure.step('点击申请转为专业投资者'):
                Page.wait_elem(driver,"com.chtwm.mall:id/zt_tv", 10).click()

            with allure.step('%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            with allure.step('确认普转专申请书'):
                Page.wait_elem(driver, "com.chtwm.mall:id/tv_confirm", 5).click()

        except Exception as e:
            print("%s报错:"%title, e)
            allure.attach("检查点%s报错:"%title, str(e),str(type(e)))
            with allure.step('用例失败%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加用例失败检查点截图，PrtScPath为图片位置


    def ProInvestors_CheckPoint(driver):
        try:
            with allure.step('检查标题'):
                time.sleep(5)
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title2", 10)
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            with allure.step('输出客户姓名'):
                tv_name = Page.wait_elem(driver,"com.chtwm.mall:id/tv_name", 10)
                print ("客户姓名print：",tv_name.text)
                allure.attach("客户姓名：",tv_name.text)

            with allure.step('输出投资者类型'):
                tv_type = Page.wait_elem(driver,"com.chtwm.mall:id/tv_invest_type", 10)
                print ("投资者类型print：",tv_type.text)
                allure.attach("投资者类型：",tv_type.text)

        except Exception as e:
            print("检查点%s报错:"%title, e)
            allure.attach("检查点%s报错:"%title, str(e),str(type(e)))
            with allure.step('用例失败%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加用例失败检查点截图，PrtScPath为图片位置
            pytest_TestResult = False
        finally:
            return pytest_TestResult




