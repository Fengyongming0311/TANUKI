__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class SelectRoom:
    #选择家电场景
    def SelectRoom(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(2)
            #print ("开始执行用例2....")
            driver.find_element_by_css_selector("wx-view[data-model=\"全部场景\"][data-nav=\"1\"]").click()
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            time.sleep(2)
            #driver.find_element_by_xpath('//wx-view[text()="主卧"]').click()
            driver.find_element_by_xpath('//*[@id="goods_scenes_0"]/wx-view[2]/wx-view/wx-view/wx-view[8]/wx-view').click()
            #//*[@id="goods_scenes_0"]/wx-view[2]/wx-view/wx-view/wx-view[8]/wx-view
            #<wx-view class="dropdownmenu--sortitem-item" data-model="[object Object]">主卧</wx-view>
            #<wx-view class="dropdownmenu--sortitem-item" data-model="[object Object]">卧室</wx-view>
            time.sleep(2)

            #开始验证是否选择场景切换为主卧
            check = driver.find_element_by_css_selector("wx-view[class=\"dropdownmenu--nav-title\"]")
            #print ("验证选择的场景文本===============：",check.text)
            if check.text == "主卧":
                #####场景还得给选回去，不然分类下没商品了
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="goods_scenes_0"]/wx-view[1]/wx-view').click()
                # //*[@id="goods_scenes_0"]/wx-view[1]/wx-view
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="goods_scenes_0"]/wx-view[2]/wx-view/wx-view/wx-view[1]/wx-view').click()
                unittest_TestResult = True
            else:
                raise Exception("check.text不是主卧，验证失败")
            #<wx-view class="dropdownmenu--nav-title">主卧</wx-view>

        except Exception as e:
            print ("选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult