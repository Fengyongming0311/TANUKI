##coding=utf-8
__author__ = 'TANUKI'
'''
Public_Page.debug_NomalTest 需要加返回值，返回0 或者1 或者True 或者false 要不脚本无法判断成功失败
如果返回false 直接跳入异常
'''
import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case03_MyHome import MyHome
from Case07_MyAPP import MyAPP
from FilePublic_Page import Public_Page


class Hachi_MyAPP(unittest.TestCase):
    @classmethod
    def setUpClass(dondake):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'noReset': True,
            'deviceName': 'huawei-duk-al20-FFK0217609003306',
            #'deviceName': 'vivo-vivo_x9-be1bd33f',
            'appPackage': 'com.pujitech.pujiejia',
            'appActivity': 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity',
            'noSign': True,
            'skipServerInstallation': True,
            'skipDeviceInitialization': True
        }
        dondake.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_001ShoppingCart(self):
        """用例名称:我家→全部应用→我的购物车"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="我的购物车", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_002BindingRooms(self):
        """用例名称:我家→全部应用→房间绑定"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="房间绑定", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_003FaultRepair(self):
        """用例名称:我家→全部应用→我的报事报修"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="我的报修", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_004CommunityServices(self):
        """用例名称:我家→全部应用→社区服务"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="社区服务", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_005SmartHome(self):
        """用例名称:我家→全部应用→智能家居"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="智能家居", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_006FaceRecognition(self):
        """用例名称:我家→全部应用→人脸识别"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="人脸识别", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_007VisitorInvitation(self):
        """用例名称:我家→全部应用→访客邀请"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="访客邀请", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_008MyActivity(self):
        """用例名称:我家→全部应用→我的活动"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.MyApplication(driver, AppName="我的活动", wojia=True)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_009IntoALLAPP(self):
        """用例名称:我家→全部应用→进入全部应用"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        TestResult = MyAPP.IntoALLAPP(driver)
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_010FavoriteShops(self):
        """用例名称:我家→全部应用→进入商家收藏"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="商家收藏")
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_011HomeLetter(self):
        """用例名称:我家→全部应用→进入我的家书"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="我的家书")
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_012Focus(self):
        """用例名称:我家→全部应用→进入我的关注"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="我的关注")
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_013MyOpinion(self):
        """用例名称:我家→全部应用→进入我的评价"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="我的评价")
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_014CarHailingService(self):
        """用例名称:我家→全部应用→进入约车记录"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="约车记录")
        self.assertTrue(TestResult)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_015MyPost(self):
        """用例名称:我家→全部应用→进入我的帖子"""
        driver = self.driver
        TestResult = MyAPP.MyApplication(driver, AppName="我的帖子")
        Public_Page.ExitBack(driver)
        self.assertTrue(TestResult)

    def test_MyAPP_016SmartBandInstruction(self):
        """用例名称:我家→全部应用→智能手环使用说明"""
        driver = self.driver
        TestResult = MyHome.SmartBandInstruction(driver)
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(2)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
