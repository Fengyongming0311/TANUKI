__author__ = 'TANUKI'
import time
import random

import sys
sys.path.append("..")
sys.path.append("../Public/PublicProgram/")
from name import CrateNamepy
from phone import CratePhoneNopy

class Public_Page:
    #进入登录页面后的登录功能
    def DengLu(driver, username, password):
        '''
        用户登录页面
        '''
        try:
            time.sleep(3)
            driver.find_element_by_id("com.pujitech.pujiejia:id/login_password_phone_edt").clear()
            #先清一下文本
            driver.find_element_by_id("com.pujitech.pujiejia:id/login_password_phone_edt").send_keys(username)
            #输入用户名
            #com.pujitech.pujiejia:id/et_login_username
            #2019.4.24 发现改为com.pujitech.pujiejia:id/login_password_phone_edt

            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/login_password_password_edt").send_keys(password)
            #输入密码
            #com.pujitech.pujiejia:id/et_login_password
            #2019.4.24 发现改为com.pujitech.pujiejia:id/login_password_password_edt

            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/login_password_perform_btn").click()
            #com.pujitech.pujiejia:id/btn_login
            #2019.4.24发现改为com.pujitech.pujiejia:id/login_password_perform_btn
            #点击立即登录

            denglu = True
            return denglu


        except:
            denglu = False
            return denglu

    def Dengchu(driver):
        """
        先决条件：在我家页面
        :return: None
        """
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_setting").click()
        #点击进入设置

        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/rl_login_out").click()
        #点击退出按钮

        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
        #点击确认
        try:
            daki = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_content")
            if daki.text == "楼盘不存在，请重新选择楼盘！":
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
                Public_Page.ChoiceBuilding(driver, Building = "中山璟湖城")
        except:
            pass



    #切换导航栏功能
    def Switch_Navigation(driver, tab):
        """
        切换导航栏功能
        :return: None
        """
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            time.sleep(2)
            allbutn = driver.find_elements_by_id("com.pujitech.pujiejia:id/fixed_bottom_navigation_title")
            for target in allbutn:
                if target.text == tab:
                    target.click()
                    break
                # 点完了就跳出循环，否则会再次找寻case内容导致报错
        except Exception as e:
            print (e)
            print("未切换到%s页面，程序退出...."%tab)
            pass

    #给出一个随机数，判断上滑下滑
    def RandomNum():
        num = random.randint(0,1)
        return num

    #随机获取用户姓名
    def CrateName(number):
        import os
        file_path = os.getcwd()
        #获取当前文件路径
        dirname, delname = os.path.split(file_path)
        txtpath = dirname + "\\Public\\PublicProgram\\"
        #重新拼接路径
        return CrateNamepy.run(number, txtpath)


    #随机获取手机号
    def CratePhoneNo(num):
        return CratePhoneNopy.run(num)

    def NomalTest(driver, title, find_element_id, check_element_id,
                  MainWait_Element = None, Wait_Element = None, YESBack = True, TestCase = None):
        '''
        测试每个按钮点击进入查看功能是否正常
        :param title: 进入后页面title名称
        :param MainWait_Element: 等待主程序的wait_activity
        :param find_element_id: 找寻元素的resource-id
        :param Wait_Element: 等待页面的wait_activity
        :param check_element_id: 被检测元素的resource-id
        :param YESBack = True 退回上一页面， YESBack = False 不退回上一页面
        :return: None
        '''
        if TestCase == None:
            casetitle = title
        else:
            casetitle = TestCase
        try:
            if MainWait_Element == None:
                print (Public_Page.huoquactivity(driver))
            else:
                driver.wait_activity("%s"%MainWait_Element, 30)
                #等待我家主界面activity
                time.sleep(2)
            try:
                #这块逻辑不对，如果不定义title每次会点击同一个元素
                driver.find_element_by_id("%s"%find_element_id).click()
            except:
                find_element_id.click()

            if Wait_Element == None:
                print(Public_Page.huoquactivity(driver))
            else:
                driver.wait_activity("%s"%Wait_Element, 30)
                time.sleep(2)

            checkpoint = driver.find_element_by_id("%s"%check_element_id)
            if checkpoint.text == title and YESBack == True:
                driver.back()
                print("测试点击%s用例Passed............成功" %casetitle)
            elif checkpoint.text == title and YESBack == False:
                pass
            else:
                print("测试点击%s用例失败dondake............Failed" %casetitle)


        except:
            print ("测试点击%s用例失败............Failed"%casetitle)
            pass


    def debug_NomalTest(driver, title, find_element_id, check_element_id,
                  MainWait_Element = None, Wait_Element = None, YESBack = True, TestCase = None):
        '''
        测试每个按钮点击进入查看功能是否正常
        :param title: 进入后页面title名称
        :param MainWait_Element: 等待主程序的wait_activity
        :param find_element_id: 找寻元素的resource-id
        :param Wait_Element: 等待页面的wait_activity
        :param check_element_id: 被检测元素的resource-id
        :param YESBack = True 退回上一页面， YESBack = False 不退回上一页面
        :param TestCase: 定义为要点击的元素名称
        :param casetitle: 返回测试结果名称的参数，也当作需要点击的对象
        :return: None
        '''
        if TestCase == None:
            casetitle = title
        else:
            casetitle = TestCase
        try:
            if MainWait_Element == None:
                print (Public_Page.huoquactivity(driver))
            else:
                driver.wait_activity("%s"%MainWait_Element, 30)
                #等待我家主界面activity
                time.sleep(2)

            try:
                #这里点击定位的元素，逻辑上先选择点击带有名称的元素，如果报错了进入except流程
                dondake = driver.find_elements_by_id("%s" % find_element_id)#这里获取所有要查找的元素
                for target in dondake:
                    if target.text == casetitle:
                        target.click()
                        break
            except:
                driver.find_element_by_id("%s" % find_element_id).click()
                #find_element_id.click()  之前是这么写的但是感觉走不通...当时可能没走脑子

            if Wait_Element == None:
                print(Public_Page.huoquactivity(driver))
            else:
                driver.wait_activity("%s"%Wait_Element, 30)
                time.sleep(2)
            try:
                #定位到元素则判断，没定位到进入异常driver.back()退出程序
                checkpoint = driver.find_element_by_id("%s"%check_element_id)

                if checkpoint.text == title and YESBack == True:
                    driver.back()
                    print("测试点击%s用例Passed............成功" % casetitle)
                elif checkpoint.text == title and YESBack == False:
                    pass
                elif checkpoint.text != title and YESBack == True:
                    driver.back()
                    print("页面标题与测试Title不符...返回上一页...")
                else:
                    print("测试点击%s用例失败dondake............Failed" % casetitle)
            except:
                print (title + "没有定位到Title，返回上一页面...")
                driver.back()




        except Exception as e:
            print (e)
            print ("测试点击%s用例失败............Failed"%casetitle)
            pass

    #随机切换楼盘
    def RandomBuilding(driver):
        """
        先决条件：进入实地派
        :return: None
        """
        driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
        time.sleep(2)
        driver.find_element_by_id("com.pujitech.pujiejia:id/rl_building_name_container").click()
        #选择标题进入切换楼盘页面

        driver.wait_activity(".modules.city.views.activities.BuildingActivity", 30)
        time.sleep(2)

        AllBuilding = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_city")

        rondomnum = random.randint(0,2)
        #修改选择楼盘范围0是第一个
        RandomBuilding = AllBuilding[rondomnum]
        time.sleep(1)

        RandomBuilding.click()
        #选择完楼盘自动跳转到实地派页面

    #指定切换楼盘
    def ChoiceBuilding(driver, Building, into = "No"):
        """
        先决条件：进入实地派页面
        :param Building 传入楼盘名称
        :param into 判断需不需要进入选楼盘页面，Yes需要点击进入楼盘页面，No不需要点击进入楼盘页面，默认为no
        :return: None
        """
        if into == "No":
            driver.wait_activity(".modules.city.views.activities.BuildingActivity", 30)
            time.sleep(2)

            AllBuilding = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_city")

            for i in AllBuilding:
                if i.text == Building:
                    time.sleep(2)
                    i.click()
                    break
        elif into == "Yes":
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)

            driver.find_element_by_id("com.pujitech.pujiejia:id/rl_building_name_container").click()
            #点击后进入选择楼盘页面
            time.sleep(3)
            AllBuilding = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_city")

            for i in AllBuilding:
                print (i.text)
                if i.text == Building:
                    time.sleep(2)
                    i.click()
                    break




    #您没有在该小区认证房间
    def NoHomeInThisBuilding(driver):
        try:
            time.sleep(6)
            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_content")
            if checkpoint.text == "您没有在该小区认证房间":
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_cancel").click()
        except:
            pass

    def ExitBack(driver):
        #只要页面有<按钮就能返回上一页面
        driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()

    """
    获取当前页面的activity-------使用方法：
    dondake = Public_Page.huoquactivity(driver)
    print (dondake)
    """
    def huoquactivity(driver):
        time.sleep(5)
        ac = driver.current_activity
        return ac



