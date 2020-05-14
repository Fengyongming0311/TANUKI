#coding=utf-8
__author__ = 'TANUKI'

import pytest
import time, re, os, sys, random

sys.path.append("..")
from appium import webdriver


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case08_NeighborTalk import NeighborTalk


class Hachi_NeighborTalk:
    #@classmethod
    def setup_class(self):
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    # @unittest.skip("调试，不执行这条用例")
    def test_MyAPP_001LinLiFenXiang(self):
        """用例名称:友邻→邻里分享→发帖"""
        message = "戏说不是胡说，改编不是乱编。"
        driver = self.driver
        NeighborTalk.IntoNeighbor(driver)
        # 进入友邻页面
        NeighborTalk.IntoNewTopic(driver)
        NeighborTalk.ChoiceSpeakType(driver, type=1)
        TestResult = NeighborTalk.PostNewTopic(driver, message)
        #self.assertTrue(TestResult)
        assert TestResult == True

    def test_MyAPP_002LinLiHuZhu(self):
        """用例名称:友邻→邻里互助→发帖"""
        message = "一个人在科学探索的道路上，走过弯路，犯过错误，并不是坏事，更不是什么耻辱，要在实践中勇于承认和改正错误。"
        driver = self.driver
        NeighborTalk.IntoNeighbor(driver)
        # 进入友邻页面
        NeighborTalk.IntoNewTopic(driver)
        NeighborTalk.ChoiceSpeakType(driver, type=2)
        TestResult = NeighborTalk.PostNewTopic(driver, message)
        #self.assertTrue(TestResult)
        assert TestResult == True

    def test_MyAPP_003TiaoZaoShiChang(self):
        """用例名称:友邻→跳蚤市场→发帖"""
        message = """寄快递最好去快递网点邮寄，一般网点都有监控，然后自己当着快递员面前录视频，
        尤其是一些细节。如果是邮寄手机、显卡、内存条之类等贵重物品，最好让快递员不要送货上门，
        要求买家去网点自取（事先和买家沟通好），以防被调包（普通物品除外）"""
        driver = self.driver
        NeighborTalk.IntoNeighbor(driver)
        # 进入友邻页面
        NeighborTalk.IntoNewTopic(driver)
        NeighborTalk.ChoiceSpeakType(driver, type=3)
        TestResult = NeighborTalk.PostNewTopic(driver, message, price=random.randint(1,9999), phone=13466738904)
        #self.assertTrue(TestResult)
        assert TestResult == True

    #@classmethod
    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    pytest.main('start_004_NeighborTalk_AndroidTestRun.py')
    #unittest.main()
