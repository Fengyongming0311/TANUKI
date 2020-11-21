__author__ = 'TANUKI'

# coding:utf-8
import time, sys
import allure
sys.path.append("..")
import huadong
sys.path.append("../Base_Appium_Function")
from Base_function import BaseFunction as Page

class AllEquitys:
    def EveryEquitys(driver,vipnames):
        """
        :param vipnames: 传入权益内容名称
        :return:
        """
        try:
            time.sleep(5)
            tv_vips = driver.find_elements_by_id("com.chtwm.mall:id/tv_vip")
            #找到所有权益内容
            for i in tv_vips:
                if i.text == vipnames:
                    with allure.step('点击"%s"按钮'%vipnames):
                        i.click()
                    break
        except Exception as e:
            print("%s报错:" %vipnames, e)


    def EveryEquitys_CheckPoint(driver,vipnames):
        """
        :param vipnames: 传入权益内容名称
        :return: pytest结果
        """
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        PrtSc = now + vipnames
        #屏幕截图名称
        PrtScPath = "../Screenshots/%s.png" %PrtSc
        time.sleep(8)
        #driver.get_screenshot_as_file(PrtScPath)
        with allure.step('添加检查点截图'):
            allure.attach(driver.get_screenshot_as_png(),'%s' %PrtScPath,attachment_type=allure.attachment_type.PNG)
        time.sleep(3)
        with allure.step('点击"返回上一页面"，返回到消息中心页面'):
            driver.back()
        pytest_TestResult = True
        return pytest_TestResult