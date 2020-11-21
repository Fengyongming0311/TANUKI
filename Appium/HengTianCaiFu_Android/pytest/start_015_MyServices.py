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
from Case002_IntoMyself_tv import IntoMyself_tv
from Case043_MyServices import MyServices


class Test_MyServices:

    #@allure.feature('用例名称:登录恒天财富账号')
    def test_MyServices_001Login(self):
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
        userid = '13093110000'
        psw = 'aa1234'
        driver = Driver.driver
        TestResult = Login.Login(driver, userid, psw)
        #登录恒天财富账号
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:打开恒天财富APP→进入我的页面')
    def test_MyServices_002IntoMyself_tv(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"我的"按钮
        期望结果：
        进入我的页面
        检查点：
        验证标题是否为我的
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoMyself_tv.IntoMyself_tv(driver)
        #进入我的页面
        TestResult = IntoMyself_tv.IntoMyself_tv_CheckPoint(driver)
        #设置检查点验证进入我的成功
        IntoMyself_tv.ShowPage2(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→基金账户诊断')
    def test_MyServices_003Account_Diagnosis(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"基金账户诊断"按钮
        期望结果：
        进入基金账户诊断页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = MyServices.MyServices(driver,"基金账户诊断")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→已报名活动')
    def test_MyServices_004Registered_Event(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"已报名活动"按钮
        期望结果：
        进入已报名活动页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = MyServices.MyServices(driver,"已报名活动")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→公募监管账户')
    def test_MyServices_005Regulatory_Account(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"公募监管账户"按钮
        期望结果：
        进入公募监管账户页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = MyServices.MyServices(driver,"公募监管账户")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→我的奖励')
    def test_MyServices_006Rewards(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"我的奖励"按钮
        期望结果：
        进入我的奖励页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = MyServices.MyServices(driver,"我的奖励")
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_015_MyServices.py', "-s", "-v"])
