__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
from selenium.webdriver.support.ui import WebDriverWait



class YXXMYanZheng:
    def YXXMYanZheng(driver):
        #进入销售管理——营销项目
        try:
            time.sleep(3)


            with allure.step('查看页面是否包含标题元素'):

                check = driver.find_element_by_css_selector("span[class=\"table-item-title ht-cust-project-title\"]")
                #<span title="000明泽视频见证-hui" class="table-item-title ht-cust-project-title">000明泽视频见证-hui</span>

                #print (check.text)
                #print (type(check.text))
                if check.text != '':
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
        except Exception as e:
            print("查看页面是否包含标题元素报错:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def IntoYXXM(driver):
        #营销项目——进入项目查看详细内容
        try:
            with allure.step('查看页面是否包含标题元素'):
                time.sleep(3)
                driver.find_element_by_css_selector("span[class=\"table-item-title ht-cust-project-title\"]").click()

                pytest_TestResult = True
        except Exception as e:
            pytest_TestResult = False
        finally:
            return pytest_TestResult


