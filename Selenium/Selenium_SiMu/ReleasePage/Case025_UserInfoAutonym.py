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
title = "身份信息"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class Autonym:
    def IntoAutonym(driver):
        try:
            with allure.step('点击身份认证'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_autonym_ll", 10).click()
            with allure.step('%s检查点截图'%title):
                time.sleep(5)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
        except Exception as e:
            print("%s报错:"%title, e)


    def Autonym_CheckPoint(driver):
        try:
            with allure.step('检查标题'):
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title", 10)

                print ("输出标题内容为..................",check.text)

                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            with allure.step('输出客户姓名'):
                tv_name = Page.wait_elem(driver,"com.chtwm.mall:id/tv_name", 10)
                print ("客户姓名：",tv_name.text)
            with allure.step('输出证件类型'):
                tv_type = Page.wait_elem(driver,"com.chtwm.mall:id/tv_type", 10)
                print ("证件类型：",tv_type.text)
            with allure.step('输出证件号码'):
                tv_birthdate = Page.wait_elem(driver,"com.chtwm.mall:id/tv_birthdate", 10)
                print ("证件号码：",tv_birthdate.text)
        except Exception as e:
            print("检查点%s报错:"%title, e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def Autonym_PageBack(driver):
        try:
            with allure.step('点击"返回上一页面"，返回到个人信息页面'):
                Page.wait_elem(driver,"com.chtwm.mall:id/iv_back", 10).click()
        except:
            driver.back()



