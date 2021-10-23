#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

from Pytest.Public import environment

sys.path.append("..")


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Page001_Login import Login
from Page002_IntoSiMuXiaoShou import IntoSiMuXiaoShou
from Page003_IntoYingXiaoXiangMu import IntoYingXiaoXiangMu
from Page004_YXXMYanZheng import YXXMYanZheng
from Page005_XMXQYanZheng import XMXQYanZheng
from Public import *

class Test_HengTian_Setting():

    @allure.feature('用例名称:登录恒天财富账号')
    def test_HTMZ_001HomePageLogin(self):
        userid = "H029829"
        psw = "123456"

        driver = Driver.driver

        driver.get('http://core.qasa.chtfund.com/login.html')
        driver.implicitly_wait(30)
        TestResult = Login.Login(driver, userid, psw)

        assert TestResult == True


    @allure.feature('用例名称:进入私募销售页面')
    def test_HTMZ_002IntoSiMuXiaoShou(self):
        driver = Driver.driver
        TestResult = IntoSiMuXiaoShou.IntoSiMuXiaoShou(driver)

        assert TestResult == True

    @allure.feature('用例名称:进入销售管理→营销项目页面')
    def test_HTMZ_003IntoYingXiaoXiangMu(self):
        driver = Driver.driver
        TestResult = IntoYingXiaoXiangMu.IntoYingXiaoXiangMu(driver)

        assert TestResult == True

    @allure.feature('用例名称:营销项目页面元素查看')
    def test_HTMZ_004YXXMYanZheng(self):
        driver = Driver.driver
        TestResult = YXXMYanZheng.YXXMYanZheng(driver)

        assert TestResult == True

    @allure.feature('用例名称:进入项目详细页面')
    def test_HTMZ_005IntoYXXM(self):
        driver = Driver.driver
        TestResult = YXXMYanZheng.IntoYXXM(driver)

        assert TestResult == True

    @allure.feature('用例名称:进入项目详细页面')
    def test_HTMZ_006XMXQYanZheng(self):
        driver = Driver.driver
        TestResult = XMXQYanZheng.XiangMuXiangQing(driver)

        assert TestResult == True


if __name__ == "__main__":
    ENV = environment()
    #print ("ENV ==========================",ENV)
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_001_YingXiaoXiangMu.py', "-s", "-v"])
