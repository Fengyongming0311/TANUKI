__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class MyServices:
    def MyServices(driver, title):
        ############
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        PrtSc = now + title
        #屏幕截图名称
        PrtScPath = "../Screenshots/%s.png" %PrtSc
        ############
        try:
            with allure.step('我的→%s'%title):
                time.sleep(5)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/myself_item_tv")
                for i in elems:
                    if i.text == title:
                        i.click()
                        pytest_TestResult = True
                        break
            with allure.step("%s页面截图"%title):
                time.sleep(8)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)

            with allure.step("返回我的页面"):
                driver.back()

        except Exception as e:
            print("进入%s报错:"%title, e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


























































    def SimuAssetProve(driver):
        try:
            with allure.step('点击申请私募资产证明'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/sm_apply", 8).click()

            with allure.step('点击下载，下载资产证明到手机'):
                time.sleep(15)
                Page.find_elem_id(driver,"com.chtwm.mall:id/right_text").click()
                try:
                    with allure.step('资产证明发送到默认邮箱，点击确定'):
                        time.sleep(2)
                        Page.find_elem_id(driver,"com.chtwm.mall:id/tv_confirm").click()
                        time.sleep(3)
                except:
                    pass

            with allure.step("私募资产证明页面截图"):
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)

            with allure.step("上滑查看私募资产证明下一页"):
                huadong.shanghua(driver,500)

            with allure.step("返回上一页面"):
                driver.back()

            pytest_TestResult = True


        except Exception as e:
            print("查看%s报错:"%"私募"+title, e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult




    def GongMuAssetProve(driver):
        try:
            with allure.step('点击申请公募资产证明'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/gm_apply", 8).click()

            with allure.step('选择起始时间'):
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/start_data_select").click()
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/btnSubmit").click()

            with allure.step('选择结束时间'):
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/finish_data_select").click()
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/btnSubmit").click()


            with allure.step('点击提交申请'):
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/submit_apply").click()


            with allure.step('点击下载，下载资产证明到手机'):
                time.sleep(15)
                Page.find_elem_id(driver,"com.chtwm.mall:id/right_text").click()
                try:
                    with allure.step('资产证明发送到默认邮箱，点击确定'):
                        time.sleep(2)
                        Page.find_elem_id(driver,"com.chtwm.mall:id/tv_confirm").click()
                        time.sleep(3)
                except:
                    pass

            with allure.step("公募资产证明页面截图"):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)

            with allure.step("上滑查看公募资产证明下一页"):
                huadong.shanghua(driver,500)

            with allure.step("返回上一页面"):
                driver.back()

            pytest_TestResult = True


        except Exception as e:
            print("查看%s报错:"%"公募"+title, e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult