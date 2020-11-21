#coding=utf-8
__author__ = 'TANUKI'

import pytest
import allure
import sys

sys.path.append("..")


sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case001_Login import Login
from Case002_IntoMyself_tv import IntoMyself_tv
from Case012_IntoMyself_Equity import IntoMyself_Equity
from Case013_AllEquitys import AllEquitys
from public import *

class Test_HengTian_Myself_Equity:


    @allure.feature('用例名称:登录恒天财富账号')
    def test_Myself_Equity_001Login(self):
        """
        前置条件：
        安装恒天财富APP
        测试步骤：
        1.Appium启动恒天财富APP
        2.如未直接进入登陆页面，则在首页点击"登录"按钮
        3.输入自然人的11位手机号(账号)
        4.输入登陆密码
        5.点击登录按钮
        期望结果：
        登录成功，页面跳转到首页
        检查点：
        无
        测试后续步骤：
        无
        """
        userid = '13093110000'
        psw = 'aa1234'
        driver = Driver.driver
        TestResult = Login.Login(driver,userid, psw)
        #登录恒天财富账号
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:打开恒天财富APP→进入我的页面')
    def test_Myself_Equity_002IntoMyself_tv(self):
        """
        前置条件：
        处于已登录状态，页面处于首页
        测试步骤：
        1.点击"我的"按钮
        期望结果：
        进入我的页面
        检查点：
        验证标题是否为我的
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoMyself_tv.IntoMyself_tv(driver)
        #进入我的页面
        TestResult = IntoMyself_tv.IntoMyself_tv_CheckPoint(driver)
        #设置检查点验证进入我的成功
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:我的页面→点击查看权益')
    def test_Myself_Equity_003IntoMyself_Equity(self):
        """
        前置条件：
        页面处于我的页面
        测试步骤：
        1.点击"查看权益"按钮
        期望结果：
        进入查看权益页面
        检查点：
        1.验证标题是否为会员权益
        测试后续步骤：
        无
        """
        driver = Driver.driver
        IntoMyself_Equity.IntoMyself_Equity(driver)
        #进入设置页面
        TestResult = IntoMyself_Equity.IntoMyself_Equity_CheckPoint(driver)
        #设置检查点会员权益
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→财富体验')
    def test_Myself_Equity_004JiuDianYuYue(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"财富体验"按钮
        期望结果：
        进入"财富体验"权益详情页面
        检查点：
        1.对"财富体验"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver

        AllEquitys.EveryEquitys(driver, "财富体验")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "财富体验")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→专家一对一')
    def test_Myself_Equity_005ShengRiLiYu(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"专家一对一"按钮
        期望结果：
        进入"专家一对一"权益详情页面
        检查点：
        1.对"专家一对一"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "专家一对一")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "专家一对一")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→恒逸人生')
    def test_Myself_Equity_006ZheKouHuanLi(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"恒逸人生"按钮
        期望结果：
        进入"恒逸人生"权益详情页面
        检查点：
        1.对"恒逸人生"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "恒逸人生")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "恒逸人生")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→管理人面对面')
    def test_Myself_Equity_007JiChangKuaiSuAnJian(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"管理人面对面"按钮
        期望结果：
        进入"管理人面对面"权益详情页面
        检查点：
        1.对"管理人面对面"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "管理人面对面")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "管理人面对面")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→邀请好礼')
    def test_Myself_Equity_008VIPRoom(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"邀请好礼"按钮
        期望结果：
        进入"邀请好礼"权益详情页面
        检查点：
        1.对"邀请好礼"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "邀请好礼")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "邀请好礼")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→公募诊断')
    def test_Myself_Equity_009ChiKeHuLi(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"公募诊断"按钮
        期望结果：
        进入"公募诊断"权益详情页面
        检查点：
        1.对"公募诊断"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "公募诊断")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "公募诊断")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→生日礼遇')
    def test_Myself_Equity_010RongYaoNianHui(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"生日礼遇"按钮
        期望结果：
        进入"生日礼遇"权益详情页面
        检查点：
        1.对"生日礼遇"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "生日礼遇")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "生日礼遇")
        assert TestResult == True

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→恒天高尔夫')
    def test_Myself_Equity_011GaoDuanTiJian(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"恒天高尔夫"按钮
        期望结果：
        进入"恒天高尔夫"权益详情页面
        检查点：
        1.对"恒天高尔夫"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "恒天高尔夫")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "恒天高尔夫")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→荣耀年会')
    def test_Myself_Equity_012XiuXianDuJia(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"荣耀年会"按钮
        期望结果：
        进入"荣耀年会"权益详情页面
        检查点：
        1.对"荣耀年会"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "荣耀年会")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "荣耀年会")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→金融产品诊断')
    def test_Myself_Equity_013JinRongChanPinZhenDuan(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"金融产品诊断"按钮
        期望结果：
        进入"金融产品诊断"权益详情页面
        检查点：
        1.对"金融产品诊断"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "金融产品诊断")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "金融产品诊断")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→财富规划')
    def test_Myself_Equity_014CaiFuGuiHua(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"财富规划"按钮
        期望结果：
        进入"财富规划"权益详情页面
        检查点：
        1.对"财富规划"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "财富规划")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "财富规划")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→持仓报告')
    def test_Myself_Equity_015ChiCangBaoGao(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"持仓报告"按钮
        期望结果：
        进入"持仓报告"权益详情页面
        检查点：
        1.对"持仓报告"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "持仓报告")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "持仓报告")
        assert TestResult == True

        time.sleep(3)
        import huadong
        huadong.custom(driver,_x1= 0.5, _x2 = 1, _y1 = 0.90,_y2 = 0.5, move = 'shang' , t = 300)
        time.sleep(1)
        huadong.custom(driver,_x1= 0.5, _x2 = 1, _y1 = 0.90,_y2 = 0.5, move = 'shang' , t = 300)

    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→专户理财')
    def test_Myself_Equity_016ZhuanHuLiCai(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"专户理财"按钮
        期望结果：
        进入"专户理财"权益详情页面
        检查点：
        1.对"专户理财"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "专户理财")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "专户理财")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→专家在线')
    def test_Myself_Equity_017ZhuanJiaZaiXian(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"专家在线"按钮
        期望结果：
        进入"专家在线"权益详情页面
        检查点：
        1.对"专家在线"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "专家在线")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "专家在线")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→法税咨询')
    def test_Myself_Equity_018FaShuiZiXun(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"法税咨询"按钮
        期望结果：
        进入"法税咨询"权益详情页面
        检查点：
        1.对"法税咨询"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "法税咨询")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "法税咨询")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→家业管家')
    def test_Myself_Equity_019JiaYeGuanJia(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"家业管家"按钮
        期望结果：
        进入"家业管家"权益详情页面
        检查点：
        1.对"家业管家"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "家业管家")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "家业管家")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→健康管家')
    def test_Myself_Equity_020JianKangGuanJia(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"健康管家"按钮
        期望结果：
        进入"健康管家"权益详情页面
        检查点：
        1.对"健康管家"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "健康管家")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "健康管家")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→专属礼遇')
    def test_Myself_Equity_021ZhuanShuLiYu(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"专属礼遇"按钮
        期望结果：
        进入"专属礼遇"权益详情页面
        检查点：
        1.对"专属礼遇"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "专属礼遇")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "专属礼遇")
        assert TestResult == True



    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→名家讲堂')
    def test_Myself_Equity_022MingJiaJiangTang(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"名家讲堂"按钮
        期望结果：
        进入"名家讲堂"权益详情页面
        检查点：
        1.对"名家讲堂"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "名家讲堂")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "名家讲堂")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→恒天有约')
    def test_Myself_Equity_023HengTianYouYue(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"恒天有约"按钮
        期望结果：
        进入"恒天有约"权益详情页面
        检查点：
        1.对"恒天有约"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "恒天有约")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "恒天有约")
        assert TestResult == True


    #@pytest.mark.skip(reason="不执行这条用例")
    @allure.feature('用例名称:会员权益→家族权益')
    def test_Myself_Equity_024JiaZuQuanYi(self):
        """
        前置条件：
        页面处于会员权益页面
        测试步骤：
        1.点击"家族权益"按钮
        期望结果：
        进入"家族权益"权益详情页面
        检查点：
        1.对"家族权益"页面进行ScreenShot
        测试后续步骤：
        1.点击"返回上一页面"，返回到消息中心页面
        """
        driver = Driver.driver
        AllEquitys.EveryEquitys(driver, "家族权益")
        TestResult = AllEquitys.EveryEquitys_CheckPoint(driver, "家族权益")
        assert TestResult == True



if __name__ == "__main__":
    ENV = environment()
    if int(ENV) == 1:
        pytest.main()
    elif int(ENV)== 2:
        pytest.main(['start_003_Myself_tv_Myself_Equity.py', "-s", "-v"])
