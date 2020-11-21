#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")

from public import *


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case001_Login import Login
from Case053_IntoProduct_tv import IntoProduct_tv
from Case056_NewFund import NewFund
from Case049_SMTuiJian import SMTuiJian
from Case050_GMTuiJian import GMTuiJian

class Test_SH_FourList:

    #@allure.feature('用例名称:登录恒天财富账号')
    def test_SH_FourList_001Login(self):
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
    @allure.feature('用例名称:打开恒天财富APP→进入理财页面')
    def test_SH_FourList_002IntoProduct_tv(self):
        """
        """
        driver = Driver.driver
        IntoProduct_tv.IntoProduct_tv(driver)
        #进入理财页面
        TestResult = IntoProduct_tv.IntoProduct_tv_CheckPoint(driver)
        #设置检查点验证进入我的成功com.chtwm.mall:id/product_tv
        assert TestResult == True




    @pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:理财页面→进入新发基金')
    def test_SH_FourList_003NewFund(self):
        """
        """
        driver = Driver.driver
        TestResult = NewFund.Into_NewFund(driver)
        NewFund.ClickFund(driver)
        assert TestResult == True





    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:理财页面→优选产品')
    def test_SH_FourList_004PreferredProducts(self):
        """
        """
        driver = Driver.driver
        TestResult = SMTuiJian.Into_SMTuiJian(driver)

        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:理财页面→公募推荐')
    def test_SH_FourList_005GMTuiJian(self):
        """
        """
        driver = Driver.driver
        TestResult = GMTuiJian.LC_GMTuiJian(driver)

        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_028_SH_FourList.py', "-s", "-v"])
