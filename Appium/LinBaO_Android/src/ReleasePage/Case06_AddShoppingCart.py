__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class AddShoppingCart:
    def AddShoppingCart(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例6....商品添加购物车")
            time.sleep(3)
            driver.find_element_by_css_selector("wx-image[class=\"shop\"][role=\"img\"]").click()

            #<wx-image class="shop" src="../../images/shop.png" role="img"><div style="background-size: 100% 100%; background-repeat: no-repeat; background-image: url(&quot;images/shop.png&quot;);"></div><span></span></wx-image>
            #点击添加购物车图标，将商品添加购物车
            time.sleep(2)
            unittest_TestResult = True

        except Exception as e:
            print ("选择价格脚本报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult