__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
xttztitle = "系统通知"
cpggtitle = "产品公告"
hdtztitle = "活动通知"
jydttitle = "交易动态"
#*****************
xttz = now + xttztitle
cpgg = now + cpggtitle
hdtz = now + hdtztitle
jydt = now + jydttitle
#屏幕截图名称
xttzPath = "../Screenshots/%s.png" %xttz
cpggPath = "../Screenshots/%s.png" %cpgg
hdtzPath = "../Screenshots/%s.png" %hdtz
jydtPath = "../Screenshots/%s.png" %jydt
############

class MessagePage:
    def XiTongTongZhi(driver):
        with allure.step('点击"系统通知"按钮进入系统通知页面'):
            time.sleep(6)
            driver.tap([(216,348)])
        #[216,348][1332,440]
        time.sleep(8)
        #点击系统通知
        #driver.get_screenshot_as_file(xttzPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %xttzPath,attachment_type=allure.attachment_type.PNG)
        with allure.step('点击"返回上一页面"，返回到消息中心页面'):
            driver.back()
        xttz_TestResult = True
        return xttz_TestResult


    def ChanPinGongGao(driver):
        time.sleep(6)
        with allure.step('点击"产品公告"按钮进入产品公告页面'):
            driver.tap([(216,672)])
        #[216,672][1332,764]
        #点击产品公告
        time.sleep(8)
        #driver.get_screenshot_as_file(cpggPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %cpggPath,attachment_type=allure.attachment_type.PNG)
        #产品公告快照
        time.sleep(1)
        with allure.step('点击"返回上一页面"，返回到消息中心页面'):
            driver.back()
        cpgg_TestResult = True
        return cpgg_TestResult

    def HuoDongTongZhi(driver):
        time.sleep(6)
        with allure.step('点击"活动通知"按钮进入活动通知页面'):
            driver.tap([(216,992)])
        #[216,992][1332,1084]
        #点击活动通知
        time.sleep(8)
        #driver.get_screenshot_as_file(hdtzPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %hdtzPath,attachment_type=allure.attachment_type.PNG)
        #活动通知快照
        time.sleep(1)
        with allure.step('点击"返回上一页面"，返回到消息中心页面'):
            driver.back()
        hdtz_TestResult = True
        return hdtz_TestResult

    def JiaoYiDongTai(driver):
        time.sleep(6)
        with allure.step('点击"交易动态"按钮进入交易动态页面'):
            driver.tap([(216,1316)])
        #[216,1316][1332,1408]
        #点击交易动态
        time.sleep(8)
        #driver.get_screenshot_as_file(jydtPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %jydtPath,attachment_type=allure.attachment_type.PNG)
        #交易动态快照
        time.sleep(1)
        with allure.step('点击"返回上一页面"，返回到消息中心页面'):
            driver.back()
        jydt_TestResult = True
        return jydt_TestResult