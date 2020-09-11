__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoMyself_tv:
    def IntoMyself_tv(driver):
        # 恒天财富APP进入我的页面
        try:
            time.sleep(6)
            # driver.wait_activity(".ui.LauncherUI", 30)
            #driver.implicitly_wait(10)
            #隐式等待，等待页面加载
            #ac = driver.current_activity
            #print (ac)
            #with allure.step('显式等待，元素为.activity.MainActivity'):
                #driver.wait_activity(".activity.MainActivity", 30)
            with allure.step('点击我的按钮'):
                #driver.find_element_by_id("com.chtwm.mall:id/myself_tv").click()
                Page.wait_elem(driver,"com.chtwm.mall:id/myself_tv", 120).click()
        except Exception as e:
            print("进入我的页面报错:", e)
            pass


    def IntoMyself_tv_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为我的'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/textView")
        if check.text == "我的":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult




    def ShowPage2(driver):
        time.sleep(2)
        with allure.step('我的页面上滑，显示交易明细等其他'):
            huadong.shanghua(driver,500)

