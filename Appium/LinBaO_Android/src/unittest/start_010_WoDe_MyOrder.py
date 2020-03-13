# coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case30_IntoWoDe import Into_WoDe
from Case33_WoDe_MyOrder import MyOrder
from Case32_UserInfo_ChangeUserName import ChangeUserName


class WoDe_UserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(dondake):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "Appium",
            #'automationName': 'UIAutomator2',
            'noReset': True,
            'deviceName': 'huawei-duk-al20-FFK0217609003306',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            # 'appActivity': '.ui.LauncherUI',
            'noSign': True,
            'skipServerInstallation': True,
            'skipDeviceInitialization': True,
            'recreateChromeDriverSessions': True,
            # 'chromedriverExcutable':"C:\\Users\\TANUKI\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\_appium-chromedriver@3.5.2@appium-chromedriver\\chromedriver\\win\\chromedriver.exe",
            # vivoX9手机直接指定chromedrvier位置
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
            'nativeWebScreenshot': True,
        }
        dondake.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    #@unittest.skip("调试，不执行这条用例")
    def test_WoDe_001IntoWoDe(self):
        """用例名称:从微信进入实地打造师微信小程序→进入我的页面"""
        driver = self.driver
        TestResult = Into_WoDe.Into_WoDe(driver)
        self.assertTrue(TestResult)
        # print("进入我的页面测试用例执行完毕")

    #@unittest.skip("调试，不执行这条用例")
    def test_WoDe_002MyOrder(self):
        """用例名称:实地打造师小程序→我的→查看全部订单"""
        driver = self.driver
        TestResult = MyOrder.MyOrder(driver)
        #实地打造师小程序→我的→查看全部订单
        self.assertTrue(TestResult)

    @unittest.skip("调试，不执行这条用例")
    def test_WoDe_003ChangeUserName(self):
        """用例名称:实地打造师小程序→我的→进入用户信息页面→点击昵称进入昵称修改页面→修改昵称"""
        driver = self.driver
        TestResult = ChangeUserName.ChangeUserName(driver)
        #实地打造师小程序→我的→进入用户信息页面→点击昵称进入昵称修改页面→修改昵称
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
