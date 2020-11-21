__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoSetting:
    def IntoSetting(driver):
        # 恒天财富APP进入设置页面
        try:
            with allure.step('点击设置按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/myself_set_img", 15).click()
        except Exception as e:
            print("点击设置按钮报错:", e)
            pass

    def IntoSetting_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为设置'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        if check.text == "设置":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult