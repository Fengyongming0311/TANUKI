__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class ZhiNengCreate_Time:
    def ZhiNengCreate_Time(driver):
        try:
            time.sleep(5)
            try:
                driver.find_element_by_css_selector("wx-view[data-sortname=\"create_time\"][data-type=\"time\"]").click()
                #<wx-view class="img-list fl-r" data-sortname="create_time" data-type="time"><wx-text class="navActive" style="vertical-align: middle; margin-right: 15px"><span style="display:none;">新品
                #点击新品按照新品排序
                #debug:这里应该加入截图功能
            except:
                print ("执行了这一步")
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[3]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[2]/wx-view[3]/wx-text/span[2]").click()
                #                             /html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[3]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[2]/wx-view[3]
                #/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[3]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[2]/wx-view[3]/wx-text/span[2]

            unittest_TestResult = True
        except Exception as e:
            print ("选择新品脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult