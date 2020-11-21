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
from Case047_ZixuanJijin import ZixuanJijin

class Test_ZixuanJijin:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_ZixuanJijin_001Login(self):
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
    @allure.feature('用例名称:APP首页→进入自选基金')
    def test_ZixuanJijin_002Into_ZixuanJijin(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"自选基金"
        期望结果：
        进入自选基金页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = ZixuanJijin.Into_ZixuanJijin(driver)

        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:自选基金→查看全部基金')
    def test_ZixuanJijin_003CheckAllFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.AllFund(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:混合基金→查看混合基金')
    def test_ZixuanJijin_004MixFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"混合")
        ZixuanJijin.AllFund(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:股票基金→查看股票基金')
    def test_ZixuanJijin_005GuPiaoFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"股票")
        ZixuanJijin.AllFund(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:债券基金→查看债券基金')
    def test_ZixuanJijin_006ZQFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"债券")
        ZixuanJijin.AllFund(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:货币基金→查看货币基金')
    def test_ZixuanJijin_007HBFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"货币")
        ZixuanJijin.AllFund(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:商品基金→查看商品基金')
    def test_ZixuanJijin_008HBFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"货币")
        ZixuanJijin.AllFund(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:QDII基金→查看QDII基金')
    def test_ZixuanJijin_009QDIIFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"QDII")
        ZixuanJijin.AllFund(driver)



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:分级基金→查看分级基金')
    def test_ZixuanJijin_010FenJiFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"分级")
        ZixuanJijin.AllFund(driver)



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:FOF基金→查看FOF基金')
    def test_ZixuanJijin_011FOFFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"FOF")
        ZixuanJijin.AllFund(driver)



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_019_HP_ZixuanJijin.py', "-s", "-v"])
