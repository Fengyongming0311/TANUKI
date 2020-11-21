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
title = "上传收入证明或金融资产证明"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class UploadAssetProve:
    def UploadAssetProve(driver):
        try:
            with allure.step('上传收入证明或金融资产证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/two_li", 60,3).click()
                #由于等待投资经历证明提交需要加长等待时间

            with allure.step('点击切换到上传金融资产证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv2", 5).click()

            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                        print ("删除之前上传过的照片成功")
                        allure.attach("删除之前上传过的照片成功")
                        time.sleep(1)
                except:
                    print ("删除之前上传过的照片失败")
                    allure.attach("删除之前上传过的照片失败")
                    pass

            with allure.step('点击+，上传图片'):
                try:
                    time.sleep(2)
                    Page.wait_elem(driver,"com.chtwm.mall:id/rel_no0", 5).click()
                except:
                    Page.wait_elem(driver,"com.chtwm.mall:id/iv_pic", 10).click()


            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()

            with allure.step('选择一张照片'):
                time.sleep(2)
                photos = driver.find_elements_by_id("com.chtwm.mall:id/v_selected")[0]
                #取第一张照片
                photos.click()

            with allure.step('点击右上方，完成按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/done", 5).click()


            with allure.step('点击下方提交按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_commit", 5).click()
                time.sleep(10)
                #等待十秒资料上传到服务器


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult



    def ZiGuan_UploadAssetProve(driver):
        try:
            with allure.step('上传收入证明或金融资产证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/rl_srzm", 60,3).click()
                #由于等待投资经历证明提交需要加长等待时间

            with allure.step('点击切换到个人资产证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_tab_02", 6).click()

            with allure.step("不知道是不是BUG，需要手动收起键盘"):
                time.sleep(5)
                print ("代码收起键盘操作")
                driver.hide_keyboard()



            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                        print ("删除之前上传过的照片成功")
                        allure.attach("删除之前上传过的照片成功")
                        time.sleep(1)
                except:
                    print ("删除之前上传过的照片失败")
                    allure.attach("删除之前上传过的照片失败")
                    pass

            with allure.step('点击+，上传图片'):
                try:
                    time.sleep(2)
                    Page.wait_elem(driver,"com.chtwm.mall:id/iv_add_img", 5).click()
                except:
                    Page.wait_elem(driver,"com.chtwm.mall:id/rl_upload_img", 10).click()

            '''
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            '''

            with allure.step('选择一张照片'):
                time.sleep(2)
                photos = driver.find_elements_by_id("com.chtwm.mall:id/v_selected")[0]
                #取第一张照片
                photos.click()

            with allure.step('点击右上方，完成按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/done", 5).click()


            with allure.step('点击下方提交按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 5).click()
                time.sleep(10)
                #等待十秒资料上传到服务器


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult


    def Prod_ZiGuan_UploadAssetProve(driver):
        try:
            #生产环境上传资管证明改了
            #with allure.step('上传收入证明或金融资产证明'):
                #time.sleep(5)
                #huadong.shanghua(driver,600)
                #Page.wait_elem(driver,"com.chtwm.mall:id/rl_srzm", 60,3).click()
                #由于等待投资经历证明提交需要加长等待时间（页面更改不从这里进入了）

            with allure.step('点击切换到个人资产证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_tab_02", 18,3).click()

            with allure.step("不知道是不是BUG，需要手动收起键盘"):
                time.sleep(5)
                print ("代码收起键盘操作")
                driver.hide_keyboard()



            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                        print ("删除之前上传过的照片成功")
                        allure.attach("删除之前上传过的照片成功")
                        time.sleep(1)
                except:
                    print ("删除之前上传过的照片失败")
                    allure.attach("删除之前上传过的照片失败")
                    pass

            with allure.step('点击+，上传图片'):
                try:
                    time.sleep(2)
                    Page.wait_elem(driver,"com.chtwm.mall:id/iv_add_img", 5).click()
                except:
                    Page.wait_elem(driver,"com.chtwm.mall:id/rl_upload_img", 10).click()

            '''
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            '''

            with allure.step('选择一张照片'):
                time.sleep(2)
                photos = driver.find_elements_by_id("com.chtwm.mall:id/v_selected")[0]
                #取第一张照片
                photos.click()

            with allure.step('点击右上方，完成按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/done", 15,3).click()


            with allure.step('点击下方立即申请'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 12,3).click()
                time.sleep(10)
                #等待十秒资料上传到服务器


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult





