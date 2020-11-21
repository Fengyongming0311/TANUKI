__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class GMTuiJian:
    def Into_GMTuiJian(driver):
        try:
            with allure.step('首页→上滑，显示公募推荐'):
                time.sleep(8)
                huadong.shanghua(driver, 5300)

                time.sleep(3)
            with allure.step('查看公募推荐'):
                Page.find_elem_id(driver,"com.chtwm.mall:id/item_tv").click()
                time.sleep(3)
                driver.back()


            pytest_TestResult = True

        except Exception as e:
            print("进入公募推荐报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult

    #首页精选公募
    def Prod_HP_JingXuanGM(driver):
        try:
            with allure.step('首页→上滑，显示公募推荐'):
                time.sleep(8)
                huadong.shanghua(driver, 5300)

                time.sleep(3)
            with allure.step('查看公募推荐'):
                try:
                    GM = driver.find_elements_by_id("com.chtwm.mall:id/item_title_tv")
                    #获取所有公募元素
                    #查看公募推荐1
                    time.sleep(3)
                    GM[0].click()
                    time.sleep(8)
                    with allure.step('公募推荐1界面截图'):
                        allure.attach(driver.get_screenshot_as_png(),'公募推荐1界面截图',attachment_type=allure.attachment_type.PNG)
                        #添加检查点截图，PrtScPath为图片位置
                    driver.back()

                    #查看公募推荐2
                    time.sleep(3)
                    GM2 = driver.find_elements_by_id("com.chtwm.mall:id/item_title_tv")
                    #获取所有公募元素
                    GM2[1].click()
                    time.sleep(8)
                    with allure.step('公募推荐2界面截图'):
                        allure.attach(driver.get_screenshot_as_png(),'公募推荐2界面截图',attachment_type=allure.attachment_type.PNG)
                        #添加检查点截图，PrtScPath为图片位置
                    driver.back()

                except:
                    pass



            pytest_TestResult = True

        except Exception as e:
            print("进入公募推荐报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult



    def LC_GMTuiJian(driver):
        try:
            with allure.step('理财→上滑，显示公募推荐'):
                time.sleep(8)
                huadong.shanghua(driver, 300)
                time.sleep(3)
            with allure.step('查看智慧盈公募'):
                Page.wait_elem(driver,"com.chtwm.mall:id/type_three_ll",18,3).click()
                time.sleep(8)
                huadong.shanghua(driver, 300)
                time.sleep(3)
                huadong.shanghua(driver, 300)
                time.sleep(3)
                driver.back()


            with allure.step("查看稳鑫盈公募"):
                time.sleep(8)
                elms2 = driver.find_elements_by_id("com.chtwm.mall:id/item_ha_than_tv")
                for i in elms2:
                    if i.text == "稳鑫盈":
                        i.click()
                        time.sleep(8)
                        huadong.shanghua(driver, 300)
                        time.sleep(3)
                        huadong.shanghua(driver, 300)
                        time.sleep(3)
                        driver.back()

            pytest_TestResult = True

        except Exception as e:
            print ("查看公募推荐模块报错：",e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult



