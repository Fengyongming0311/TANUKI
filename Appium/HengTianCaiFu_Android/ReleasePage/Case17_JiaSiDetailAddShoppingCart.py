__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class JiaSiDetailAddShoppingCart:
    def JiaSiDetailAddShoppingCart(driver, switch = 0):
        #print ("是否切换上下文和句柄开关的switch为：：：：：",switch)
        #print ("开始执行用例9....商品详情页面，商品添加购物车")
        if switch == 1:
            try:
                time.sleep(3)
                try:
                    driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
                except:
                    print ("try切换上下文没有切换成功，进入异常")
                    time.sleep(3)
                    driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
                    pass

                print("当前上下文current_context", driver.current_context)
                print ("#####################################################")
                Homepage_all_handles = driver.window_handles
                print ("全部句柄为：：：",Homepage_all_handles)
                nowhandle = driver.current_window_handle
                print("当前句柄为：：：=======>",nowhandle)
                for i in Homepage_all_handles:
                    if i != nowhandle:
                        New_handles = i
                        break

                time.sleep(3)
                print ("切换的新剧bing为...........",New_handles)
                driver.switch_to.window(New_handles)

                don = (driver.page_source).encode("gbk", 'ignore').decode("gbk", "ignore")
                print(don)

                #input("添加购物车添加购物车")

                #/html/body/wx-view/wx-view[2]/wx-view/wx-view[3]/wx-text/span[2]
                #/html/body/wx-view/wx-view[2]/wx-view/wx-view[3]
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[2]/wx-view/wx-view[3]").click()
                #                             /html/body/wx-view/wx-view[2]/wx-view/wx-view[3]
                #                             /html/body/wx-view/wx-view[2]/wx-view/wx-view[3]/wx-text
                #                             /html/body/wx-view/wx-view[2]/wx-view/wx-view[3]/wx-text/span[1]
                #                             /html/body/wx-view/wx-view[2]/wx-view/wx-view[3]/wx-text/span[2]
                #点击加入购物车
                time.sleep(5)
                #input("等待点击立即购买")

                #/html/body/wx-view/wx-view[2]/wx-view/wx-view[4]
                #/html/body/wx-view/wx-view[2]/wx-view/wx-view[4]/wx-text/span[1]
                #/html/body/wx-view/wx-view[2]/wx-view/wx-view[4]/wx-text/span[2]
                driver.find_element_by_xpath("/html/body/wx-view/wx-view[2]/wx-view/wx-view[4]").click()
                #点击立即购买
                time.sleep(7)

                unittest_TestResult = True
            except Exception as e:
                print("商品详情页面，商品添加购物车脚本报错信息为：", e)
                unittest_TestResult = False
            finally:
                return unittest_TestResult
        else:
            print ("没有切句柄，switch等于：：：：",switch)
            unittest_TestResult = False
            return unittest_TestResult
