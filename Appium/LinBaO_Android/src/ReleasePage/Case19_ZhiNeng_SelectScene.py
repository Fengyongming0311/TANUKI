__author__ = 'TANUKI'
# coding:utf-8
import time

###
import sys
from selenium import webdriver
sys.path.append("..")



############################################
class ZhiNengSelectScene:
    #选择智能场景
    def ZhiNengSelectScene(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(5)

            try:
                driver.find_element_by_css_selector("wx-dropdownmenu[class=\"goods_scenes\"][id=\"goods_scenes_2\"]").click()
                #<wx-dropdownmenu is="component/dropdownmenu/dropdownmenu" class="goods_scenes" id="goods_scenes_2"><wx-view class="dropdownmenu--nav"><wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--active dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view></wx-view><wx-view class="dropdownmenu--container dropdownmenu--container_hd dropdownmenu--show"><wx-view class="dropdownmenu--z-height"><wx-view><wx-view class="dropdownmenu--sortitem">

            except:
                driver.find_element_by_css_selector("wx-view[data-model=\"全部场景\"][data-nav=\"1\"]").click()
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--active dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>

            time.sleep(2)
            #driver.find_element_by_xpath('//wx-view[text()="主卧"]').click()
            driver.find_element_by_xpath('//*[@id="goods_scenes_2"]/wx-view[2]/wx-view/wx-view/wx-view[2]/wx-view').click()
            #//*[@id="goods_scenes_1"]/wx-view[2]/wx-view/wx-view/wx-view[5]/wx-view
            #选择全屋
            time.sleep(5)

            #开始验证是否选择场景切换为全屋
            #check = driver.find_element_by_css_selector("wx-view[class=\"dropdownmenu--nav-title\"]")
            check = driver.find_element_by_xpath("//*[@id=\"goods_scenes_2\"]/wx-view[1]/wx-view/wx-view")

            print ("check.text内容为=====================",check.text)

            if check.text == "全屋":
                unittest_TestResult = True
            else:
                raise Exception("check.text不是全屋，验证失败")
            #<wx-view class="dropdownmenu--nav-title">北欧</wx-view>
            #<wx-view class="dropdownmenu--nav-title">北欧</wx-view>

        except Exception as e:
            print ("选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult