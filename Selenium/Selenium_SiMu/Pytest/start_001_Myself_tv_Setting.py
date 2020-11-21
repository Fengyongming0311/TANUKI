#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import time, re, os, sys

sys.path.append("..")


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Page001_Login import Login
from Page002_IntoSiMuXiaoShou import IntoSiMuXiaoShou
from Page003_IntoYingXiaoXiangMu import IntoYingXiaoXiangMu
from Public import *

class Test_HengTian_Setting():

    @allure.feature('用例名称:登录恒天财富账号')
    def test_Setting_001HomePageLogin(self):
        userid = "H029829"
        psw = "123456"

        driver = Driver.driver

        driver.get('https://core.uata.haomalljf.com/login.html')

        driver.implicitly_wait(30)
        TestResult = Login.Login(driver, userid, psw)

        assert TestResult == True


    @allure.feature('用例名称:进入私募销售页面')
    def test_Setting_002IntoSiMuXiaoShou(self):
        driver = Driver.driver
        TestResult = IntoSiMuXiaoShou.IntoSiMuXiaoShou(driver)

        assert TestResult == True

    @allure.feature('用例名称:进入销售管理页面')
    def test_Setting_003IntoYingXiaoXiangMu(self):
        driver = Driver.driver
        TestResult = IntoYingXiaoXiangMu.IntoYingXiaoXiangMu(driver)

        assert TestResult == True


if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_001_Myself_tv_Setting.py', "-s", "-v"])
