import time, re, os, sys
#导入selenium模块
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import subprocess


class Driver:
    driver = None
	#下面这个不是我写的，不太懂啥意思 到return o结束
    #xml_report_path = ''  # 报告路径
    #html_report_path = ''

    @staticmethod
    def invoke(cmd):
        print(cmd)
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        print(errors)
        return o



def environment():
    huanjing = 2
    #1    为生产环境正式执行
    #2    为调试单条脚本
    return huanjing



def setup_module():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    #解决您的连接不是私密连接的网站
    #Driver.driver = webdriver.Chrome(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    Driver.driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe',options = options)
    Driver.driver.maximize_window()


def teardown_module():
    time.sleep(3)
    #Driver.driver.quit()