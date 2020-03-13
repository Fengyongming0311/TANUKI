__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class ZhiNengCommodityTypes:
    def ZhiNengCommodityTypes(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(2)

            driver.find_element_by_css_selector("wx-dropdownmenu[class=\"goods_categories\"][id=\"goods_categories_2\"]").click()
            #

            time.sleep(5)

            driver.find_element_by_xpath('//*[@id="goods_categories_2"]/wx-view[2]/wx-view/wx-view/wx-view[11]/wx-view').click()
            time.sleep(5)

            #开始验证是否选择分类切换为家居照明
            check = driver.find_element_by_xpath('//*[@id="goods_categories_2"]/wx-view[1]/wx-view/wx-view')
            #//*[@id="goods_categories_2"]/wx-view[1]/wx-view/wx-view

            print ("验证选择的场景文本===============：",check.text)

            if check.text == "家居照明":
                unittest_TestResult = True
            else:
                raise Exception("check.text不是家居照明，验证失败")

        except Exception as e:
            print ("家私选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult