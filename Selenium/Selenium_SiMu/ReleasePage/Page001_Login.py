__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
sys.path.append("../Base_Appium_Function")
from selenium.webdriver.support.ui import WebDriverWait


class Login():
    def Login(driver,userid, psw):
        #登录
        try:
            time.sleep(5)
            driver.find_element_by_css_selector('input[name=\"username\"][id=\"username\"]').send_keys(userid)
            #<input name="username" id="username" type="text" placeholder="请输入工号" maxlength="7" onfocus="this.placeholder=''" onblur="checkImgCode()" class="">
            #用户名
            driver.find_element_by_css_selector('input[name=\"password\"][id=\"password\"]').send_keys(psw)
            #<input name="password" id="password" type="password" placeholder="请输入密码" maxlength="20" onfocus="this.placeholder=''" onblur="this.placeholder='请输入密码'">
            #密码
            time.sleep(3)
            #driver.find_element_by_css_selector('a[class=\"btn_submit a_btn_submit disabled\"]').click()
            driver.find_element_by_xpath("//*[@id=\"login_form\"]/div/div[1]/div[6]").click()
            #<a onclick="login()" class="btn_submit a_btn_submit disabled"><span>立即登录</span><img class="arrow" src="img/arrow.png"></a>
            #//*[@id="login_form"]/div/div[1]/div[6]
            #登录
            pytest_TestResult = True

        except Exception as e:
            print ("登录报错：",e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
