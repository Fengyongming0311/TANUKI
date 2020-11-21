__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class MarketImg:
    def MarketImg(driver):
        try:
            with allure.step('首页→上滑，显示活动资讯'):
                time.sleep(3)
                huadong.shanghua(driver, 10000)

                time.sleep(3)
            with allure.step('查看活动资讯'):
                Page.find_elem_id(driver,"com.chtwm.mall:id/item_market_img").click()
                time.sleep(3)
                driver.back()


            pytest_TestResult = True

        except Exception as e:
            print("活动资讯报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult

    def tv_welth(driver):
        try:
            with allure.step('查看财富学院'):
                time.sleep(5)
                Page.find_elem_id(driver,"com.chtwm.mall:id/tv_welth").click()
                time.sleep(3)
                driver.back()


            pytest_TestResult = True

        except Exception as e:
            print("活动资讯报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult

