##coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case02_ShiDiPai import ShiDiPai

class Hachi_ShiDiPai(unittest.TestCase):
    @classmethod
    def setUpClass(dondake):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'noReset': True,
            'deviceName': 'huawei-duk-al20-FFK0217609003306',
            #'deviceName':'vivo-vivo_x9-be1bd33f',
            'appPackage': 'com.pujitech.pujiejia',
            'appActivity': 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity',
            'noSign': True,
            #'skipServerInstallation': True,
            #'skipDeviceInitialization': True
        }
        dondake.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    #@unittest.skip("调试，不执行这条用例")
    def test_ShiDiPai_001RecommendApp(self):
        """用例名称:实地派首页→测试7个推荐应用和更多"""
        driver = self.driver
        ShiDiPai.IntoShiDiPai(driver)
        # 进入实地派首页
        TestResult = ShiDiPai.RecommendApp(driver)
        # 7个推荐应用和更多
        self.assertTrue(TestResult)

    def test_ShiDiPai_002Brand_Image(self):
        """用例名称:实地派首页→测试商标图片——实地派会员专享权益（品牌宣传位）"""
        driver = self.driver
        TestResult = ShiDiPai.Brand_Image(driver)
        # 点击商标图片——实地派会员专享权益（品牌宣传位）
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_ShiDiPai_003ZunXiangFuWu(self):
        """用例名称:实地派首页→测试尊享服务"""
        driver = self.driver
        TestResult = ShiDiPai.ZunXiangFuWu(driver)
        # 测试首页尊享服务
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_ShiDiPai_004Recommend_Community_Title(self):
        """用例名称:实地派首页→测试精品楼盘"""
        driver = self.driver
        ShiDiPai.XiaLaPage(driver, 600)
        TestResult = ShiDiPai.Recommend_Community_Title(driver)
        # 测试首页精品楼盘
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(3)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
