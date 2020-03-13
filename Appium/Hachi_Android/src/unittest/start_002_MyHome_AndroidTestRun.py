#coding=utf-8
__author__ = 'TANUKI'

import unittest, time, re, sys

sys.path.append("..")
from appium import webdriver
import os, time

sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case03_MyHome import MyHome
from Case04_MyTorrent import MyTorrent
from Case05_MyCoupon import MyCoupon
from Case06_MyOrder import MyOrder

class Hachi_MyHome(unittest.TestCase):
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

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_001MsgSetting(self):
        """用例名称:我家→测试我的消息、设置、进入个人资料是否正常显示"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        # 进入我家页面
        time.sleep(3)
        TestResult = MyHome.MyHome_MsgSetting(driver)
        # 测试我的消息、设置、进入个人资料是否正常显示
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_002Change_ProfilePhoto(self):
        """用例名称:我家→修改个人资料中的头像功能"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(1)
        TestResult = MyHome.Change_ProfilePhoto(driver)
        ##修改个人头像
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_003Change_PersonalData(self):
        """用例名称:我家→修改个人资料功能"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(1)
        TestResult = MyHome.Change_PersonalData(driver)
        # 修改个人资料功能
        """
        BUG下期优化一下荣耀V9修改个人信息生日身高体重上滑下滑坐标不对问题
        """
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_004AddressManage(self):
        """用例名称:我家→地址管理→增加收货地址"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyHome.AddressManage(driver)
        # 地址管理增加收货地址
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_005DeleteAddress(self):
        """用例名称:我家→地址管理→删除收货地址"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyHome.DeleteAddress(driver, 1)
        # 地址管理删除收货地址driver后面的数字为删除次数
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_006MyTorrent(self):
        """用例名称:我家→进入我的种子"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyTorrent.MyTorrent(driver)
        # 进入我的种子
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_007IntoCoupon(self):
        """用例名称:我家→进入我的优惠券"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyCoupon.IntoCoupon(driver)
        # 进入我的优惠券
        self.assertTrue(TestResult)

    #@unittest.skip("调试，不执行这条用例")
    def test_MyHome_008WoJiaOrder(self):
        """用例名称:我家→我的订单查看订单详情"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyOrder.WoJiaOrder(driver)
        # 我家的订单查看详情
        self.assertTrue(TestResult)

    def test_MyHome_009AllOrder(self):
        """用例名称:我家→我家查看全部订单"""
        driver = self.driver
        MyHome.IntoMyHome(driver)
        time.sleep(2)
        TestResult = MyOrder.AllOrder(driver)
        # 我家查看全部订单
        self.assertTrue(TestResult)

    def test_MyHome_010ClickMyOrder(self):
        """用例名称:我家→我的订单订单管理"""
        driver = self.driver
        TestResult = MyOrder.ClickMyOrder(driver)
        # 我的订单订单管理
        self.assertTrue(TestResult)

    @classmethod
    def tearDownClass(dondake):
        time.sleep(2)
        dondake.driver.quit()


if __name__ == "__main__":
    unittest.main()
