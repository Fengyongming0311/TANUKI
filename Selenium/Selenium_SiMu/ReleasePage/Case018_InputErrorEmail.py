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
title = "输入邮箱内容"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class InputEmail:
    def InputErrorEmail(driver, ErrorEmail):
        try:
            with allure.step('输入错误邮箱内容'):
                Page.wait_elem(driver,"com.chtwm.mall:id/change_email_input_et", 10).send_keys(ErrorEmail)
            with allure.step('点击提交'):
                Page.wait_elem(driver,"com.chtwm.mall:id/change_email_submit_tv", 10).click()
            with allure.step('点击确认修改'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 10).click()
            time.sleep(1)
            with allure.step('%s检查点截图'%title):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
            return True
        except Exception as e:
            print("修改邮箱报错:", e)
            return False

    def InputRightEmail(driver, RightEmail):
        try:
            with allure.step('输入符合规格邮箱内容'):
                Page.wait_elem(driver,"com.chtwm.mall:id/change_email_input_et", 10).send_keys(RightEmail)
            with allure.step('点击提交'):
                Page.wait_elem(driver,"com.chtwm.mall:id/change_email_submit_tv", 10).click()
            with allure.step('点击确认修改'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 10).click()
            time.sleep(1)
            with allure.step('%s检查点截图'%title):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置
            with allure.step('显示发送邮件提示信息'):
                content = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_content")
                print (content.text)
        except Exception as e:
            print("修改正确邮箱报错:", e)


    def InputRightEmail_CheckPoint(driver):
        try:
            with allure.step('点击确认（明白了）'):
                confirm = Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 10)
                if confirm.text == "明白了":
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
                confirm.click()
        except Exception as e:
            print("二次确认报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult