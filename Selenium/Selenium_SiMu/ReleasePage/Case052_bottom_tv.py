__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class bottom_tv:
    def bottom(driver):
        try:
            with allure.step('首页→上滑，显示底部'):
                time.sleep(10)
                huadong.shanghua(driver, 600)
                time.sleep(2)
                huadong.shanghua(driver, 600)
                time.sleep(2)
                huadong.shanghua(driver, 600)
                time.sleep(2)
                huadong.shanghua(driver, 600)

        except Exception as e:
            print("显示底部报错:", e)




    def grid_item(driver, title):
        try:
            with allure.step('查看%s'%title):
                time.sleep(3)
                elems = driver.find_elements_by_id("com.chtwm.mall:id/grid_item_title")
                for i in elems:
                    if i.text == title:
                        i.click()
                        time.sleep(3)
                        huadong.shanghua(driver, 600)
                        time.sleep(3)
                        with allure.step('%s界面截图'%title):
                            allure.attach(driver.get_screenshot_as_png(),'%s界面截图'%title,attachment_type=allure.attachment_type.PNG)
                        pytest_TestResult = True
                        break
                time.sleep(3)
                driver.back()



        except Exception as e:
            print("活动资讯报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult

