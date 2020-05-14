__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class JiaSiPrice:
    def JiaSiPrice(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            try:
                driver.find_element_by_css_selector("wx-view[data-sortname=\"price\"][data-type=\"price\"]").click()
                #点击价格按照价格排序
                #debug:这里应该加入截图功能
            except:
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[2]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[2]/wx-view[2]").click()

            unittest_TestResult = True
        except Exception as e:
            print ("选择价格脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult