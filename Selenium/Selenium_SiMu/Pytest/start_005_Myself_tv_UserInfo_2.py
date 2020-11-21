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
from Case019_UserInfoBank import UserInfoBank
from Case020_FengCeShuoMing import FengCeShuoMing
from Case021_IntoFengCe import IntoFengCe
from Case022_IntoRiskTest import IntoRiskTest
from Case023_StartRiskTest import StartRiskTest
from public import *

class Test_HengTian_UserInfo_2:
    '''
    @classmethod
    def setup_class(self):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'noReset': True,
            'deviceName': 'huawei-duk-al20-FFK0217609003306',
            'appPackage': 'com.chtwm.mall',
            #上边这个肯定是对的
            'appActivity': 'com.chtwm.mall.activity.user.LaunchActivity',
            'noSign': True,
            #'skipServerInstallation': True,
            #'skipDeviceInitialization': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
    '''

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
        userid = '13093110000'
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
    @allure.feature('用例名称:个人信息→个人信息银行卡')
    def test_Myself_UserInfo_004UserInfoBank(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"银行卡"按钮
        期望结果：
        进入银行卡页面
        检查点：
        1.截图验证
        测试后续步骤：
        点击返回按钮返回个人信息页面
        """
        driver = Driver.driver
        TestResult = UserInfoBank.IntoUserInfoBank(driver)
        assert TestResult == True
        UserInfoBank.Bank_PageBack(driver)


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→风测说明')
    def test_Myself_UserInfo_005FengCeShuoMing(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"基金风险测评"按钮
        期望结果：
        进入风测说明页面
        检查点：
        1.验证内容（与接口数据校验是否一致：/app/content/frontend/getContent）
        测试后续步骤：
        点击确认关闭提示框，返回个人信息页面
        """
        driver = Driver.driver
        FengCeShuoMing.FengCeShuoMing(driver)

        #CheckPoint = FengCeShuoMing.FengCeShuoMingAPI_CheckPoint()
        #接口获取的风测说明内容
        TestResult = FengCeShuoMing.FengCeShuoMing_CheckPoint(driver)
        #从UI自动化获取的风测说明内容

        FengCeShuoMing.FengCeShuoMing_PageBack(driver)

        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:个人信息→进入风险测评')
    def test_Myself_UserInfo_006IntoFengCe(self):
        """
        前置条件：
        页面处于个人信息页面
        测试步骤：
        1.点击"基金风险测评"按钮
        期望结果：
        进入基金风险测评页面
        检查点：
        1.验证页面标题
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoFengCe.IntoFengCe(driver)
        TestResult = IntoFengCe.IntoFengCe_CheckPoint(driver)

        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:风险测评→点击重新测评→开始风险测评')
    def test_Myself_UserInfo_007IntoRiskTest(self):
        """
        前置条件：
        页面处于风险评测页面
        测试步骤：
        1.点击重新测评
        期望结果：
        进入风险测评页面，并弹出风险揭示提示
        检查点：
        打印风险揭示内容
        测试后续步骤：
        点击确定
        """
        driver = Driver.driver
        IntoRiskTest.IntoRiskTest(driver)
        IntoRiskTest.Rerisk_Reason(driver)
        #选择重新风测原因
        TestResult = IntoRiskTest.FengCeShuoMing_CheckPoint(driver)
        assert TestResult == True





    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:风险评测→随机进行风险内容评测')
    def test_Myself_UserInfo_008StartRiskTest(self):
        """
        前置条件：
        页面处于风险评测页面
        测试步骤：
        1.对风险评测内容进行随机填写
        期望结果：
        完成风险测评
        检查点：
        无
        测试后续步骤：
        无
        """
        questions = 12
        #配置题目数

        driver = Driver.driver
        try:
            for i in range(questions):
                if i == 4:
                    StartRiskTest.Select_Risk_3Answers(driver)
                    #随机从3个答案里选择

                elif i == 9:
                    #第十题，只能选择D
                    StartRiskTest.Select_Risk_Q10(driver)

                else:
                    StartRiskTest.Select_Risk_4Answers(driver)
                    #随机从4个答案里选择
        except:
            pass
        finally:
            StartRiskTest.fin(driver)




if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_005_Myself_tv_UserInfo_2.py', "-s", "-v"])
