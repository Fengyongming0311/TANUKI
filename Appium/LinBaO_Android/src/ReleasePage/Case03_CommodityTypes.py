__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class CommodityTypes:
    def CommodityTypes(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(2)
            #print ("开始执行用例3....")
            driver.find_element_by_css_selector("wx-view[data-model=\"全部分类\"][data-nav=\"2\"]").click()
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--aaa dropdownmenu--1" data-model="全部场景" data-nav="1"><wx-view class="dropdownmenu--nav-title">全部场景</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--bbb dropdownmenu--0" data-model="全部分类" data-nav="2"><wx-view class="dropdownmenu--nav-title">全部分类</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            time.sleep(2)
            #driver.find_element_by_xpath('//wx-view[text()="主卧"]').click()
            driver.find_element_by_xpath('//*[@id="goods_categories_0"]/wx-view[2]/wx-view/wx-view/wx-view[5]/wx-view').click()
            time.sleep(2)

            #开始验证是否选择分类切换为电视
            check = driver.find_element_by_xpath('//*[@id="goods_categories_0"]/wx-view[1]/wx-view')
            #<wx-view class="dropdownmenu--nav-child dropdownmenu--borders dropdownmenu--bbb dropdownmenu--2" data-model="主卧" data-nav="1"><wx-view class="dropdownmenu--nav-title">主卧</wx-view><wx-image class="dropdownmenu--img1" src="/images/sanJiao.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/sanJiao.png&quot;);"></div><span></span></wx-image></wx-view>
            #<wx-view class="dropdownmenu--nav-title">主卧</wx-view>
            #<wx-view class="dropdownmenu--nav-title">电视</wx-view>
            #//*[@id="goods_scenes_0"]/wx-view[1]/wx-view
            #//*[@id="goods_categories_0"]/wx-view[1]/wx-view
            #print ("验证选择的场景文本===============：",check.text)
            if check.text == "平板电视":
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="goods_categories_0"]/wx-view[1]/wx-view').click()
                # //*[@id="goods_categories_0"]/wx-view[1]/wx-view
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="goods_categories_0"]/wx-view[2]/wx-view/wx-view/wx-view[1]/wx-view').click()
                unittest_TestResult = True
            else:
                raise Exception("check.text不是电视，验证失败")
            #<wx-view class="dropdownmenu--nav-title">主卧</wx-view>

        except Exception as e:
            print ("选择场景执行脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult