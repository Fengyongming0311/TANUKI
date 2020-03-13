# coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case26_IntoShoppingCart import Into_ShoppingCart
from Case27_ShoppingCart_Choose import ChooseGoods
from Case29_ShoppingCart_Orders import Orders


class ShoppingCart_Orders(unittest.TestCase):
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
    def test_ShoppingCart_001IntoShoppingCart(self):
        """用例名称:从微信进入实地打造师微信小程序→进入购物车页面"""
        driver = self.driver
        TestResult = Into_ShoppingCart.Into_ShoppingCart(driver)
        self.assertTrue(TestResult)
        # print("进入购物车页面测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_ShoppingCart_002ChooseGoods(self):
        """用例名称:实地打造师小程序→购物车→勾选商品"""
        driver = self.driver
        TestResult = ChooseGoods.OrderChooseGoods(driver)
        # 实地打造师小程序→购物车→勾选商品
        self.assertTrue(TestResult)
        # print ("选择智能场景测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_ShoppingCart_003Orders(self):
        """用例名称:实地打造师小程序→购物车→勾选商品→下单"""
        driver = self.driver
        TestResult = Orders.Orders(driver)
        # 实地打造师小程序→购物车→勾选商品→下单
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
