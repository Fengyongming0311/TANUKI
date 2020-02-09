__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class Create_Time:
    def Create_Time(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例4....按照新品排序")
            driver.find_element_by_css_selector("wx-view[data-sortname=\"create_time\"][data-type=\"time\"]").click()
            #点击新品按照新品排序
            #debug:这里应该加入截图功能
            time.sleep(2)
            driver.find_element_by_css_selector("wx-view[data-sortname=\"create_time\"][data-type=\"time\"]").click()
            #再次点击返回原始排序
            unittest_TestResult = True

        except Exception as e:
            print ("选择新品脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult