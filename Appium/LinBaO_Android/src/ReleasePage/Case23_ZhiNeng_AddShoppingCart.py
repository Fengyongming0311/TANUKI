__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class ZhiNengAddShoppingCart:
    def ZhiNengAddShoppingCart(driver):
        try:
            driver.implicitly_wait(10)
            time.sleep(3)
            try:
                driver.find_element_by_css_selector("wx-image[class=\"shop\"][role=\"img\"]").click()
                # 点击添加购物车图标，将商品添加购物车
            except:
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[3]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[3]/wx-view[1]/wx-view[2]/wx-view[4]/wx-view[2]/wx-image").click()
                #                             /html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[3]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[3]/wx-view[1]/wx-view[2]/wx-view[4]/wx-view[2]/wx-image
            unittest_TestResult = True

        except Exception as e:
            print ("家私添加商品到购物车脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult