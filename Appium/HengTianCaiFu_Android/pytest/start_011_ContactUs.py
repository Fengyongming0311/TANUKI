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
from Case039_ContactUs import ContactUs
from public import *



class Test_ContactUs:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_ContactUs_001Login(self):
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
    def test_ContactUs_002IntoMyself_tv(self):
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
    @allure.feature('用例名称:我的页面→点击联系我们')
    def test_ContactUs_003Into_ContactUs(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"联系我们"按钮
        期望结果：
        进入联系我们页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = ContactUs.Into_ContactUs(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:联系我们→官方微信号')
    def test_ContactUs_004OfficialWechat(self):
        """
        前置条件：
        页面处于联系我们
        测试步骤：
        1.点击"官方微信号"按钮
        期望结果：
        进入官方微信号
        检查点：
        检查标题，并截图
        测试后续步骤：
        返回联系我们页面
        """
        driver = Driver.driver
        TestResult = ContactUs.OfficialWechat(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:联系我们→客服热线')
    def test_ContactUs_005HotLine(self):
        """
        前置条件：
        页面处于联系我们
        测试步骤：
        1.点击"客服热线"按钮
        期望结果：
        进入客服热线
        检查点：
        截图查看电话号码
        测试后续步骤：
        返回联系我们页面
        """
        driver = Driver.driver
        TestResult = ContactUs.HotLine(driver)
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:联系我们→意见反馈')
    def test_ContactUs_006FeedBack(self):
        """
        前置条件：
        页面处于联系我们
        测试步骤：
        1.点击"意见反馈"按钮
        期望结果：
        进入意见反馈
        检查点：
        截图查看页面
        测试后续步骤：
        返回联系我们页面
        """
        driver = Driver.driver
        TestResult = ContactUs.FeedBack(driver)
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:联系我们→在线客服')
    def test_ContactUs_007OnlineService(self):
        """
        前置条件：
        页面处于联系我们
        测试步骤：
        1.点击"在线客服"按钮
        期望结果：
        进入在线客服
        检查点：
        截图查看页面
        测试后续步骤：
        返回联系我们页面
        """
        driver = Driver.driver
        TestResult = ContactUs.OnlineService(driver)
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_011_ContactUs.py', "-s", "-v"])
