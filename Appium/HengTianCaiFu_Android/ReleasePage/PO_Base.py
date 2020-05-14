__author__ = 'TANUKI'
#coding:utf-8
"""
appium的二次封装
"""
from appium import webdriver

class Base:
    #通过resource_id获取单个元素
    def find_elem_id(driver, element):
        """
        :param element: 定位方式为id，传入需要定位的元素
        """
        return driver.find_element_by_id("%s" %element)

    #显示等待页面元素
    def wait_elem(driver,element, time):
        """
        :param element: 定位方式为id，传入需要定位的元素
        :param time: 等待时间
        """
        return driver.wait_activity("%s" %element, time)
