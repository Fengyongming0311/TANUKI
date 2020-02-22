##coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case10_IntoJiaSi import Into_JiaSi
from Case11_SelectScene import SelectScene
from Case04_Create_Time import Create_Time
from Case05_Price import Price
from Case06_AddShoppingCart import AddShoppingCart

class Hachi_LinBaO(unittest.TestCase):
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
            #'chromedriverExcutable':"C:\\Users\\TANUKI\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\_appium-chromedriver@3.5.2@appium-chromedriver\\chromedriver\\win\\chromedriver.exe",
            #vivoX9手机直接指定chromedrvier位置
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
            'nativeWebScreenshot': True,
        }
        dondake.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    #@unittest.skip("调试，不执行这条用例")
    def test_JiaSI_001IntoJiaSi(self):
        """用例名称:从微信进入实地打造师微信小程序→进入家私页面"""
        driver = self.driver
        TestResult = Into_JiaSi.Into_JiaSi(driver)
        self.assertTrue(TestResult)
        print("进入家私页面测试用例执行完毕")

    #@unittest.skip("调试，不执行这条用例")
    def test_LinBaO_002SelectScene(self):
        """用例名称:实地打造师小程序→家私→选择场景测试"""
        driver = self.driver
        TestResult = SelectScene.SelectScene(driver)
        # 实地打造师小程序→家私→选择场景测试
        self.assertTrue(TestResult)
        print ("选择场景测试用例执行完毕")

    #@unittest.skip("调试，不执行这条用例")
    def test_LinBaO_003CommodityTypes(self):
        """用例名称:实地打造师小程序→家电→选择分类测试"""
        driver = self.driver
        TestResult = CommodityTypes.CommodityTypes(driver)
        # 实地打造师小程序→家电→选择分类测试
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_LinBaO_004Create_Time(self):
        """用例名称:实地打造师小程序→家电→按照新品排序"""
        driver = self.driver
        TestResult = Create_Time.Create_Time(driver)
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_LinBaO_005Price(self):
        """用例名称:实地打造师小程序→家电→按照价格排序"""
        driver = self.driver
        TestResult = Price.Price(driver)
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_LinBaO_006AddShoppingCart(self):
        """用例名称:实地打造师小程序→家电→商品添加购物车"""
        driver = self.driver
        TestResult = AddShoppingCart.AddShoppingCart(driver)
        self.assertTrue(TestResult)
    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
