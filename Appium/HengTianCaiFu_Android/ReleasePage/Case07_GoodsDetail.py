__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")

class GoodsDetail:
    def GoodsDetail(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例7....进入商品详情")
            time.sleep(3)
            Homepage_all_handles = driver.window_handles
            needhandle = driver.current_window_handle
            for i in Homepage_all_handles:
                if i != needhandle:
                    Detailpage_handles = i
                    break
            #print("当前上下文为,", needhandle)
            driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-swiper/div/div[1]/div/wx-swiper-item[1]/wx-scroll-view/div/div/div/wx-view/wx-view[2]/wx-view[3]/wx-view[1]").click()
            #按照xpath定位选择第一个商品 进入查看商品详情
            time.sleep(2)
            driver.implicitly_wait(10)

            #driver.switch_to_window(Detailpage_handles)这个方法是旧方法，不换成新的报warning
            driver.switch_to.window(Detailpage_handles)

            """
            #debug: 不行就切换三个handle，然后打印每个handle的页面信息
            for i in Detailpage_all_handles:
                time.sleep(3)
                print ("dondake当前句柄为",i)
                driver.switch_to_window(i)
                #print(driver.page_source ,encoding='utf-8')这个不对，会报错用下面的c的那个
                c = (driver.page_source).encode("gbk", 'ignore').decode("gbk", "ignore")
                print (c)
                #当时为了验证页面元素在哪个handle里，便打印了所有的handle下的page_source,最终找到了
            """

            """
            print ("#############################################33")
            contexts = driver.contexts
            print("contexts全部上下文",contexts)
            dondake = driver.current_context
            print ("当前上下文为:",dondake)
            """
            #print(driver.page_source)
            time.sleep(2)
            goodsname = driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view[1]")
            goodsprice = driver.find_element_by_xpath("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view[3]/wx-text[1]/span[2]")
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