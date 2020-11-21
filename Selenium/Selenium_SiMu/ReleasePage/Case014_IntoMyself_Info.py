__author__ = 'TANUKI'

#coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class myself_info:
    def intomyself_info(driver):
        try:
            with allure.step('点击\"个人信息\"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/myself_info_tv", 20,2).click()
            time.sleep(3)
        except Exception as e:
            print("进入个人信息报错:", e)
            pass

    def myself_info_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为个人信息'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        if check.text == "个人信息":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        with allure.step('输出客户姓名'):
            username = Page.find_elem_id(driver,"com.chtwm.mall:id/user_info_tv_username")
            print("自动化校验客户姓名为：",username.text)
        with allure.step('输出客户编号'):
            userNO = Page.find_elem_id(driver,"com.chtwm.mall:id/user_info_tv_userjecno")
            print("自动化校验",userNO.text)
        with allure.step('输出客户注册手机号'):
            phone = Page.find_elem_id(driver,"com.chtwm.mall:id/user_info_tv_userjecno")
            print("自动化校验客户",phone.text)
        return pytest_TestResult