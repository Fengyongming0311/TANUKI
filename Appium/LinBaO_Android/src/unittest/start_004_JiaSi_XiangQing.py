# coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case10_IntoJiaSi import Into_JiaSi
from Case16_JiaSi_GoodsDetail import JiaSiGoodsDetail
from Case08_LookGoods import LookGoods
from Case17_JiaSiDetailAddShoppingCart import JiaSiDetailAddShoppingCart


class JiaSi_XiangQing(unittest.TestCase):
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
    def test_JiaSi_002JiaSiGoodsDetail(self):
        """用例名称:实地打造师小程序→家私→选择价格最高的商品进入商品详情"""
        driver = self.driver
        TestResult = JiaSiGoodsDetail.JiaSiGoodsDetail(driver)
        self.assertTrue(TestResult)

    def test_JiaSi_003JiaSiLookGoods(self):
        """用例名称：家私商品详情页面，滑动查看商品内容"""
        driver = self.driver
        TestResult = LookGoods.LookGoods(driver)
        self.assertTrue(TestResult)

    def test_JiaSi_004JiaSiDetailAddShoppingCart(self):
        """用例名称：家私商品详情页面，商品添加购物车"""
        driver = self.driver
        TestResult = JiaSiDetailAddShoppingCart.JiaSiDetailAddShoppingCart(driver, switch=1)
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
