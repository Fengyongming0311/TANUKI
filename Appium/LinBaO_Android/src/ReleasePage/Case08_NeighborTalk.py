__author__ = 'TANUKI'
# coding:utf-8
import time
###
import sys

sys.path.append("..")
from FilePublic_Page import Public_Page
import huadong
import random


###

class NeighborTalk:
    # 进入友邻
    def IntoNeighbor(driver):
        # 先点击我家按钮进入首页页面
        time.sleep(2)
        Public_Page.Switch_Navigation(driver, tab="友邻")
        time.sleep(2)

    # 点击发帖
    def IntoNewTopic(driver):
        driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_right_icon").click()

    # 选择发布类型
    def ChoiceSpeakType(driver, type):
        """
        点击选择发布类型
        :param type: 1.邻里分享,2.邻里互助,3.跳蚤市场
        :return: None
        """
        driver.wait_activity(".modules.neighbors.activities.NeighborSpeakActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/tv_choice_speak_type").click()
        driver.wait_activity(".modules.neighbors.activities.NeighborSpeakTypeActivity", 30)
        time.sleep(2)
        alltype = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_item_title")
        for i in alltype:
            if type == 1 and i.text == "邻里分享":
                i.click()
                break
            if type == 2 and i.text == "邻里互助":
                i.click()
                break
            if type == 3 and i.text == "跳蚤市场":
                i.click()
                break

    # 发帖子
    def PostNewTopic(driver, message, price=None, phone=None):
        try:
            if not price == None:
                driver.find_element_by_id("com.pujitech.pujiejia:id/et_business_price").send_keys(price)
                time.sleep(2)
                driver.find_element_by_id("com.pujitech.pujiejia:id/et_business_phone").send_keys(phone)

            time.sleep(2)
            # 下面是普通的输入内容
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_neighbor_speak_content").send_keys(message)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_right_text").click()
            # 点击发布

            unittest_TestResult = True
        except:
            unittest_TestResult = False
        finally:
            return unittest_TestResult
