__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page



class UploadZiChanProve:
    #上传资产证明
    def UploadZiChanProve(driver):
        try:
            with allure.step('切换到上传资产证明页面'):
                time.sleep(5)
                Page.wait_elem(driver,"com.chtwm.mall:id/tv_tab_02", 10, 2).click()

            with allure.step('上滑显示页面'):
                time.sleep(3)
                huadong.shanghua(driver, 1800)

            with allure.step('尝试删除之前上传过的照片记录'):
                time.sleep(3)
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
                    Page.wait_elem(driver,"com.chtwm.mall:id/rl_upload_img", 6).click()
                    #点击大图上传图片
                except:
                    Page.wait_elem(driver,"com.chtwm.mall:id/iv_add_img", 10).click()
                    ##点击小加号上传图片
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

            #立即申请后会弹出短信验证框
            with allure.step('点击下方立即申请按钮'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/bt_suction_bottom", 5).click()
                time.sleep(5)


            with allure.step('输入短信验证码，点击确认'):
                time.sleep(3)
                Page.wait_elem(driver,"com.chtwm.mall:id/et_input_code", 5).send_keys("753698")
                time.sleep(3)
                #Page.find_elem_id(driver,"com.chtwm.mall:id/tv_confirm").click()
                #暂不提交TANUKIdondake
                time.sleep(3)



            pytest_TestResult = True


        except Exception as e:
            #print("%s报错:"%title, e)
            allure.attach("%s报错:%s%s"%(title,str(e),str(type(e))))
            pytest_TestResult = False

        finally:
            return pytest_TestResult

