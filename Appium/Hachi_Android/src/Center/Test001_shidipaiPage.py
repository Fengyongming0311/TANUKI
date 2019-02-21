__author__ = 'TANUKI'
#coding:utf-8
#生产版本的自动化测试
#Test001测试实地派页面自动化
#测试楼盘遵义蔷薇国际

import sys
sys.path.append("..")
from appium import webdriver
import os,time
from Public import testphone
#img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../ReleasePage")
#from 文件名 import Class名
from Case01_Loginin import Loginin
from Case02_ShiDiPai import ShiDiPai
from Case03_MyHome import MyHome
from Case04_MyPurse import MyPurse
from Case05_MyCoupon import MyCoupon
from Case06_MyOrder import MyOrder
from Case07_MyAPP import MyAPP
from Case08_NeighborTalk import NeighborTalk
from FilePublic_Page import Public_Page

######################################
#测试手机配置
shouji = testphone.testphone()
#读取被测的手机型号
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)

#测试手机配置结束

"""
#############使用遵义蔷薇国际楼盘进行实地派页面测试
ShiDiPai.IntoShiDiPai(driver)
#case1: 测试左下角实地派，进入实地派页面
ShiDiPai.RecommendApp(driver)
#case2: 测试七个推荐，加一个更多按钮
#ShiDiPai.Zhongshan_Brand_Image(driver)
#case3: 测试实地派品牌宣传广告页面
#ShiDiPai.ZunXiangFuWu(driver)废弃了
ShiDiPai.SheQuFuWu(driver)
#case4: 测试实地派尊享服务
ShiDiPai.XiaLaPage(driver,200)
#case5: 下滑页面，不然定位不到下方的元素
ShiDiPai.ShengHuoPeiTao(driver)
#case6: 测试实地派生活配套
#ShiDiPai.Community_Image(driver)弃用页面没有
#case: 实地派广告，此楼盘下无此元素
#ShiDiPai.Recommend_Community_Title(driver)弃用页面没有
ShiDiPai.Tuijian_Loupan(driver)
#case7: 实地派推荐楼盘
#############实地派页面测试结束########################
"""
###########选择楼盘测试，切换导哈奇内部测试
#Loginin.QieHuanLouPan(driver, "哈奇内部测试", into = "Yes")
###########切换导哈奇内部测试结束####################

MyHome.IntoMyHome(driver)
'''
MyHome.MyHome_two(driver)
MyHome.Change_ProfilePhoto(driver)
MyHome.Change_PersonalData(driver)
MyHome.AddressManage(driver)
#MyHome.DeleteAddress(driver, 3)
#测试我家页面中各个功能
MyPurse.IntoPurse(driver)
#进入我的钱包

MyCoupon.IntoCoupon(driver)
#进入我的优惠券
MyOrder.WoJiaOrder(driver)
MyOrder.AllOrder(driver)
MyOrder.ClickMyOrder(driver)
#我的订单订单管理



MyHome.IntoMyHome(driver)
#单独测试就得重新进入我家

MyAPP.MyApplication(driver, AppName = "我的购物车", wojia = True)
MyAPP.MyApplication(driver, AppName = "房间绑定", wojia = True)
MyAPP.MyApplication(driver, AppName = "投诉建议", wojia = True)
MyAPP.MyApplication(driver, AppName = "房屋报修", wojia = True)
MyAPP.MyApplication(driver, AppName = "社区服务", wojia = True)
MyAPP.MyApplication(driver, AppName = "智能家居", wojia = True)
'''
MyAPP.MyApplication(driver, AppName = "人脸识别", wojia = True)
'''
MyAPP.MyApplication(driver, AppName = "访客邀请", wojia = True)
#我家的我的应用（从我家页面进入需要带参数wojia = True）

MyAPP.IntoALLAPP(driver)
#点击全部应用进入全部应用
MyAPP.MyApplication(driver, AppName = "商家收藏")
MyAPP.MyApplication(driver, AppName = "我的家书")
MyAPP.MyApplication(driver, AppName = "我的关注")
MyAPP.MyApplication(driver, AppName = "我的评价")
MyAPP.MyApplication(driver, AppName = "我的帖子")
Public_Page.ExitBack(driver)
#返回到我家页面
MyHome.SmartBandInstruction(driver)

NeighborTalk.IntoNeighbor(driver)
#进入友邻页面
NeighborTalk.IntoNewTopic(driver)
NeighborTalk.ChoiceSpeakType(driver, type = 3)
NeighborTalk.PostNewTopic(driver, price = 100, phone = 13435951753)
'''