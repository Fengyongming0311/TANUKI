__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class IntoMessageCenter:
    def IntoMessageCenter(driver):
        #进入消息中心
        try:
            with allure.step('点击右上角"消息中心"按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/myself_message_img", 10).click()
            time.sleep(3)
        except Exception as e:
            print("进入消息中心报错:", e)
            pass
