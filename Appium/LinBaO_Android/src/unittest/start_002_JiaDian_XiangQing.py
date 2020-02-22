##coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case01_IntoShiDiDaZaoShi import IntoShiDiDaZaoShi
from Case07_GoodsDetail import GoodsDetail
from Case08_LookGoods import LookGoods
from Case09_DetailAddShoppingCart import DetailAddShoppingCart


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
            #'chromedriverExcutable':"C:\\Users\\TANUKI\\AppData\\Roaming\\npm\\node_modules\\appium\\node_modules\\_appium-chromedriver@4.20.2@appium-chromedriver\\chromedriver\\win\\chromedriver_2.40.exe",
            #vivoX9手机直接指定chromedrvier位置
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
            'nativeWebScreenshot': True,
        }
        dondake.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    #@unittest.skip("调试，不执行这条用例")
    def test_JiaDian_001IntoJiaDian(self):
        """用例名称:从微信进入实地打造师微信小程序家电首页"""
        driver = self.driver
        TestResult = IntoShiDiDaZaoShi.IntoShiDiDaZaoShi(driver)
        self.assertTrue(TestResult)
        #debug:优化时加个，第一个脚本如果跑失败，将不执行接下来的脚本

    #@unittest.skip("调试，不执行这条用例")
    def test_JiaDian_002GoodsDetail(self):
        """用例名称:实地打造师小程序→家电→选择价格最高的商品进入商品详情"""
        driver = self.driver
        TestResult = GoodsDetail.GoodsDetail(driver)
        self.assertTrue(TestResult)

    def test_JiaDian_003LookGoods(self):
        """用例名称：商品详情页面，滑动查看商品内容"""
        driver = self.driver
        TestResult = LookGoods.LookGoods(driver)
        self.assertTrue(TestResult)

    def test_JiaDian_004DetailAddShoppingCart(self):
        """用例名称：商品详情页面，商品添加购物车"""
        driver = self.driver
        TestResult = DetailAddShoppingCart.DetailAddShoppingCart(driver,switch = 1)
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
