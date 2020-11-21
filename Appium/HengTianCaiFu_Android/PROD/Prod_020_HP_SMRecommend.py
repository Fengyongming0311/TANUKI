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
from Case049_SMTuiJian import SMTuiJian
from Case050_GMTuiJian import GMTuiJian
from Case051_MarketImg import MarketImg


class Test_SMRecommend:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_SMRecommend_001Login(self):
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
    @allure.feature('用例名称:APP首页→进入私募推荐')
    def test_SMRecommend_002SMRecommend(self):
        """
        """
        driver = Driver.driver
        TestResult = SMTuiJian.Into_SMTuiJian(driver)

        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→进入公募推荐')
    def test_SMRecommend_003GMRecommend(self):
        """
        """
        driver = Driver.driver
        TestResult = GMTuiJian.Prod_HP_JingXuanGM(driver)

        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→活动市场')
    def test_SMRecommend_004MarketImg(self):
        """
        """
        driver = Driver.driver
        TestResult = MarketImg.MarketImg(driver)

        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→财富学院')
    def test_SMRecommend_005tv_welth(self):
        """
        """
        driver = Driver.driver
        TestResult = MarketImg.tv_welth(driver)

        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_020_HP_SMRecommend.py', "-s", "-v"])
