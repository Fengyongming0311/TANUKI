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
from public import *

class Test_User_Info_Qualified:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_Qualified_001Login(self):
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
    def test_Qualified_002IntoMyself_tv(self):
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
    def test_Qualified_003IntoMyself_Info(self):
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
    def test_Qualified_004Into_Qualified(self):
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






    @pytest.mark.skip(reason="界面UI改变这条用例不执行")
    @allure.feature('用例名称:私募合格投资者认证→查看附件')
    def test_Qualified_005AttachedFile(self):
        """
        前置条件：
        页面处于私募合格投资者认证
        测试步骤：
        1.点击附件
        期望结果：
        进入"附件"页面
        检查点：
        快照验证附件页面内容
        测试后续步骤：
        返回上一页面（私募合格投资者认证）
        """
        driver = Driver.driver
        AttachedFile.AttachedFile(driver)
        TestResult = AttachedFile.AttachedFile_CheckPoint(driver)
        assert TestResult == True
        AttachedFile.AttachedFile_Back(driver)



    @pytest.mark.skip(reason="界面UI改变这条用例不执行")
    @allure.feature('用例名称:私募合格投资者认证→查看公募产品')
    def test_Qualified_006IntoGongMuProduct(self):
        """
        前置条件：
        页面处于私募合格投资者认证
        测试步骤：
        1.点击公募产品
        期望结果：
        进入"公募产品"页面
        检查点：
        快照验证公募产品页面内容
        测试后续步骤：
        返回上一页面（私募合格投资者认证）
        """
        driver = Driver.driver
        IntoGongMuProduct.IntoGongMuProduct(driver)
        TestResult = IntoGongMuProduct.IntoGongMuProduct_CheckPoint(driver)
        assert TestResult == True
        IntoGongMuProduct.IntoGongMuProduct_Back(driver)


    @pytest.mark.skip(reason="界面UI改变这条用例不执行")
    @allure.feature('用例名称:私募合格投资者认证→查看私募产品')
    def test_Qualified_007IntoSiMuProduct(self):
        """
        前置条件：
        页面处于私募合格投资者认证
        测试步骤：
        1.点击私募产品
        期望结果：
        进入"私募产品"页面
        检查点：
        快照验证私募产品页面内容
        测试后续步骤：
        返回上一页面（私募合格投资者认证）
        """
        driver = Driver.driver
        IntoSiMuProduct.IntoSiMuProduct(driver)
        TestResult = IntoSiMuProduct.IntoSiMuProduct_CheckPoint(driver)
        assert TestResult == True
        IntoSiMuProduct.IntoSiMuProduct_Back(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:合格投资者认证→去市场看看')
    def test_Qualified_008TiaozhuanMarket(self):
        """
        前置条件：
        页面处于资管合格投资者认证页面，属于合格投资者认证成功状态
        测试步骤：
        1.点击去市场看看
        期望结果：
        跳转到理财页面
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = IntoSiMuProduct.TiaozhuanMarket(driver)
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_008_User_Info_Qualified.py', "-s", "-v"])
