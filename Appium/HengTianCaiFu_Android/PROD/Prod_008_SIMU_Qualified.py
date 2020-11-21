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
from Case031_Into_Qualified import Into_Qualified
from Case032_AttachedFile import AttachedFile
from Case033_IntoGongMuProduct import IntoGongMuProduct
from Case034_IntoSiMuProduct import IntoSiMuProduct
from Case058_HeGeTouZiZheRenZheng import HeGeTouZiZheRenZheng
from Case059_UploadZiChanProve import UploadZiChanProve
from public import *

class Test_SIMU_Qualified:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_SIMU_Qualified_001Login(self):
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
    def test_SIMU_Qualified_002IntoMyself_tv(self):
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
    def test_SIMU_Qualified_003IntoMyself_Info(self):
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
    @allure.feature('用例名称:个人信息→进入合格投资者认证')
    def test_SIMU_Qualified_004Into_Qualified(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"合格投资者认证"按钮
        期望结果：
        进入"合格投资者认证"页面
        检查点：
        1.验证页面标题
        测试后续步骤：
        无
        """
        driver = Driver.driver
        Into_Qualified.Into_Qualified(driver)
        TestResult = Into_Qualified.Into_Qualified_CheckPoint(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:合格投资者认证→合格投资者认证申请须知')
    def test_SIMU_Qualified_005Application_Guide(self):
        """
        合格投资者认证申请须知
        """
        driver = Driver.driver
        TestResult = HeGeTouZiZheRenZheng.Application_Guide(driver)

        assert TestResult == True





    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:合格投资者认证→进入私募合格投资者')
    def test_SIMU_Qualified_006IntoSIMUTouZizhe(self):
        """
        进入私募合格投资者
        """
        driver = Driver.driver
        TestResult = HeGeTouZiZheRenZheng.IntoSIMUTouZizhe(driver)
        print ("用例名称:合格投资者认证→进入私募合格投资者测试结果============",TestResult)
        assert TestResult == True




    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:私募合格投资者认证→上传资产证明')
    def test_SIMU_Qualified_007UpLoadZiChanProve(self):
        """
        上传资产证明
        """
        driver = Driver.driver
        TestResult = UploadZiChanProve.UploadZiChanProve(driver)
        assert TestResult == True








if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['Prod_008_SIMU_Qualified.py', "-s", "-v"])

