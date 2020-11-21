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
from Case014_IntoMyself_Info import myself_info
from Case024_ShenFenShuoMing import ShenFenShuoMing
from Case025_UserInfoAutonym import Autonym
from Case026_UserInfoInvestor import UserInfoInvestor
from public import *


class Test_HengTian_UserInfo_3:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_Myself_UserInfo_001Login(self):
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
    def test_Myself_UserInfo_002IntoMyself_tv(self):
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
    @allure.feature('用例名称:我的页面→进入个人信息')
    def test_Myself_UserInfo_003IntoMyself_Info(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"个人信息"按钮
        期望结果：
        进入个人信息页面
        检查点：
        1.验证标题是否为个人信息
        2.输出客户姓名
        3.输出客户编号
        4.输出客户注册手机号
        测试后续步骤：
        无
        """
        driver = Driver.driver
        myself_info.intomyself_info(driver)
        #进入个人信息页面
        TestResult = myself_info.myself_info_CheckPoint(driver)
        #设置检查点检查个人信息
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→查看身份认证说明')
    def test_Myself_UserInfo_004ShenFenShuoMing(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"身份认证问号"按钮
        期望结果：
        打开身份认证说明
        检查点：
        1.验证内容（与接口数据校验是否一致：/app/content/frontend/getContent）
        测试后续步骤：
        点击返回按钮返回个人信息页面
        """
        driver = Driver.driver
        ShenFenShuoMing.ShenFenShuoMing(driver)

        #CheckPoint = ShenFenShuoMing.ShenFenShuoMingAPI_CheckPoint()
        #接口获取的身份说明内容

        BackStr = ShenFenShuoMing.ShenFenShuoMing_CheckPoint(driver)
        #从UI自动化获取的身份说明内容
        if len(BackStr) == 0:
            TestResult = False
        else:
            TestResult = True
        #判断返回值是否为空  不为空则用例结果正确


        ShenFenShuoMing.ShenFenShuoMing_PageBack(driver)

        assert TestResult == True




    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→身份信息')
    def test_Myself_UserInfo_005Autonym(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"身份认证"按钮
        期望结果：
        进入身份认证（信息）页面
        检查点：
        1.标题
        2.输出姓名，身份类型，身份证号
        测试后续步骤：
        点击返回按钮，返回个人信息页面
        """
        driver = Driver.driver
        Autonym.IntoAutonym(driver)

        TestResult = Autonym.Autonym_CheckPoint(driver)
        #从UI自动化获取的风测说明内容
        assert TestResult == True

        Autonym.Autonym_PageBack(driver)



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→投资者分类认证')
    def test_Myself_UserInfo_006user_info_investor(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"投资者分类认证"按钮
        期望结果：
        进入投资者分类认证页面
        2.点击申请转为专业投资者（普转专）
        3.如果跳到做题页面得选择5道题的结果
        4.进入上传投资经历证明页面
        5.上传投资经历证明
        检查点：
        1.验证页面标题
        测试后续步骤：
        无
        """
        driver = Driver.driver
        UserInfoInvestor.IntoUserInfoInvestor(driver)
        TestResult = UserInfoInvestor.PROD_UserInfoInvestor_CheckPoint(driver)
        assert TestResult == True

        UserInfoInvestor.UserInfoInvestor_PageBack(driver)



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_006_Myself_tv_UserInfo_3.py', "-s", "-v"])

