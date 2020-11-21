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
title = "官方微信号"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
title2 = "客服热线"
PrtSc2 = now + title2
PrtScPath2 = "../Screenshots/%s.png" %PrtSc2
############
title3 = "意见反馈"
PrtSc3 = now + title3
PrtScPath3 = "../Screenshots/%s.png" %PrtSc3
############
title4 = "在线客服"
PrtSc4 = now + title4
PrtScPath4 = "../Screenshots/%s.png" %PrtSc4
############

class ContactUs:
    def Into_ContactUs(driver):
        try:
            with allure.step('我的→联系我们'):
                time.sleep(3)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/myself_item_tv")
                for i in elems:
                    #print (i.text)
                    if i.text == "联系我们":
                        i.click()
                        pytest_TestResult = True
                        break

        except Exception as e:
            print("进入联系我们报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def OfficialWechat(driver):
        try:
            with allure.step('联系我们→官方微信号'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/ll_authority_wechat",8).click()
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
            with allure.step('判断页面元素标题是否正确'):
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title", 10)
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            driver.back()
        except Exception as e:
            print("%s报错:"%title, e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult



    def HotLine(driver):
        try:
            with allure.step('联系我们→客服热线'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/ll_hot_line",8).click()
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath2,attachment_type=allure.attachment_type.PNG)
                pytest_TestResult = True
                driver.back()
                driver.back()

        except Exception as e:
            print("%s报错:"%title2, e)
            pytest_TestResult = False
            driver.back()

        finally:
            return pytest_TestResult



    def FeedBack(driver):
        #H5页面目前无法自动化
        try:
            with allure.step('联系我们→意见反馈'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/ll_feed_back",8).click()
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath3,attachment_type=allure.attachment_type.PNG)
                pytest_TestResult = True
                driver.back()

        except Exception as e:
            print("%s报错:"%title3, e)
            pytest_TestResult = False
            driver.back()

        finally:
            return pytest_TestResult



    def OnlineService(driver):
        #H5页面目前无法自动化
        try:
            with allure.step('联系我们→在线客服'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/ll_online_service",8).click()
                time.sleep(10)
                driver.tap([(48,2210)])
                time.sleep(3)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath4,attachment_type=allure.attachment_type.PNG)
                pytest_TestResult = True
                driver.back()

        except Exception as e:
            print("%s报错:"%title4, e)
            pytest_TestResult = False
            driver.back()

        finally:
            return pytest_TestResult