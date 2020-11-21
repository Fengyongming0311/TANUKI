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
from Case044_GMGroup import GMGroup
from Case045_GMDiagnose import GM_Diagnose
from Case046_SMChaoshi import SMChaoshi

class Test_HP_6Module:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_HP_6Module_001Login(self):
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
    @allure.feature('用例名称:APP首页→公募组合')
    def test_HP_6Module_002Into_GMGroup(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"公募组合"
        期望结果：
        进入公募组合页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = GMGroup.Into_GMGroup(driver)

        assert TestResult == True



    @pytest.mark.skip(reason="H5页面，不执行这条用例")
    @allure.feature('用例名称:APP首页→公募组合')
    def test_HP_6Module_003GMGroup(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"公募组合"
        期望结果：
        进入公募组合页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = GMGroup.GMGroup(driver)

        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→进入公募诊断')
    def test_HP_6Module_004Into_GMDiagnose(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"公募诊断"
        期望结果：
        进入公募诊断页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = GM_Diagnose.Into_GM_Diagnose(driver)

        assert TestResult == True



    @pytest.mark.skip(reason="H5页面，不执行这条用例")
    @allure.feature('用例名称:公募诊断→查看基金诊断')
    def test_HP_6Module_005GMDiagnose(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"公募诊断"
        期望结果：
        进入公募诊断页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = GM_Diagnose.GM_Diagnose(driver)

        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:APP首页→进入私募超市')
    def test_HP_6Module_006Into_SMchaoshi(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"私募超市"
        期望结果：
        进入私募超市页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = SMChaoshi.Into_SMChaoshi(driver)

        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:私募超市→查看产品详情')
    def test_HP_6Module_007Zhaiquaninvest(self):
        """
        """
        driver = Driver.driver
        TestResult = SMChaoshi.Zhaiquaninvest(driver)

        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_017_HP_6Module.py', "-s", "-v"])
