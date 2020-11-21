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
from Case046_SMChaoshi import SMChaoshi
from Case053_IntoProduct_tv import IntoProduct_tv
from Case055_JiJinPaiHang import JiJinPaiHang
from Case047_ZixuanJijin import ZixuanJijin

class Test_LC_JiJinPaiHang:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_LC_JiJinPaiHang_001Login(self):
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
    @allure.feature('用例名称:打开恒天财富APP→进入理财页面')
    def test_LC_JiJinPaiHang_002IntoProduct_tv(self):
        """
        """
        driver = Driver.driver
        IntoProduct_tv.IntoProduct_tv(driver)
        #进入理财页面
        TestResult = IntoProduct_tv.IntoProduct_tv_CheckPoint(driver)
        #设置检查点验证进入我的成功com.chtwm.mall:id/product_tv
        assert TestResult == True







    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:理财页面→进入基金排行')
    def test_LC_JiJinPaiHang_003Into_JiJinPaiHang(self):
        """
        """
        driver = Driver.driver
        TestResult = JiJinPaiHang.Into_JiJinPaiHang(driver)

        assert TestResult == True





    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:混合基金→查看混合基金')
    def test_LC_JiJinPaiHang_004MixFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"混合")
        #ZixuanJijin.FundRanking(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:股票基金→查看股票基金')
    def test_LC_JiJinPaiHang_005GuPiaoFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"股票")
        #ZixuanJijin.FundRanking(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:债券基金→查看债券基金')
    def test_LC_JiJinPaiHang_006ZQFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"债券")
        #ZixuanJijin.FundRanking(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:货币基金→查看货币基金')
    def test_LC_JiJinPaiHang_007HBFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"货币")
        #ZixuanJijin.FundRanking(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:商品基金→查看商品基金')
    def test_LC_JiJinPaiHang_008HBFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"货币")
        #ZixuanJijin.FundRanking(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:QDII基金→查看QDII基金')
    def test_LC_JiJinPaiHang_009QDIIFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"QDII")
        #ZixuanJijin.FundRanking(driver)



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:分级基金→查看分级基金')
    def test_LC_JiJinPaiHang_010FenJiFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"分级")
        #ZixuanJijin.FundRanking(driver)



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:FOF基金→查看FOF基金')
    def test_LC_JiJinPaiHang_011FOFFund(self):
        """
        """
        driver = Driver.driver
        ZixuanJijin.Switch_Category(driver,"FOF")
        #ZixuanJijin.FundRanking(driver)




if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_024_LC_JiJinPaiHang.py', "-s", "-v"])