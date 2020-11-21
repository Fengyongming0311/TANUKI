import time, re, os, sys
from appium import webdriver
import datetime
import subprocess


class Driver:
    driver=None
    xml_report_path = ''  # 报告路径
    html_report_path = ''

    @staticmethod
    def invoke(cmd):
        print(cmd)
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        print(errors)
        return o

def environment():
    huanjing = 1
    #1    为生产环境正式执行
    #2    为调试单条脚本
    return huanjing


def setup_module():
    desired_caps = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'noReset': True,
            'deviceName': 'oneplus-oneplus_a6000-92c14cac',
            'appPackage': 'com.chtwm.mall',
            # 上边这个肯定是对的
            'appActivity': 'com.chtwm.mall.activity.user.LaunchActivity',
            'noSign': True,
            # 'skipServerInstallation': True,
            # 'skipDeviceInitialization': True
    }
    Driver.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)
    #path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    #Driver.xml_report_path = os.path.join(path_dir, 'Report', 'xml')  # 报告路径
    #Driver.html_report_path = os.path.join(path_dir, 'Report', 'html',datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S'))

def teardown_module():
    time.sleep(3)
    Driver.driver.quit()
    #cmd = 'allure generate --clean %s -o %s' % (Driver.xml_report_path, Driver.html_report_path)
    #Driver.invoke(cmd)
    #--clean

