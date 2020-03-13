__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class JiaSiSelectScene:
    #选择家私场景
    def JiaSiSelectScene(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(2)

            #c = (driver.page_source).encode("gbk", 'ignore').decode("gbk", "ignore")
            #print(c)

            #<wx-dropdownmenu  class="goods_scenes" id="goods_scenes_1"><wx-view class="dropdownmenu--nav"><wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view></wx-view><wx-view class="dropdownmenu--container dropdownmenu--container_hd dropdownmenu--disappear"><wx-view class="dropdownmenu--z-height"><wx-view><wx-view class="dropdownmenu--sortitem"><wx-view class="dropdownmenu--sortitem-item dropdownmenu--active" data-model="[object Object]">全部分类
            try:
                driver.find_element_by_css_selector("wx-dropdownmenu[class=\"goods_scenes\"][id=\"goods_scenes_1\"]").click()
            except:
                driver.find_element_by_css_selector("wx-view[data-model=\"全部场景\"][data-nav=\"1\"]").click()
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            time.sleep(2)
            #driver.find_element_by_xpath('//wx-view[text()="主卧"]').click()
            driver.find_element_by_xpath('//*[@id="goods_scenes_1"]/wx-view[2]/wx-view/wx-view/wx-view[5]/wx-view').click()
            #//*[@id="goods_scenes_1"]/wx-view[2]/wx-view/wx-view/wx-view[5]/wx-view
            #选择北欧
            time.sleep(5)

            #开始验证是否选择场景切换为主卧
            #check = driver.find_element_by_css_selector("wx-view[class=\"dropdownmenu--nav-title\"]")这个定位不到
            check = driver.find_element_by_xpath("//*[@id=\"goods_scenes_1\"]/wx-view[1]/wx-view/wx-view")

            #print ("check.text内容为=====================",check.text)

            if check.text == "北欧":
                unittest_TestResult = True
            else:
                raise Exception("check.text不是北欧，验证失败")
            #<wx-view class="dropdownmenu--nav-title">北欧</wx-view>
            #<wx-view class="dropdownmenu--nav-title">北欧</wx-view>

        except Exception as e:
            print ("选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult