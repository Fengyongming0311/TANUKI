__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class JiaSiCreate_Time:
    def JiaSiCreate_Time(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            try:
                driver.find_element_by_css_selector("wx-view[data-sortname=\"create_time\"][data-type=\"time\"]").click()
                #点击新品按照新品排序
                #debug:这里应该加入截图功能
            except:
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[2]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[2]/wx-view[3]").click()

            unittest_TestResult = True
        except Exception as e:
            print ("选择新品脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult