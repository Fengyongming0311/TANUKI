__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class HeGeTouZiZheRenZheng:
    #合格投资者认证申请须知
    def Application_Guide(driver):
        try:
            time.sleep(5)
            with allure.step('点击合格投资者认证申请须知'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_tip", 27, 3).click()
            time.sleep(5)
            with allure.step('下滑查看合格投资者须知内容'):
                huadong.shanghua(driver,1000)
            time.sleep(3)
            with allure.step("合格投资者认证须知页面截图"):
                allure.attach(driver.get_screenshot_as_png(),"合格投资者认证须知截图",attachment_type=allure.attachment_type.PNG)
            time.sleep(3)
            with allure.step("返回合格投资者认证页面"):
                Page.wait_elem(driver,"com.chtwm.mall:id/iv_back", 18, 3).click()

            pytest_TestResult = True

        except Exception as e:
            print("合格投资者认证申请须知页面报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def IntoSIMUTouZizhe(driver):
        try:
            time.sleep(5)
            with allure.step('点击私募合格投资者'):
                Page.wait_elem(driver,"com.chtwm.mall:id/cl_simu_qi", 27, 3).click()
            time.sleep(5)
            with allure.step('验证页面标题是否为私募合格投资者认证'):
                title = Page.wait_elem(driver,"com.chtwm.mall:id/tv_Title",16,2)
                #print ("开始验证！！！！！！！！！！！！！！！！！")
                #print ("验证页面标题是否为私募合格投资者认证title=====================",title.text)
                if title.text == "私募合格投资者认证":
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

        except Exception as e:
            print ("进入私募合格投资者认证报错：",e)
            #报错截图代码
            pytest_TestResult = False
        finally:
            return pytest_TestResult


    def IntoZIGUANTouZizhe(driver):
        try:
            time.sleep(5)
            with allure.step('点击资管合格投资者'):
                Page.wait_elem(driver,"com.chtwm.mall:id/cl_ziguan_qi", 27, 3).click()
            time.sleep(5)
            with allure.step('验证页面标题是否为资管合格投资者认证'):
                title = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title",10,2)
                if title.text == "资管合格投资者认证":
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

        except Exception as e:
            print ("进入资管合格投资者认证报错：",e)
            #报错截图代码
            pytest_TestResult = False
        finally:
            return pytest_TestResult


