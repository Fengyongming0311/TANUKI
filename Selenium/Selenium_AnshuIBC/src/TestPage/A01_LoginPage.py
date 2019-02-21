__author__ = 'TANUKI'
#coding:utf-8
'''
A01.实现桉树登录页面
'''
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys     #引用Key包
from selenium.webdriver.common.action_chains import ActionChains    #解决下拉菜单引入
from selenium.webdriver.support.ui import WebDriverWait       #引用WebDriverWait包
import sys
sys.path.append('../Center/')
import start          #这个是为了读取start.py中的参数   下边是为了直接引用start.py中的类的
#from start import MainStart
#上边从start文件中引用MainStart类

class Z01_LoginPage:
    def LoginPage(driver):
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("username"))#wait
            driver.find_element_by_id("username").send_keys(start.username)
            #用户名输入
            #<input name="username" id="username" maxlength="30" placeholder="请输入用户名" autocomplete="off" class="layui-input" style="background-color: #fff;border: 1px solid #d7d7d7;border-radius: 2px;height: 42px;line-height: 42px;padding-left: 40px;" type="text">

            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("password"))#wait
            driver.find_element_by_id("password").send_keys(start.passwd)
            #<input name="password" id="password" maxlength="30" placeholder="请输入密码" autocomplete="off" class="layui-input" style="background-color: #fff;border: 1px solid #d7d7d7;border-radius: 2px;height: 42px;line-height: 42px;padding-left: 40px;" type="password">

            #输入验证码(验证码未被屏蔽)
            #yanzhengma = input("请输入验证码...:")
            #print ("输入的验证码为",yanzhengma)
            #WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id("validateCode"))#wait
            #driver.find_element_by_id("validateCode").send_keys(yanzhengma)

            time.sleep(8)


            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_css_selector("input[type=\"submit\"]"))#wait
            driver.find_element_by_css_selector("input[type=\"submit\"]").click()
            #<input class="layui-btn" style="width:100%;margin-top:12px;" value="登 录" type="submit">

        except Exception as e:
            print ("登录用户运行报错，报错信息为：",e)

        finally:
            pass



driver = webdriver.Chrome()
driver.get("http://beta.anshuspace.cn:10007/euc/home/page")
print (driver.title)

driver.maximize_window()

time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("topFrame")

time.sleep(3)

driver.find_element_by_css_selector("a[href=\"login.html\"][target=\"_parent\"]").click()


