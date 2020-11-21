#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")
from appium import webdriver

from public import *

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case001_Login import Login
from Case052_bottom_tv import bottom_tv


class Test_Bottom_tv:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_Bottom_tv_001Login(self):
        """
        前置条件：
        安装恒天财富APP
        测试步骤：
        1.Appium启动恒天财富APP
        2.如未直接进入登陆页面，则在首页点击"登录"按钮
        3.输入自然人的11位手机号(账号)
        4.输入登陆密码
        5.点击登录按钮
        期望结果：
        登录成功，页面跳转到首页
        检查点：
        无
        测试后续步骤：
        无
        """
        userid = '13263160105'
        psw = 'aa1234'
        driver = Driver.driver
        TestResult = Login.Login(driver, userid, psw)
        #登录恒天财富账号
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→了解恒天→公司简介')
    def test_Bottom_tv_002CompanyInfo(self):
        """
        """
        driver = Driver.driver
        bottom_tv.bottom(driver)
        TestResult = bottom_tv.grid_item(driver, "公司简介")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→了解恒天→公司荣誉')
    def test_Bottom_tv_003CompanyCredit(self):
        """
        """
        driver = Driver.driver
        TestResult = bottom_tv.grid_item(driver, "公司荣誉")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→了解恒天→风险管理')
    def test_Bottom_tv_004RiskControlSystem(self):
        """
        """
        driver = Driver.driver
        TestResult = bottom_tv.grid_item(driver, "风险管理")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→了解恒天→平台资质')
    def test_Bottom_tv_005Licence(self):
        """
        """
        driver = Driver.driver
        TestResult = bottom_tv.grid_item(driver, "平台资质")
        assert TestResult == True




if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_021_HP_Bottom_tv.py', "-s", "-v"])
