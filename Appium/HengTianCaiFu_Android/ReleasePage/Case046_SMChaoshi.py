__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page


class SMChaoshi:
    def Into_SMChaoshi(driver):
        try:
            with allure.step('首页→私募超市'):
                time.sleep(8)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "私募超市":
                        i.click()
                        break
            pytest_TestResult = True

        except Exception as e:
            print("进入私募超市报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def LCInto_SMChaoshi(driver):
        try:
            with allure.step('理财→私募超市'):
                time.sleep(8)
                #com.chtwm.mall:id/myself_item_tv
                elems = driver.find_elements_by_id("com.chtwm.mall:id/tv_name")
                for i in elems:
                    if i.text == "私募超市":
                        i.click()
                        break
            pytest_TestResult = True

        except Exception as e:
            print("进入私募超市报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult



    def Switch_Category(driver, name):
        try:
            with allure.step('切换到%s列表'%name):
                time.sleep(3)
                tv_tab_title = driver.find_elements_by_id("com.chtwm.mall:id/tv_tab_title")
                for i in tv_tab_title:
                    if i.text == "%s"%name:
                        i.click()
                        break
        except Exception as e:
            print("切换分类报错:", e)

    def Zhaiquaninvest(driver):
        try:
            with allure.step('点击债权名称进入产品详情'):
                time.sleep(3)

                pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                #层级往下定位
                for i in pr_names:
                    i.click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)

            for i in range(0,5):
                with allure.step('下滑查看下页三条数据'):
                    time.sleep(3)
                    huadong.shanghua(driver, 500)
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


            pytest_TestResult = True


        except Exception as e:
            print("债权投资报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def Guquaninvest(driver):
        try:
            with allure.step('切换到股权投资列表'):
                time.sleep(3)
                #input("开始切换到股权投资")
                tv_tab_title = driver.find_elements_by_id("com.chtwm.mall:id/tv_tab_title")
                for i in tv_tab_title:
                    if i.text == "股权投资":
                        i.click()
                        break

            with allure.step('点击股权名称进入产品详情'):
                time.sleep(2)

                pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                #层级往下定位
                for i in pr_names:
                    i.click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)

            for i in range(0,4):
                with allure.step('下滑查看下页三条数据'):
                    time.sleep(3)
                    huadong.shanghua(driver, 500)
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


            pytest_TestResult = True


        except Exception as e:
            print("债权投资报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def Zhengquaninvest(driver):
        try:
            with allure.step('切换到证券投资列表'):
                time.sleep(3)
                #input("开始切换到证券投资")
                tv_tab_title = driver.find_elements_by_id("com.chtwm.mall:id/tv_tab_title")
                for i in tv_tab_title:
                    if i.text == "证券投资":
                        i.click()
                        break

            with allure.step('点击证券名称进入产品详情'):
                time.sleep(2)

                pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                #层级往下定位
                for i in pr_names:
                    i.click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)

            for i in range(0,3):
                with allure.step('下滑查看下页三条数据'):
                    time.sleep(3)
                    huadong.shanghua(driver, 500)
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


            pytest_TestResult = True


        except Exception as e:
            print("证券投资报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def Qitainvest(driver):
        try:
            with allure.step('切换到其他投资列表'):
                time.sleep(3)
                #input("开始切换到证券投资")
                tv_tab_title = driver.find_elements_by_id("com.chtwm.mall:id/tv_tab_title")
                for i in tv_tab_title:
                    if i.text == "其他":
                        i.click()
                        break

            with allure.step('点击其他进入产品详情'):
                time.sleep(2)

                pr_names = driver.find_elements_by_id("com.chtwm.mall:id/pr_name")
                #层级往下定位
                for i in pr_names:
                    i.click()
                    time.sleep(3)
                    driver.back()
                    time.sleep(2)

            for i in range(0,3):
                with allure.step('下滑查看下页三条数据'):
                    time.sleep(3)
                    huadong.shanghua(driver, 500)
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


            pytest_TestResult = True


        except Exception as e:
            print("其他投资报错:", e)
            pytest_TestResult = False
            driver.back()
        finally:
            return pytest_TestResult


    def ZQCategory(driver, Category):
        try:
            with allure.step('点击分类列表'):
                time.sleep(2)
                Page.find_elem_id(driver,"com.chtwm.mall:id/right_images").click()
            with allure.step("%s"%Category):
                time.sleep(3)
                names = driver.find_elements_by_id("com.chtwm.mall:id/text_aa")
                for i in names:
                    if i.text == "%s"%Category:
                        i.click()
                Page.wait_elem(driver,"com.chtwm.mall:id/filter_true",10).click()
                #点击确定
            with allure.step("滑动查看详情"):
                time.sleep(3)
                huadong.shanghua(driver,1000)
                time.sleep(8)
                huadong.shanghua(driver,1000)
                time.sleep(8)


        except Exception as e:
            print("债权条件筛选报错:", e)
            #pytest_TestResult = False
            #driver.back()
        finally:
            pass
            #return pytest_TestResult
