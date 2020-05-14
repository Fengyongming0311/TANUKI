#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")
from appium import webdriver


sys.path.append("../ReleasePage")
# from 文件名 import Class名
#from Case001_Login import Login
from Case001_LoginPO import Login
from Case002_IntoMyself_tv import IntoMyself_tv

class Test_HengTian_Login:
    @classmethod
    def setup_class(self):
        desired_caps = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'noReset': True,
            'deviceName': 'huawei-duk-al20-FFK0217609003306',
            'appPackage': 'com.chtwm.mall',
            #上边这个肯定是对的
            'appActivity': 'com.chtwm.mall.activity.user.LaunchActivity',
            'noSign': True,
            #'skipServerInstallation': True,
            #'skipDeviceInitialization': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    @allure.feature('用例名称:登录恒天财富账号')
    def test_HengTian_001Login(self):
        """用例名称:用例名称:登录恒天财富账号"""
        driver = self.driver
        TestResult = Login.Login(driver)
        #登录恒天财富账号
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:打开恒天财富APP→进入我的界面')
    def test_HengTian_002IntoMyself_tv(self):
        """用例名称:打开恒天财富APP→进入我的界面"""
        driver = self.driver
        TestResult = IntoMyself_tv.IntoMyself_tv(driver)
        #进入我的界面
        assert TestResult == True

    @pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:实地派首页→测试商标图片——实地派会员专享权益（品牌宣传位）')
    def test_ShiDiPai_002Brand_Image(self):
        """用例名称:实地派首页→测试商标图片——实地派会员专享权益（品牌宣传位）"""
        driver = self.driver
        TestResult = ShiDiPai.Brand_Image(driver)
        # 点击商标图片——实地派会员专享权益（品牌宣传位）
        #self.assertTrue(TestResult)
        assert TestResult == True

    @pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:实地派首页→测试尊享服务')
    def test_ShiDiPai_003ZunXiangFuWu(self):
        """用例名称:实地派首页→测试尊享服务"""
        driver = self.driver
        TestResult = ShiDiPai.ZunXiangFuWu(driver)
        # 测试首页尊享服务
        #self.assertTrue(TestResult)
        #assert TestResult == True
        assert TestResult == False
        #故意写个错的查看报告

    @pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:实地派首页→测试精品楼盘')
    def test_ShiDiPai_004Recommend_Community_Title(self):
        """用例名称:实地派首页→测试精品楼盘"""
        driver = self.driver
        ShiDiPai.XiaLaPage(driver, 600)
        TestResult = ShiDiPai.Recommend_Community_Title(driver)
        # 测试首页精品楼盘
        #self.assertTrue(TestResult)
        assert TestResult == True

    @classmethod
    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()



if __name__ == "__main__":
    pytest.main(['start_001_HengTian_Login.py','--show-capture=no'])
    #pytest.main(["-s", "C:\\TANUKI\\Appium\\Hachi_Android\\src\\pytest\\start_001_ShiDiPai_AndroidTestRun.py"])
    #pytest.main(["-s","C:\\TANUKI\\Appium\\Hachi_Android\\src\\pytest\\start_001_ShiDiPai_AndroidTestRun.py", "--alluredir=D:\\jekins_allure\\fymallure-report"])
    #pytest.main(['-s', 'start_001_ShiDiPai_AndroidTestRun.py'])
    #pytest.main('start_001_ShiDiPai_AndroidTestRun.py')

