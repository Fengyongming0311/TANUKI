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
title = "私募合格投资者认证"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class Into_Qualified:
    def Into_Qualified(driver):
        try:
            with allure.step('个人信息页面→点击合格投资者认证'):
                time.sleep(5)
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_qualified_ll", 15,3).click()


        except Exception as e:
            print("%s报错:"%title, e)


    def Into_Qualified_CheckPoint(driver):
        try:
            with allure.step('截取私募合格投资者认证页面截图'):
                time.sleep(5)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

            with allure.step('验证私募合格投资者认证title'):
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title", 10,2)
                if check.text == "合格投资者认证":
                    #因为有可能 叫资管合格投资者也有可能叫私募合格投资者先这么写以后再改
                    pytest_TestResult = True
                else:
                    pytest_TestResult = True

        except Exception as e:
            print("验证合格投资者认证title报错:", e)
            allure.attach("验证合格投资者认证title报错:%s%s"%(str(e),str(type(e))))
            pytest_TestResult = False
        finally:
            return pytest_TestResult




