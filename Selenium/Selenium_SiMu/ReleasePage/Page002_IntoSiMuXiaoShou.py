__author__ = 'TANUKI'
# coding:utf-8
import time, sys
import allure
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait



class IntoSiMuXiaoShou:
    def IntoSiMuXiaoShou(driver):
        #进入私募销售页面
        try:
            time.sleep(5)
            with allure.step('点击私募销售按钮'):
                WebDriverWait(driver, 120).until(lambda x: x.find_element_by_css_selector("li[id=\"21\"]"))
                #<li id="21" onclick="jump(&quot;https://salesproject.uata.haomalljf.com&quot;)"><a><p><i class="icon icon-pos59"></i></p><p>私募销售</p></a></li>
                driver.find_element_by_css_selector("li[id=\"21\"]").click()

                pytest_TestResult = True

        except Exception as e:
            print("进入私募销售页面报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult


