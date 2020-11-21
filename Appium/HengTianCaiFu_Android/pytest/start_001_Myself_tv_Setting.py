#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case001_Login import Login
from Case002_IntoMyself_tv import IntoMyself_tv
from Case003_IntoSetting import IntoSetting
from Case004_DeviceManage import DeviceManage
from Case005_LoginRecord import LoginRecord
from Case006_IntoAbout import IntoAbout
from Case007_CheckVersion import CheckVersion
from Case008_YinSiZhengCe import YinSiZhengCe
from Case009_FuWuXieYi import FuWuXieYi
from public import *

class Test_HengTian_Setting():

    @allure.feature('用例名称:登录恒天财富账号')
    def test_Setting_001Login(self):
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
        TestResult = Login.Login(Driver.driver, userid, psw)
        #登录恒天财富账号
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:打开恒天财富APP→进入我的页面')
    def test_Setting_002IntoMyself_tv(self):
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
        TestResult = IntoMyself_tv.IntoMyself_tv_CheckPoint(Driver.driver)
        #设置检查点验证进入我的成功
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→点击设置按钮进入设置页面')
    def test_Setting_003IntoSetting(self):
        """
        前置条件：
        已登录状态，页面处于我的页面
        测试步骤：
        1.点击左上角"设置"按钮
        期望结果：
        进入设置页面
        检查点：
        验证标题是否为设置
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoSetting.IntoSetting(driver)
        #进入设置页面
        TestResult = IntoSetting.IntoSetting_CheckPoint(driver)
        #设置检查点验证进入设置成功
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:设置→查看设备管理')
    def test_Setting_004DeviceManage(self):
        """
        前置条件：
        页面处于设置页面
        测试步骤：
        1.点击"设备管理"按钮
        期望结果：
        进入设备管理页面
        检查点：
        1.对设备管理页面进行ScreenShot
        2.验证标题是否为设备管理
        测试后续步骤：
        1.点击"返回上一页面"，返回到设置页面
        """
        driver = Driver.driver
        DeviceManage.DeviceManage(driver)
        #进入设备管理
        TestResult = DeviceManage.DeviceManage_CheckPoint(driver)
        #检查点验证设备管理内容
        DeviceManage.DeviceManage_PageBack(driver)
        #返回设置页面
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:设置→登录日志查询')
    def test_Setting_005LoginLog(self):
        """
        前置条件：
        页面处于设置页面
        测试步骤：
        1.点击"登录日志查询"按钮
        期望结果：
        进入登录日志查询页面
        检查点：
        1.对设备管理页面进行ScreenShot
        2.验证标题是否为登录日志查询
        测试后续步骤：
        1.点击"返回上一页面"，返回到设置页面
        """
        driver = Driver.driver
        LoginRecord.LoginRecord(driver)
        #进入登录日志查询
        TestResult = LoginRecord.LoginRecord_CheckPoint(driver)
        #检查点验证登陆日志查询
        LoginRecord.LoginRecord_PageBack(driver)
        #返回设置页面
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:设置→进入关于页面')
    def test_Setting_006IntoAbout(self):
        """
        前置条件：
        页面处于设置页面
        测试步骤：
        1.点击"关于"按钮
        期望结果：
        进入关于页面
        检查点：
        1.验证标题是否为关于
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoAbout.IntoAbout(driver)
        #进入设置页面
        TestResult = IntoAbout.IntoAbout_CheckPoint(driver)
        #检查点验证进入关于成功
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:关于→检查版本')
    def test_Setting_007CheckVersion(self):
        """
        前置条件：
        页面处于关于页面
        测试步骤：
        1.点击"检查版本"
        期望结果：
        页面弹出新版本升级提示
        或者提示已经是最新版本
        检查点：
        无
        测试后续步骤：
        1.点击"稍后再说"不做升级，页面返回关于
        """
        driver = Driver.driver
        CheckVersion.CheckVersion(driver)
        #检查版本
        TestResult = CheckVersion.CheckVersion_CheckPoint(driver)
        #检查点验证检查版本
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:关于→隐私政策')
    def test_Setting_008YinSiZhengCe(self):
        """
        前置条件：
        页面处于关于页面
        测试步骤：
        1.点击"隐私政策"
        2.进入隐私政策页面
        3.上滑查看隐私政策协议内容
        4.左滑查看页面是否偏移
        期望结果：
        正确显示隐私权政策协议
        左滑页面不做偏移
        检查点：
        1.对隐私权政策协议页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到关于页面
        """
        driver = Driver.driver
        YinSiZhengCe.IntoYinSiZhengCe(driver)
        #点击进入隐私政策
        TestResult = YinSiZhengCe.YinSiZhengCe_CheckPoint(driver)
        #检查点隐私政策
        YinSiZhengCe.YinSiZhengCe_PageBack(driver)
        #返回设置页面
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:关于→服务协议')
    def test_Setting_009FuWuXieYi(self):
        """
        前置条件：
        页面处于关于页面
        测试步骤：
        1.点击"服务协议"
        2.进入服务协议页面
        3.上滑查看服务协议内容
        4.左滑查看页面是否偏移
        期望结果：
        正确显示服务协议
        左滑页面不做偏移
        检查点：
        1.对服务协议页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到关于页面
        """
        driver = Driver.driver
        FuWuXieYi.IntoFuWuXieYi(driver)
        #点击进入隐私政策
        TestResult = FuWuXieYi.FuWuXieYi_CheckPoint(driver)
        #检查点隐私政策
        FuWuXieYi.FuWuXieYi_PageBack(driver)
        #返回设置页面
        assert TestResult == True




if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_001_Myself_tv_Setting.py', "-s", "-v"])
