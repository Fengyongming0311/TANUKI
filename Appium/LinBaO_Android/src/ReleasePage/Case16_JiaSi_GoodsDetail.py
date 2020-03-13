__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class JiaSiGoodsDetail:
    def JiaSiGoodsDetail(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例16....进入商品详情")
            time.sleep(3)

            needhandle = driver.current_window_handle
            #目前页面在家私首页，获取家私页面上下文

            driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[2]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[3]/wx-view[1]/wx-view[2]/wx-view[2]").click()
            #按照xpath定位选择第一个商品 进入查看商品详情
            time.sleep(2)
            driver.implicitly_wait(10)


            Homepage_all_handles = driver.window_handles
            #进入到商品详情页面获取全部上下文，然后for循环，不等于家私首页的上下文就是详情的

            for i in Homepage_all_handles:
                if i != needhandle:
                    Detailpage_handles = i
                    break

            driver.switch_to.window(Detailpage_handles)
            print("切换webview上下文到商品详情页面成功")

            time.sleep(2)
            goodsname = driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view[1]")
            goodsprice = driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view[2]/wx-text[1]/span[2]")
            if goodsname.text != None:
                print ("商品名称:",goodsname.text)
                print ("商品价格:",goodsprice.text)
                unittest_TestResult = True
            else:
                raise Exception("商品名称为空，进入商品详情页面失败")
            unittest_TestResult = True


        except Exception as e:
            print ("选择价格最高的商品进入商品详情脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult