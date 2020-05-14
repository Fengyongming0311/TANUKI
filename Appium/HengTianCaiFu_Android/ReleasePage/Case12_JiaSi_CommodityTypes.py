__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class JiaSiCommodityTypes:
    def JiaSiCommodityTypes(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(2)

            driver.find_element_by_css_selector("wx-dropdownmenu[class=\"goods_categories\"][id=\"goods_categories_1\"]").click()
            #<wx-dropdownmenu is="component/dropdownmenu/dropdownmenu" class="goods_categories" id="goods_categories_1"><wx-view class="dropdownmenu--nav"><wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--bbb dropdownmenu--1" data-model="全部分类" data-nav="2"><wx-view class="dropdownmenu--nav-title">全部分类</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view></wx-view><wx-view class="dropdownmenu--container dropdownmenu--container_hd dropdownmenu--disappear"><wx-view class="dropdownmenu--z-height"><wx-view><wx-view class="dropdownmenu--sortitem"><wx-view class="dropdownmenu--sortitem-item dropdownmenu--active" data-model="[object Object]">全部分类
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--bbb dropdownmenu--1" data-model="全部分类" data-nav="2"><wx-view class="dropdownmenu--nav-title">全部分类</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            time.sleep(5)

            driver.find_element_by_xpath('//*[@id="goods_categories_1"]/wx-view[2]/wx-view/wx-view/wx-view[8]/wx-view').click()
            #                             //*[@id="goods_categories_1"]/wx-view[2]/wx-view/wx-view/wx-view[8]/wx-view
            time.sleep(5)

            #开始验证是否选择分类切换为茶几
            check = driver.find_element_by_xpath('//*[@id="goods_categories_1"]/wx-view[1]/wx-view')
            #//*[@id="goods_categories_1"]/wx-view[1]/wx-view

            print ("验证选择的场景文本===============：",check.text)

            if check.text == "茶几":
                unittest_TestResult = True
            else:
                raise Exception("check.text不是茶几，验证失败")
            #<wx-view class="dropdownmenu--nav-title">主卧</wx-view>

        except Exception as e:
            print ("家私选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult