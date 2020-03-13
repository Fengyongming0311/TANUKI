# coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case18_IntoZhiNeng import Into_ZhiNeng
from Case19_ZhiNeng_SelectScene import ZhiNengSelectScene
from Case20_ZhiNeng_CommodityTypes import ZhiNengCommodityTypes

from Case21_ZhiNeng_Create_Time import ZhiNengCreate_Time
from Case22_ZhiNeng_Price import ZhiNengPrice
from Case23_ZhiNeng_AddShoppingCart import ZhiNengAddShoppingCart


class ZhiNeng_HomePage(unittest.TestCase):
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
    def test_ZhiNeng_001IntoZhiNeng(self):
        """用例名称:从微信进入实地打造师微信小程序→进入智能页面"""
        driver = self.driver
        TestResult = Into_ZhiNeng.Into_ZhiNeng(driver)
        self.assertTrue(TestResult)
        # print("进入智能页面测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_ZhiNeng_002ZhiNengSelectScene(self):
        """用例名称:实地打造师小程序→智能→选择场景测试"""
        driver = self.driver
        TestResult = ZhiNengSelectScene.ZhiNengSelectScene(driver)
        # 实地打造师小程序→智能→选择场景测试
        self.assertTrue(TestResult)
        # print ("选择智能场景测试用例执行完毕")

    # @unittest.skip("调试，不执行这条用例")
    def test_ZhiNeng_003JiaSiCommodityTypes(self):
        """用例名称:实地打造师小程序→智能→选择分类测试"""
        print("开始执行脚本智能选择分类")
        driver = self.driver
        TestResult = ZhiNengCommodityTypes.ZhiNengCommodityTypes(driver)
        # 实地打造师小程序→智能→选择分类测试
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_ZhiNeng_004ZhiNengCreate_Time(self):
        """用例名称:实地打造师小程序→智能→按照新品排序"""
        driver = self.driver
        TestResult = ZhiNengCreate_Time.ZhiNengCreate_Time(driver)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_ZhiNeng_005ZhiNengPrice(self):
        """用例名称:实地打造师小程序→智能→按照价格排序"""
        driver = self.driver
        TestResult = ZhiNengPrice.ZhiNengPrice(driver)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_ZhiNeng_006ZhiNengAddShoppingCart(self):
        """用例名称:实地打造师小程序→智能→商品添加购物车"""
        driver = self.driver
        TestResult = ZhiNengAddShoppingCart.ZhiNengAddShoppingCart(driver)
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
