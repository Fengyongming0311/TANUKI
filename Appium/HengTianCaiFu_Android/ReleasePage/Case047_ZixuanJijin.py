__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class ZixuanJijin:
    def Into_ZixuanJijin(driver):
        try:
            with allure.step('首页→左滑，显示自选基金'):
                time.sleep(15)
                huadong.zuohua(driver, 500)

                time.sleep(3)
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "自选基金":
                        i.click()
                        break

            pytest_TestResult = True

        except Exception as e:
            print("进入自选基金报错:", e)
            pytest_TestResult = False

        finally:
            return pytest_TestResult


    def Switch_Category(driver, name):
        try:
            with allure.step('切换到%s列表'%name):
                time.sleep(5)
                tv_tab_title = driver.find_elements_by_id("com.chtwm.mall:id/tv_tab_title")
                for i in tv_tab_title:
                    if i.text == "%s"%name:
                        i.click()
                        break
        except Exception as e:
            print("切换分类报错:", e)


    def AllFund(driver):
        try:
            with allure.step("通过基金名称查看基金"):
                time.sleep(8)
                print ("开始进入基金内部")
                names = driver.find_elements_by_id("com.chtwm.mall:id/tv_number")
                #层级往下定位
                for i in names:
                    time.sleep(3)
                    print (i.text)
                    i.click()
                    time.sleep(8)
                    driver.back()

        except Exception as e:
            print("查看全部基金报错:", e)



    def FundRanking(driver):
        try:
            with allure.step("通过基金名称查看基金"):
                time.sleep(3)
                i = driver.find_element_by_id("com.chtwm.mall:id/tv_product_name").click()
                time.sleep(3)
                print (i.text)
                i.click()
                time.sleep(3)
                driver.back()

        except Exception as e:
            print("查看全部基金报错:", e)