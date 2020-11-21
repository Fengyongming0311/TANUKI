__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoMyself_Equity:
    def IntoMyself_Equity(driver):
        #进入会员权益
        try:
            with allure.step('点击"查看权益"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/myself_equity", 10).click()
            time.sleep(3)
        except Exception as e:
            print("进入会员权益报错:", e)
            pass

    def IntoMyself_Equity_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为会员权益'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        if check.text == "会员权益":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult