#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")
from appium import webdriver


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case001_Login import Login
from Case046_SMChaoshi import SMChaoshi
from public import *

class Test_SMChaoshiCategory:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_SMChaoshiCategory_001Login(self):
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
    @allure.feature('用例名称:APP首页→进入私募超市')
    def test_SMChaoshiCategory_002Into_SMchaoshi(self):
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
    @allure.feature('用例名称:债权投资→智能排序')
    def test_SMChaoshiCategory_003ZQCategory(self):
        """
        """
        driver = Driver.driver
        SMChaoshi.ZQCategory(driver,"按业绩比较基准")
        SMChaoshi.ZQCategory(driver,"按产品期限")
        SMChaoshi.ZQCategory(driver,"按起投金额")


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:股权投资→智能排序')
    def test_SMChaoshiCategory_004GQCategory(self):
        """
        """
        driver = Driver.driver
        SMChaoshi.Switch_Category(driver,"股权投资")
        SMChaoshi.ZQCategory(driver,"按业绩比较基准")
        SMChaoshi.ZQCategory(driver,"按产品期限")
        SMChaoshi.ZQCategory(driver,"按起投金额")


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:证券投资→智能排序')
    def test_SMChaoshiCategory_005ZhengQCategory(self):
        """
        """
        driver = Driver.driver
        SMChaoshi.Switch_Category(driver,"证券投资")
        SMChaoshi.ZQCategory(driver,"按业绩比较基准")
        SMChaoshi.ZQCategory(driver,"按产品期限")
        SMChaoshi.ZQCategory(driver,"按起投金额")


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:其他→智能排序')
    def test_SMChaoshiCategory_006QiTaCategory(self):
        """
        """
        driver = Driver.driver
        SMChaoshi.Switch_Category(driver,"其他")
        SMChaoshi.ZQCategory(driver,"按业绩比较基准")
        SMChaoshi.ZQCategory(driver,"按产品期限")
        SMChaoshi.ZQCategory(driver,"按起投金额")


if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_019_HP_SMChaoshiCategory.py', "-s", "-v"])
