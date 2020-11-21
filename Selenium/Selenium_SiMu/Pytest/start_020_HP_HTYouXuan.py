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
from Case048_HTYouXuan import HTYouXuan

class Test_HTYouXuan:

    #@allure.feature('用例名称:登录恒天财富账号')
    def test_HTYouXuan_001Login(self):
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
    @allure.feature('用例名称:APP首页→进入恒天优选')
    def test_HTYouXuan_002Into_HTYouXuan(self):
        """
        """
        driver = Driver.driver
        TestResult = HTYouXuan.Into_HTYouXuan(driver)

        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:债权投资→智能排序')
    def test_HTYouXuan_003ZQCategory(self):
        """
        """
        driver = Driver.driver
        HTYouXuan.AllFund(driver)



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_020_HP_HTYouXuan.py', "-s", "-v"])