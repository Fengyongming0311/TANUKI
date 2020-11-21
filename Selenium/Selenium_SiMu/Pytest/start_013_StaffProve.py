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
from Case041_StaffProve import StaffProve
from public import *


class Test_StaffProve:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_StaffProve_001Login(self):
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
    def test_StaffProve_002IntoMyself_tv(self):
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
    @allure.feature('用例名称:我的页面→进入员工验证')
    def test_StaffProve_003Into_StaffProve(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"员工验证"按钮
        期望结果：
        进入员工验证页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = StaffProve.Into_StaffProve(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:输入正确工号进行员工验证')
    def test_StaffProve_004TrueStaffNO(self):
        """
        前置条件：
        页面处于员工验证
        测试步骤：
        1.输入正确工号
        2.点击查询员工信息
        期望结果：
        查询到员工信息
        检查点：
        查看员工姓名
        测试后续步骤：
        返回员工验证页面
        """
        driver = Driver.driver
        TestResult = StaffProve.StaffNo(driver,"H017639","赵晶晶")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:输入错误工号进行员工验证')
    def test_StaffProve_005FalseStaffNO(self):
        """
        前置条件：
        页面处于员工验证
        测试步骤：
        1.输入错误工号
        2.点击查询员工信息
        期望结果：
        无法查询到员工信息
        检查点：
        查看员工姓名
        测试后续步骤：
        返回员工验证页面
        """
        driver = Driver.driver
        TestResult = StaffProve.StaffNo(driver,"H111111","赵晶晶")
        assert TestResult == False
        #输入错误工号进行员工验证======False就对了


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:输入正确员工姓名进行员工验证')
    def test_StaffProve_006TrueStaffName(self):
        """
        前置条件：
        页面处于员工验证
        测试步骤：
        1.输入正确员工姓名
        2.点击查询员工信息
        期望结果：
        查询到员工信息
        检查点：
        查看员工姓名是否正确
        测试后续步骤：
        返回员工验证页面
        """
        driver = Driver.driver
        TestResult = StaffProve.StaffName(driver,"刘涛")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:输入错误员工姓名进行员工验证')
    def test_StaffProve_007FalseStaffName(self):
        """
        前置条件：
        页面处于员工验证
        测试步骤：
        1.输入错误员工姓名
        2.点击查询员工信息
        期望结果：
        无法查询到员工信息
        检查点：
        查看员工姓名是否正确
        测试后续步骤：
        返回员工验证页面
        """
        driver = Driver.driver
        TestResult = StaffProve.StaffName(driver,"周杰伦")
        assert TestResult == False
        #输入错误员工姓名进行员工验证 ==False就对了



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_013_StaffProve.py', "-s", "-v"])
