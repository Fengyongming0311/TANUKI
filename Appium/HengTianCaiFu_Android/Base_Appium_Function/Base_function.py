__author__ = 'TANUKI'
#coding:utf-8
"""
appium的二次封装
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class BaseFunction(object):
    #通过resource_id获取单个元素
    def find_elem_id(driver, element):
        """
        :param element: 定位方式为id，传入需要定位的元素
        """
        return driver.find_element_by_id("%s" %element)

    #显式等待单个元素，调用selenium中的WebDriverWait
    def wait_elem(driver, element, timeout = 5, poll_frequency = 0.5):
        return WebDriverWait(driver, timeout, poll_frequency).until(lambda x: driver.find_element_by_id("%s" %element))


    #显式等待activity
    def wait_ACT(driver, element, time):
        """
        :param element: 定位方式为id，传入需要定位的元素
        :param time: 等待时间
        """
        return driver.wait_activity("%s" %element, time)
