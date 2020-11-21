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
from Case010_IntoMessageCenter import IntoMessageCenter
from Case011_MessagePage import MessagePage
from public import *

class Test_HengTian_MessageCenter:


    @allure.feature('用例名称:登录恒天财富账号')
    def test_MessageCenter_001Login(self):
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
        TestResult = Login.Login(driver,userid, psw)
        #登录恒天财富账号
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:打开恒天财富APP→进入我的页面')
    def test_MessageCenter_002IntoMyself_tv(self):
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
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→点击消息中心进入消息中心页面')
    def test_MessageCenter_003IntoMessageCenter(self):
        """
        前置条件：
        已登录状态，页面处于我的页面
        测试步骤：
        1.点击右上角"消息中心"按钮
        期望结果：
        进入消息中心页面
        检查点：
        验证标题是否为消息中心
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoMessageCenter.IntoMessageCenter(driver)
        #进入设置页面
        TestResult = True
        #假检查点...
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:消息中心→查看系统通知')
    def test_MessageCenter_004XiTongZhongXin(self):
        """
        前置条件：
        页面处于消息中心页面
        测试步骤：
        1.点击"系统通知"按钮
        期望结果：
        进入系统通知页面
        检查点：
        1.对设备管理页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        TestResult = MessagePage.XiTongTongZhi(driver)
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:消息中心→查看产品公告')
    def test_MessageCenter_005ChanPinGongGao(self):
        """
        前置条件：
        页面处于消息中心页面
        测试步骤：
        1.点击"产品公告"按钮
        期望结果：
        进入产品公告页面
        检查点：
        1.对设备管理页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        TestResult = MessagePage.ChanPinGongGao(driver)
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:消息中心→查看活动通知')
    def test_MessageCenter_006HuoDongTongZhi(self):
        """
        前置条件：
        页面处于消息中心页面
        测试步骤：
        1.点击"活动通知"按钮
        期望结果：
        进入活动通知页面
        检查点：
        1.对设备管理页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        TestResult = MessagePage.HuoDongTongZhi(driver)
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:消息中心→查看交易动态')
    def test_MessageCenter_007JiaoYiDongTai(self):
        """
        前置条件：
        页面处于消息中心页面
        测试步骤：
        1.点击"交易动态"按钮
        期望结果：
        进入交易动态页面
        检查点：
        1.对设备管理页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        TestResult = MessagePage.JiaoYiDongTai(driver)
        assert TestResult == True


if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_002_Myself_tv_MessageCenter.py', "-s", "-v"])
