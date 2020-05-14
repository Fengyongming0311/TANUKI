__author__ = 'TANUKI'
# coding:utf-8
import time, sys

sys.path.append("..")
import huadong


class Into_ZhiNeng:
    def Into_ZhiNeng(driver):
        # 从微信进入到实地打造师小程序中
        try:
            driver.wait_activity(".ui.LauncherUI", 30)
            dibu = driver.find_elements_by_id("com.tencent.mm:id/dkb")
            for i in dibu:
                # print ("i的text为",i.text)
                if i.text == "发现":
                    i.click()
                    break
            # time.sleep(2)
            driver.wait_activity(".ui.LauncherUI", 30)
            xcx = driver.find_elements_by_id("android:id/title")
            for i in xcx:
                if i.text == "小程序":
                    i.click()
                    break
            time.sleep(2)
            # print(driver.context)

            # ac = driver.current_activity
            # print (ac)
            driver.wait_activity(".plugin.appbrand.ui.AppBrandLauncherUI", 30)
            time.sleep(2)

            shidi = driver.find_elements_by_id("com.tencent.mm:id/cg")
            for i in shidi:
                if i.text == "实地打造师":
                    i.click()
                    break
            # com.tencent.mm:id/cg
            # ac = driver.current_activity
            # print("实地打造师",ac)
            driver.wait_activity(".plugin.appbrand.ui.AppBrandUI", 30)

            # ac = driver.current_activity
            # print("实地打造师",ac)

            # contexts = driver.contexts
            # print("contexts全部上下文",contexts)
            # print ("############################################")
            # print("进入小程序后查看上下文",driver.context)
            # print("切换以后查看", driver.context)
            # time.sleep(5)
            # print(driver.page_source)

            # driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand2')
            # driver.switch_to.context('WEBVIEW_com.tencent.mm')
            # driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
            #这里切换上下文
            time.sleep(3)
            try:
                driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
            except:
                time.sleep(3)
                driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
                pass

            # print('切换成功')
            # print("当前上下文current_context", driver.current_context)
            # print("*****************************************")
            #print ("selenium获取全部handles和needhandle")
            time.sleep(5)
            all_handles = driver.window_handles
            # print("all_handles所有句柄为：", all_handles)
            # time.sleep(2)
            needhandle = driver.current_window_handle
            #print("needhandle,", needhandle)
            time.sleep(3)
            #debug：这块偶尔会报错，以后优化一下
            for i in all_handles:
                if i != needhandle:
                    #driver.switch_to_window(i)
                    driver.switch_to.window(i)
                    # print(i)
                    break

            # print("切换以后查看", driver.context)
            # print(driver.page_source)
            # print("测试点击网页")
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id=\"65\"]/wx-text/span[2]").click()
            #                             //*[@id="63"]/wx-text/span[2]
            #                             //*[@id="65"]/wx-text/span[2]
            #点击智能进入智能页面
            unittest_TestResult = True
        except Exception as e:
            print("进入实地打造师报错信息==========:", e)
            unittest_TestResult = False
        finally:
            return unittest_TestResult
