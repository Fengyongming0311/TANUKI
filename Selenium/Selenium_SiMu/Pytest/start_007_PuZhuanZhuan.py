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
from Case026_UserInfoInvestor import UserInfoInvestor
from Case027_ApplyProInvestors import ApplyProInvestors
from Case028_UploadInvestProve import UploadInvestProve
from Case029_UploadAssetProve import UploadAssetProve
from Case030_Submit_UpLoadFile import Submit_UpLoadFile
from public import *

#普转专暂不执行
class Test_PuZhuanZhuan:


    #@allure.feature('用例名称:登录恒天财富账号')
    def test_PuZhuanZhuan_001Login(self):
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
    def test_PuZhuanZhuan_002IntoMyself_tv(self):
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
    def test_PuZhuanZhuan_003IntoMyself_Info(self):
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
    @allure.feature('用例名称:个人信息→进入投资者分类认证')
    def test_PuZhuanZhuan_004user_info_investor(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"投资者分类认证"按钮
        期望结果：
        进入投资者分类认证页面
        检查点：
        1.验证页面标题
        测试后续步骤：
        无
        """
        driver = Driver.driver
        UserInfoInvestor.IntoUserInfoInvestor(driver)
        TestResult = UserInfoInvestor.UserInfoInvestor_CheckPoint(driver)
        assert TestResult == True


        #UserInfoInvestor.UserInfoInvestor_PageBack(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:投资者分类认证→申请转为专业投资者')
    def test_PuZhuanZhuan_005ClickPuZhuanZhuan(self):
        """
        前置条件：
        页面处于普通投资者认证
        测试步骤：
        1.上滑页面，显示出"申请转为专业投资者"
        2.弹出提示页面，点击确认按钮
        期望结果：
        进入"普通投资者转专业投资者认证"页面
        检查点：
        1.验证页面标题
        测试后续步骤：
        无
        """
        driver = Driver.driver
        ApplyProInvestors.ApplyProInvestors(driver)
        TestResult = ApplyProInvestors.ProInvestors_CheckPoint(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:普通投资者转专用投资者→上传投资经历证明')
    def test_PuZhuanZhuan_006UploadInvestProve(self):
        """
        前置条件：
        页面处于普通投资者转专业投资者认证页面
        测试步骤：
        1.点击上传投资经历证明
        2.进入上传投资经历证明页面，删除之前上传的图片
        3.上传相册中第一张图片
        4点击提交
        期望结果：
        进入"普通投资者转专业投资者认证"页面，上传图片成功
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = UploadInvestProve.UploadInvestProve(driver)
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:普通投资者转专用投资者→上传收入证明或金融资产证明')
    def test_PuZhuanZhuan_007UploadAssetProve(self):
        """
        前置条件：
        页面处于普通投资者转专业投资者认证页面
        测试步骤：
        1.点击上传收入证明或金融资产证明
        2.进入上传收入证明或金融资产证明页面，删除之前上传的图片
        3.上传相册中第一张图片
        4点击提交
        期望结果：
        进入"普通投资者转专业投资者认证"页面，上传图片成功
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = UploadAssetProve.UploadAssetProve(driver)
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:普通投资者转专用投资者→提交资料')
    def test_PuZhuanZhuan_008PuZhuanZhuan_Submit(self):
        """
        前置条件：
        页面处于普通投资者转专业投资者认证页面
        测试步骤：
        1.之前上传过投资经历证明和金融资产证明
        2.点击立即提交
        3.弹出短信验证码输入框
        4.截图查看是否弹出短信验证码输入框
        5.输入错误验证码点击提交
        期望结果：
        报验证失败，请重新获取短信验证码
        检查点：
        无
        测试后续步骤：
        无
        """
        driver = Driver.driver
        TestResult = Submit_UpLoadFile.PuZhuanZhuan_Submit(driver)
        assert TestResult == True




if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_007_PuZhuanZhuan.py', "-s", "-v"])

