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
class UserInfoInvestor:
    #点击投资者分类认证
    def IntoUserInfoInvestor(driver):
        try:
            with allure.step('点击投资者分类认证'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_investor_ll", 27,3).click()
            with allure.step('%s检查点截图'%title):
                time.sleep(5)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
        except Exception as e:
            print("%s报错:"%title, e)
            allure.attach("%s报错:"%title, str(e),str(type(e)))
            with allure.step('用例失败%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %("IntoUserInfoInvestor失败报错",PrtScPath),attachment_type=allure.attachment_type.PNG)
                #添加用例失败检查点截图，PrtScPath为图片位置


    def UserInfoInvestor_CheckPoint(driver):
        #实在不行改为普通定位
        try:
            with allure.step('检查标题'):
                time.sleep(10)
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title2", 27,3)
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            with allure.step('输出客户姓名'):
                tv_name = Page.wait_elem(driver,"com.chtwm.mall:id/tv_name", 10)
                allure.attach("客户姓名：",tv_name.text)
                print ("客户姓名666：",tv_name.text)

            with allure.step('输出投资者类型'):
                tv_type = Page.wait_elem(driver,"com.chtwm.mall:id/tv_invest_type", 10)
                allure.attach("投资者类型：",tv_type.text)
                print ("投资者类型666：",tv_type.text)


        except Exception as e:
            print("检查点%s报错:"%title, e)
            allure.attach("检查点%s报错:"%title, str(e),str(type(e)))
            with allure.step('用例失败%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %("UserInfoInvestor_CheckPoint失败报错",PrtScPath),attachment_type=allure.attachment_type.PNG)
                #添加用例失败检查点截图，PrtScPath为图片位置
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def PROD_UserInfoInvestor_CheckPoint(driver):
        #实在不行改为普通定位
        try:
            with allure.step('检查标题'):
                time.sleep(10)
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title", 27,3)
                if check.text == "普通投资者认证":
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            with allure.step('输出客户姓名'):
                tv_name = Page.wait_elem(driver,"com.chtwm.mall:id/tv_name", 10)
                allure.attach("客户姓名：",tv_name.text)
                print ("客户姓名666：",tv_name.text)

            with allure.step('输出投资者类型'):
                tv_type = Page.wait_elem(driver,"com.chtwm.mall:id/tv_invest_type", 10)
                allure.attach("投资者类型：",tv_type.text)
                print ("投资者类型666：",tv_type.text)


        except Exception as e:
            print("检查点%s报错:"%title, e)
            allure.attach("检查点%s报错:"%title, str(e),str(type(e)))
            with allure.step('用例失败%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %("UserInfoInvestor_CheckPoint失败报错",PrtScPath),attachment_type=allure.attachment_type.PNG)
                #添加用例失败检查点截图，PrtScPath为图片位置
            pytest_TestResult = False
        finally:
            return pytest_TestResult











    def UserInfoInvestor_PageBack(driver):
        try:
            with allure.step('点击"返回上一页面"，返回到个人信息页面'):
                Page.wait_elem(driver,"com.chtwm.mall:id/iv_back_white", 10).click()
        except:
            driver.back()



