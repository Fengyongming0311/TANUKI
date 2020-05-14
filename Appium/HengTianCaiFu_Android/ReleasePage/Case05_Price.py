__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class Price:
    def Price(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例5....按照价格排序")
            time.sleep(3)
            driver.find_element_by_css_selector("wx-view[data-sortname=\"price\"][data-type=\"price\"]").click()
            #点击价格按照价格排序
            #debug:这里应该加入截图功能
            time.sleep(2)
            driver.find_element_by_css_selector("wx-view[data-sortname=\"price\"][data-type=\"price\"]").click()
            #再次点击返回原始排序
            unittest_TestResult = True

        except Exception as e:
            print ("选择价格脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult