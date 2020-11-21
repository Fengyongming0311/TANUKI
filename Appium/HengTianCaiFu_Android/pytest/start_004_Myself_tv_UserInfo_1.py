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
from Case015_Basic_Information import Basic_Information
from Case016_IntoUserinfo_Myemail import IntoUserinfo_Myemail
from Case017_IntoChangeEmail import IntoChangeEmail
from Case018_InputErrorEmail import InputEmail
from public import *


class Test_HengTian_UserInfo_1:


    @allure.feature('用例名称:登录恒天财富账号')
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
        userid = '13093110000'
        psw = 'aa1234'
        driver = Driver.driver
        TestResult = Login.Login(driver,userid,psw)
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
    @allure.feature('用例名称:个人信息→基本信息')
    def test_Myself_UserInfo_004basic_information(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"基本信息"按钮
        期望结果：
        进入基本信息页面
        检查点：
        1.验证页面标题
        2.对基本信息页面进行截图
        测试后续步骤：
        返回个人信息页面
        """
        driver = Driver.driver
        Basic_Information.IntoBasic_Information(driver)
        TestResult = Basic_Information.Basic_Information_CheckPoint(driver)
        assert TestResult == True
        Basic_Information.Basic_Information_PageBack(driver)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→进入我的邮箱')
    def test_Myself_UserInfo_005IntoUserinfo_Myemail(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"我的邮箱"按钮
        期望结果：
        进入绑定邮箱页面
        检查点：
        1.验证标题是否为绑定邮箱
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoUserinfo_Myemail.IntoUserinfo_Myemail(driver)
        TestResult = IntoUserinfo_Myemail.IntoUserinfo_Myemail_CheckPoint(driver)
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:绑定邮箱→进入修改邮箱')
    def test_Myself_UserInfo_006ZheKouHuanLi(self):
        """
        前置条件：
        页面处于绑定邮箱页面
        测试步骤：
        1.点击"修改邮箱"按钮
        期望结果：
        进入输入新邮箱页面
        检查点：
        1.检查标题为输入新邮箱
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoChangeEmail.IntoChangeEmail(driver)
        TestResult = IntoChangeEmail.IntoChangeEmail_CheckPoint(driver)
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:修改邮箱→输入包含中文字符的邮箱')
    def test_Myself_UserInfo_007ErrorEmail1(self):
        """
        前置条件：
        页面处于输入新邮箱页面
        测试步骤：
        1.输入包含中文字符的邮箱
        2.点击修改邮箱按钮
        3.二次验证提醒，点击确认修改
        期望结果：
        toast提示更改失败！！
        检查点：
        页面截图查看提示信息（等一秒）
        测试后续步骤：
        无
        """
        ErrorEmail1 = "测试邮箱@126.com"
        driver = Driver.driver
        TestResult1 = InputEmail.InputErrorEmail(driver, ErrorEmail1)
        assert TestResult1 == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:修改邮箱→输入超长邮箱')
    def test_Myself_UserInfo_008ErrorEmail2(self):
        """
        前置条件：
        页面处于输入新邮箱页面
        测试步骤：
        1.输入超长的邮箱
        2.点击修改邮箱按钮
        3.二次验证提醒，点击确认修改
        期望结果：
        toast提示更改失败！！
        检查点：
        页面截图查看提示信息（等一秒）
        测试后续步骤：
        无
        """
        ErrorEmail2 = "oaisodauhdowuqorqepqijwdpaioaeiushdouqouoqhuwheoqwepijpdasjdpaisjdpingrnoijopipqijpasjdaofuhoeuo@126.com"
        driver = Driver.driver
        TestResult2 = InputEmail.InputErrorEmail(driver, ErrorEmail2)
        assert TestResult2 == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:修改邮箱→输入正确邮箱')
    def test_Myself_UserInfo_009RightEmail(self):
        """
        前置条件：
        页面处于输入新邮箱页面
        测试步骤：
        1.输入规则正确的邮箱
        2.点击修改邮箱按钮
        3.二次验证提醒，点击确认修改
        期望结果：
        发送邮件到提交的邮箱，
        检查点：
        页面截图查看提示信息（等一秒）
        测试后续步骤：
        无
        """
        RightEmail = "fengyongming0311@sohu.com"
        driver = Driver.driver
        InputEmail.InputRightEmail(driver, RightEmail)
        TestResult = InputEmail.InputRightEmail_CheckPoint(driver)
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_004_Myself_tv_UserInfo_1.py', "-s", "-v"])
