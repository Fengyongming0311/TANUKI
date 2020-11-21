__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
############
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
title = "风测说明"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class FengCeShuoMing:
    def FengCeShuoMing(driver):
        try:
            with allure.step('点击风险评测问号图片'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/user_info_found_img", 10).click()
            with allure.step('%s检查点截图'%title):
                time.sleep(2)
                allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
                #添加检查点截图，PrtScPath为图片位置

        except Exception as e:
            print("银行卡报错:", e)


    def FengCeShuoMingAPI_CheckPoint(*args):
        import http.client
        conn = http.client.HTTPSConnection("app.haomaojf.com")
        payload = "{\"contentBelong\":\"7\"}"
        headers = {
            'accept-encoding': 'gzip',
            'connection': 'Keep-Alive',
            'content-length': '21',
            'content-type': 'application/json; charset=utf-8',
            'cookie': 'APPSESSIONID=9d01c387-1837-4cb9-a5fa-c0a2ccf55be9; Domain=haomaojf.com; Path=/; HttpOnly; SameSite=Lax',
            'host': 'app.haomaojf.com',
            'jf-app-version': '3.8.0',
            'newcardlist': 'newCardList',
            'user-agent': 'okhttp/3.9.0',
            'Content-Type': 'text/plain'
        }
        conn.request("POST", "/app/content/frontend/getContent", payload, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        #接口返回值
        print (data)
        print (type(data))
        try:
            a,b = data.split("descr\":\"")

            checkpoint,delte = b.split("\",\"linkType")
            print("getContent接口返回数据为:",checkpoint)
            return checkpoint
        except Exception as e:
            return e


    def FengCeShuoMing_CheckPoint(driver):
        with allure.step('获取风测说明内容'):
            check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_content", 10)
            print ("UI自动化获取封测说明内容为：",check.text)
            if check.text != '':
                return True
            else:
                return False

    def FengCeShuoMing_PageBack(driver):
        try:
            with allure.step('点击确认（明白了）'):
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_confirm", 10).click()
        except:
            driver.back()