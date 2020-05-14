__author__ = 'TANUKI'

# coding:utf-8
import time, sys

sys.path.append("..")
import huadong


class IntoMyself_tv:
    def IntoMyself_tv(driver):
        # 恒天财富APP进入我的页面
        try:
            # driver.wait_activity(".ui.LauncherUI", 30)
            driver.implicitly_wait(10)
            #隐式等待，等待页面加载
            #ac = driver.current_activity
            #print (ac)
            #
            driver.wait_activity(".activity.MainActivity", 30)
            #显式等待，元素为.activity.MainActivity
            driver.find_element_by_id("com.chtwm.mall:id/myself_tv").click()
            #点击我的按钮
            pytest_TestResult = True

        except Exception as e:
            print("进入我的页面报错信息==========:", e)
            pytest_TestResult = False
        finally:
            return pytest_TestResult
