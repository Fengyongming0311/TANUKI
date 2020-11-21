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
title = "上传投资经历证明"
PrtSc = now + title
#屏幕截图名称
PrtScPath = "../Screenshots/%s.png" %PrtSc
############
class UploadInvestProve:
    def UploadInvestProve(driver):
        try:
            with allure.step('点击普转专页面的上传投资经历证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/one_li", 10).click()

            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                    print ("删除之前上传过的照片成功")
                    allure.attach("删除之前上传过的照片成功")
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
            '''
            with allure.step('点击相机，上传拍摄的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/camera_tv", 5).click()
            
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            '''
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
                time.sleep(5)


            pytest_TestResult = True
            return pytest_TestResult


        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False
            return pytest_TestResult

    def ZiGuan_UploadInvestProve(driver):
        try:
            with allure.step('点击普转专页面的上传投资经历证明'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/rl_tzjl", 10).click()

            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                    print ("删除之前上传过的照片成功")
                    allure.attach("删除之前上传过的照片成功")
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
            with allure.step('点击相机，上传拍摄的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/camera_tv", 5).click()
            
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            
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
                #等待十秒上传资料到服务器


            pytest_TestResult = True



        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False

        finally:
            return pytest_TestResult


    def Prod_ZiGuan_UploadInvestProve(driver):
        try:
            #这块需求改了？？得点击下方的上传证明页面？？？
            with allure.step('点击上传证明'):
                time.sleep(5)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 24,3).click()

            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(2)
                try:
                    for i in range(4):
                        #尝试删除4次之前上传的图片
                        Page.wait_elem(driver,"com.chtwm.mall:id/iv_del", 5).click()
                    print ("删除之前上传过的照片成功")
                    allure.attach("删除之前上传过的照片成功")
                except:
                    print ("删除之前上传过的照片失败")
                    allure.attach("删除之前上传过的照片失败")
                    pass

            with allure.step('点击+，上传图片'):
                try:
                    time.sleep(3)
                    Page.wait_elem(driver,"com.chtwm.mall:id/iv_add_img", 12,3).click()
                except:
                    Page.wait_elem(driver,"com.chtwm.mall:id/rl_upload_img", 12,3).click()
            '''
            with allure.step('点击相机，上传拍摄的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/camera_tv", 5).click()
            
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            
            with allure.step('点击相册，上传相册中的照片'):
                time.sleep(2)
                Page.wait_elem(driver,"com.chtwm.mall:id/photo_tv", 5).click()
            '''
            with allure.step('选择一张照片'):
                time.sleep(5)
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
                #等待十秒上传资料到服务器


            pytest_TestResult = True



        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False

        finally:
            return pytest_TestResult


    '''
    def ProInvestors_CheckPoint(driver):
        try:
            with allure.step('检查标题'):
                time.sleep(1)
                check = Page.wait_elem(driver,"com.chtwm.mall:id/tv_title2", 10)
                if check.text == title:
                    pytest_TestResult = True
                else:
                    pytest_TestResult = False
            with allure.step('输出客户姓名'):
                tv_name = Page.wait_elem(driver,"com.chtwm.mall:id/tv_name", 10)
                print ("客户姓名：",tv_name.text)


            with allure.step('输出投资者类型'):
                tv_type = Page.wait_elem(driver,"com.chtwm.mall:id/tv_invest_type", 10)
                print ("投资者类型：",tv_type.text)

        except Exception as e:
            print("检查点%s报错:"%title, e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
    '''



