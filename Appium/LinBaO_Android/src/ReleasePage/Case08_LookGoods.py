__author__ = 'TANUKI'
# coding:utf-8
import time,sys
sys.path.append("..")
import huadong

class LookGoods:
    def LookGoods(driver):
        try:
            driver.implicitly_wait(10)
            #print ("开始执行用例8....商品详情页面，滑动查看商品内容")
            time.sleep(3)

            #c = (driver.page_source).encode("gbk", 'ignore').decode("gbk", "ignore")
            #print(c)

            contexts = driver.contexts
            #print("contexts全部上下文", contexts)
            #
            try:
                driver.switch_to.context('NATIVE_APP')
            except:
                pass

            print("当前上下文current_context", driver.current_context)
            print("contexts全部上下文", contexts)

            for i in range(1,14):
                #print ("第",i,"次滑动")
                time.sleep(1)
                huadong.shanghua(driver,500)

            for i in range(1,8):
                time.sleep(1)
                huadong.xiahua(driver,250)

            unittest_TestResult = True
        except Exception as e:
            print ("Case008查看商品详情报错信息为：",e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult