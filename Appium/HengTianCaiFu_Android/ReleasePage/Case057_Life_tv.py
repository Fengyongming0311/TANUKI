__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoProduct_tv:
    def IntoProduct_tv(driver):
        # 恒天财富APP进入理财页面
        try:
            time.sleep(3)
            with allure.step('点击理财按钮'):
                #driver.find_element_by_id("com.chtwm.mall:id/myself_tv").click()
                Page.wait_elem(driver,"com.chtwm.mall:id/product_tv", 120).click()
        except Exception as e:
            print("进入理财页面报错:", e)
            pass


    def IntoProduct_tv_CheckPoint(driver):
        time.sleep(5)
        with allure.step('验证标题是否为理财'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_lc")
        if check.text == "理财":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult




    def ShowPage2(driver):
        time.sleep(2)
        with allure.step('我的页面上滑，显示交易明细等其他'):
            huadong.shanghua(driver,500)

