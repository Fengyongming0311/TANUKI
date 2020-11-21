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
title = "员工验证"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############


class StaffProve:
    def Into_StaffProve(driver):
        try:
            with allure.step('我的→员工验证'):
                time.sleep(3)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/myself_item_tv")
                for i in elems:
                    if i.text == title:
                        i.click()
                        pytest_TestResult = True
                        break

        except Exception as e:
            print("进入%s报错:"%title, e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult



    def StaffNo(driver, StaffNo, Staffname):
        try:
            print ("StaffNo====================",StaffNo)
            print ("Staffname==================",Staffname)
            with allure.step('输入员工信息，验证'):
                time.sleep(3)
                Page.find_elem_id(driver,"com.chtwm.mall:id/search_edit").send_keys(StaffNo)
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/search_tv").click()
                time.sleep(3)
                name = Page.wait_elem(driver,"com.chtwm.mall:id/item_staff_query_name_tv",8)
                if name.text == Staffname:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

                driver.back()

        except Exception as e:
            print("查看%s报错:"%title, e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult




    def StaffName(driver, Staffname):
        try:
            with allure.step('输入员工信息，验证'):
                time.sleep(3)
                Page.find_elem_id(driver,"com.chtwm.mall:id/search_edit").send_keys(Staffname)
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/search_tv").click()
                time.sleep(3)
                name = Page.wait_elem(driver,"com.chtwm.mall:id/item_staff_query_name_tv",8)
                if name.text == Staffname:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False

                driver.back()

        except Exception as e:
            print("查看%s报错:"%title, e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult