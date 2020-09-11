__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page
import huadong


#继承Base类
class Login(Page):
    def __init__(self):
        Page.__init__(self)

    def Login(driver,userid, psw):
        # 恒天财富APP登录页面
        try:
            try:
                #time.sleep(3)
                #WebDriverWait(driver, 60).until(lambda x: driver.find_element_by_id("com.chtwm.mall:id/tv_commit")).click()
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_commit", 5).click()
                #Page.find_elem_id(driver,"com.chtwm.mall:id/tv_commit").click()
                #先尝试点击页面登录按钮
            except:
                print ("没有寻找到登录按钮...")
                pass
            with allure.step('输入自然人登录手机号'):
                Page.wait_elem(driver,"com.chtwm.mall:id/et_phone_NO", 30).send_keys(userid)
            #Page.find_elem_id(driver,"com.chtwm.mall:id/et_pwd").send_keys(psw)
            with allure.step('输入登录密码'):
                Page.wait_elem(driver,"com.chtwm.mall:id/et_pwd", 30).send_keys(psw)
            #Page.find_elem_id(driver,"com.chtwm.mall:id/bt_pwdlogin2").click()
            with allure.step('点击登录按钮'):
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_pwdlogin2", 30).click()
            pytest_TestResult = True

        except Exception as e:
            print ("登陆报错：",e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
