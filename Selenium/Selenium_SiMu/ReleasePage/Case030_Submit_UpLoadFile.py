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
title = "普通投资者转专业投资者认证提交总体数据"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class Submit_UpLoadFile:
    def PuZhuanZhuan_Submit(driver):
        try:
            with allure.step('点击立即提交'):
                time.sleep(5)
                Page.wait_elem(driver,"com.chtwm.mall:id/yes_tv", 120).click()
                #由于等待金融资产证明提交需要加长等待时间

            with allure.step('截取弹出短信页面截图'):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            with allure.step('点击获取验证码按钮'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_get_code", 5).click()

            with allure.step('输入短信验证码'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/et_input_code", 5).send_keys('000000')


            with allure.step('点击确认提交数据'):
                time.sleep(2)
                #Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 5).click()
                #TANUKIdondake

            #time.sleep(60)


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult



    def ZiGuan_Submit(driver):
        try:
            with allure.step('点击立即申请'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 60, 3).click()
                #由于等待金融资产证明提交需要加长等待时间

            with allure.step('截取弹出短信页面截图'):
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %now + "立即申请后页面截图",attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            with allure.step('点击获取验证码按钮'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_get_code", 5).click()

            with allure.step('输入短信验证码'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/et_input_code", 5).send_keys('000000')


            with allure.step('点击确认提交数据'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 5).click()

            #time.sleep(60)


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult



    def Prod_ZiGuan_Submit(driver):
        try:
            '''
            with allure.step('点击立即申请'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 60, 3).click()
                #由于等待金融资产证明提交需要加长等待时间
            '''

            with allure.step('截取弹出短信页面截图'):
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %now + "立即申请后页面截图",attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            with allure.step('点击获取验证码按钮'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_get_code", 5).click()

            with allure.step('输入短信验证码'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/et_input_code", 5).send_keys('000000')


            with allure.step('点击确认提交数据'):
                time.sleep(2)
                #Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 5).click()
                #TANUKIdondake

            #time.sleep(60)


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult

