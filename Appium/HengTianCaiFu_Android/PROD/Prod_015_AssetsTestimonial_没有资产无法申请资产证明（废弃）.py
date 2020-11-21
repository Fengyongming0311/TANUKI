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
from Case002_IntoMyself_tv import IntoMyself_tv
from Case042_AssetProve import AssetProve
from public import *


class Test_AssetsTestimonial:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_AssetsTestimonial_001Login(self):
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
    @allure.feature('用例名称:打开恒天财富APP→进入我的页面')
    def test_AssetsTestimonial_002IntoMyself_tv(self):
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
    @allure.feature('用例名称:我的页面→进入资产证明')
    def test_AssetsTestimonial_003Into_AssetsProve(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"资产证明"按钮
        期望结果：
        进入资产证明页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = AssetProve.Into_AssetProve(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:私募申请资产证明')
    def test_AssetsTestimonial_004SimuAssetProve(self):
        """
        前置条件：
        页面处于申请资产证明
        测试步骤：
        1.点击私募的申请资产证明按钮
        2.生成私募资产证明
        3.点击下载，将私募资产证明下载到手机中
        4.对资产证明页面进行截图
        5.向上滑动查看资产证明内容
        测试后续步骤：
        返回申请资产证明页面
        """
        driver = Driver.driver
        TestResult = AssetProve.SimuAssetProve(driver)
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:公募申请资产证明')
    def test_AssetsTestimonial_005GongMuAssetProve(self):
        """
        前置条件：
        页面处于申请资产证明
        测试步骤：
        1.点击公募的申请资产证明按钮
        2.选择起始时间，选择终止时间
        3.点击提交
        4.生成公募资产证明
        5.点击下载，将公募资产证明下载到手机中
        6.对资产证明页面进行截图
        7.向上滑动查看资产证明内容
        测试后续步骤：
        返回申请资产证明页面
        """
        driver = Driver.driver
        TestResult = AssetProve.GongMuAssetProve(driver)
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_015_AssetsTestimonial.py', "-s", "-v"])