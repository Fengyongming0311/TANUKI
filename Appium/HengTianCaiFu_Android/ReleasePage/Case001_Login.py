__author__ = 'TANUKI'

# coding:utf-8
import time, sys

sys.path.append("..")
import huadong
from PO_Base import Base
############
userid = '13263160105'
psw = 'Peter963'
############

class Login:
    def Login(driver):
        # 恒天财富APP登录页面
        try:
            #print ("开始执行登陆操作")
            time.sleep(3)
            driver.find_element_by_id("com.chtwm.mall:id/et_phone_NO").send_keys(userid)
            #输入手机号
            time.sleep(3)

            driver.find_element_by_id("com.chtwm.mall:id/et_pwd").send_keys(psw)
            #输入密码

            driver.find_element_by_id("com.chtwm.mall:id/bt_pwdlogin2").click()
            #点击登录按钮
            pytest_TestResult = True

        except Exception as e:
            print("进入我的页面报错信息==========:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
