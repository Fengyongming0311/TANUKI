__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoAbout:
    def IntoAbout(driver):
        # 恒天财富APP进入关于页面
        try:
            with allure.step('点击设置按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/lin_above", 10).click()
        except Exception as e:
            print("进入关于报错:", e)
            pass

    def IntoAbout_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题为关于'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_above")
        if check.text == "关于":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult