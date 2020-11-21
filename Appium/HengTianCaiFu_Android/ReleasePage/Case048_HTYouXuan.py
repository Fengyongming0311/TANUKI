__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class HTYouXuan:
    def Into_HTYouXuan(driver):
        try:
            with allure.step('首页→左滑，显示恒天优选'):
                time.sleep(15)
                huadong.zuohua(driver, 500)

                time.sleep(3)
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "恒天优选":
                        i.click()
                        break

            pytest_TestResult = True

        except Exception as e:
            print("进入恒天优选报错:", e)
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
                time.sleep(5)
                print ("开始进入基金内部")
                pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                #层级往下定位
                for i in pr_names:
                    i.click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)

            for i in range(0,2):
                with allure.step('下滑查看下页三条数据'):
                    time.sleep(3)
                    huadong.shanghua(driver, 1000)
                    #下滑页面

                    pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                    #层级往下定位
                    for i in pr_names:
                        i.click()
                        time.sleep(3)
                        huadong.shanghua(driver, 300)
                        time.sleep(2)
                        driver.back()
                        time.sleep(2)

        except Exception as e:
            print("查看全部基金报错:", e)