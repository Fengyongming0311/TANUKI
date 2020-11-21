__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait



class IntoYingXiaoXiangMu:
    def IntoYingXiaoXiangMu(driver):
        #进入销售管理——营销项目
        try:
            with allure.step('进入销售管理——营销项目'):
                WebDriverWait(driver, 60).until(lambda x: x.find_element_by_css_selector("a[id=\"projectList\"][class=\"menu_link\"]"))
                driver.find_element_by_css_selector("a[id=\"projectList\"][class=\"menu_link\"]").click()
                #<a id="projectList" class="menu_link">营销项目</a>
                pytest_TestResult = True
        except Exception as e:
            print("进入销售管理——营销项目报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult




    def IntoSetting_CheckPoint(driver):
        time.sleep(2)
        with allure.step('验证标题是否为设置'):
            check = Page.find_elem_id(driver,"com.chtwm.mall:id/tv_title")
        if check.text == "设置":
            pytest_TestResult = True
        else:
            pytest_TestResult = False
        return pytest_TestResult