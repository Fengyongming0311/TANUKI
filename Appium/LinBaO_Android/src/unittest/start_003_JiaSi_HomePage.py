# coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case10_IntoJiaSi import Into_JiaSi
from Case11_JiaSi_SelectScene import JiaSiSelectScene
from Case12_JiaSi_CommodityTypes import JiaSiCommodityTypes

from Case13_JiaSi_Create_Time import JiaSiCreate_Time
from Case14_JiaSi_Price import JiaSiPrice
from Case15_JiaSi_AddShoppingCart import JiaSiAddShoppingCart


class JiaSi_HomePage(unittest.TestCase):
    @classmethod
    def setUpClass(dondake):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "Appium",
            # 'automationName': 'UIAutomator2',
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

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_001IntoJiaSi(self):
        """用例名称:从微信进入实地打造师微信小程序→进入家私页面"""
        driver = self.driver
        TestResult = Into_JiaSi.Into_JiaSi(driver)
        self.assertTrue(TestResult)
        # print("进入家私页面测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_002JiaSiSelectScene(self):
        """用例名称:实地打造师小程序→家私→选择场景测试"""
        driver = self.driver
        TestResult = JiaSiSelectScene.JiaSiSelectScene(driver)
        # 实地打造师小程序→家私→选择场景测试
        self.assertTrue(TestResult)
        # print ("选择场景测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_003JiaSiCommodityTypes(self):
        """用例名称:实地打造师小程序→家私→选择分类测试"""
        print("开始执行脚本家私选择分类")
        driver = self.driver
        TestResult = JiaSiCommodityTypes.JiaSiCommodityTypes(driver)
        # 实地打造师小程序→家私→选择分类测试
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_004JiaSiCreate_Time(self):
        """用例名称:实地打造师小程序→家私→按照新品排序"""
        driver = self.driver
        TestResult = JiaSiCreate_Time.JiaSiCreate_Time(driver)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_005JiaSiPrice(self):
        """用例名称:实地打造师小程序→家私→按照价格排序"""
        driver = self.driver
        TestResult = JiaSiPrice.JiaSiPrice(driver)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_JiaSi_006JiaSiAddShoppingCart(self):
        """用例名称:实地打造师小程序→家私→商品添加购物车"""
        driver = self.driver
        TestResult = JiaSiAddShoppingCart.JiaSiAddShoppingCart(driver)
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
