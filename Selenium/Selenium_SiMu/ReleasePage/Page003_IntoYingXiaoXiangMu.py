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
            time.sleep(5)
            #这里需要切换句柄

            nowwindow1 = driver.current_window_handle
            allwindows = driver.window_handles
            #print ("这个有可能是新窗口的页面句柄",nowwindow1)
            #获取所有窗口
            #print (allwindows)
            #print ("================================================")
            for smap in allwindows:
                #print(smap)
                if smap != nowwindow1:
                    driver.switch_to_window(smap)

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

