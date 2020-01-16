__author__ = 'TANUKI'
# coding:utf-8
# 生产版本的自动化测试
# 前置条件：安装好生产环境的测试包，登录账号后切换到哈奇内测楼盘，页面处于实地派首页
# 上传头像的脚本需要提前开手机权限
import sys

sys.path.append("..")
from appium import webdriver
import os, time
from Public import testphone

# img_file = img_file.img_file()  #定义图片文件保存的位置
############导入测试用例###############
sys.path.append("../ReleasePage")
# from 文件名 import Class名
from Case01_Loginin import Loginin
from Case02_ShiDiPai import ShiDiPai
from Case03_MyHome import MyHome
from Case04_MyTorrent import MyTorrent
from Case05_MyCoupon import MyCoupon
from Case06_MyOrder import MyOrder
from Case07_MyAPP import MyAPP
from Case08_NeighborTalk import NeighborTalk
from FilePublic_Page import Public_Page

######################################

shouji = testphone.testphone()
# 读取被测的手机型号
driver = webdriver.Remote('http://localhost:4723/wd/hub', shouji)

'''
ShiDiPai.IntoShiDiPai(driver)
#进入实地派首页
ShiDiPai.RecommendApp(driver)
#7个推荐应用和更多

ShiDiPai.Brand_Image(driver)
#点击商标图片——实地派会员专享权益（品牌宣传位）
#BUG:点击进入58到家选择城市页面然后404了


ShiDiPai.ZunXiangFuWu(driver)
#查看尊享服务

ShiDiPai.XiaLaPage(driver, 600)


ShiDiPai.Community_Image(driver)
#主要推荐的大图片楼盘,在哈奇内部测试楼盘不存在

ShiDiPai.Recommend_Community_Title(driver)
#精品楼盘
#实地派首页的自动化测试完成


MyHome.IntoMyHome(driver)
# 进入我家页面
time.sleep(3)

MyHome.MyHome_two(driver)
# 测试我的消息、设置、进入个人资料是否正常显示

MyHome.Change_ProfilePhoto(driver)
#修改个人头像
MyHome.IntoMyHome(driver)
#再次进入我家页面
MyHome.Change_PersonalData(driver)
#修改个人资料功能

MyHome.AddressManage(driver)
#地址管理增加收货地址
MyHome.DeleteAddress(driver, 3)
#测试我家页面中各个功能
MyTorrent.MyTorrent(driver)
#进入我的种子

MyCoupon.IntoCoupon(driver)
#进入我的优惠券

MyOrder.WoJiaOrder(driver)
#我家的订单查看详情




MyOrder.AllOrder(driver)
#我家查看全部订单
MyOrder.ClickMyOrder(driver)
#我的订单订单管理


MyHome.IntoMyHome(driver)
#单独测试就得重新进入我家

#MyAPP.MyApplication(driver, AppName = "我的购物车", wojia = True)
#MyAPP.MyApplication(driver, AppName = "房间绑定", wojia = True)
#MyAPP.MyApplication(driver, AppName = "我的报修", wojia = True)
#MyAPP.MyApplication(driver, AppName = "社区服务", wojia = True)
#MyAPP.MyApplication(driver, AppName = "智能家居", wojia = True)
#MyAPP.MyApplication(driver, AppName = "人脸识别", wojia = True)
#MyAPP.MyApplication(driver, AppName = "访客邀请", wojia = True)
#MyAPP.MyApplication(driver, AppName = "我的活动", wojia = True)
#我家的我的应用（从我家页面进入需要带参数wojia = True）
time.sleep(3)
MyAPP.IntoALLAPP(driver)
#点击全部应用进入全部应用
#MyAPP.MyApplication(driver, AppName = "商家收藏")
#MyAPP.MyApplication(driver, AppName = "我的家书")
#MyAPP.MyApplication(driver, AppName = "我的关注")
#MyAPP.MyApplication(driver, AppName = "我的评价")
#MyAPP.MyApplication(driver, AppName = "约车记录")
MyAPP.MyApplication(driver, AppName = "我的帖子")
Public_Page.ExitBack(driver)
#返回到我家页面
MyHome.SmartBandInstruction(driver)
'''

NeighborTalk.IntoNeighbor(driver)
#进入友邻页面
NeighborTalk.IntoNewTopic(driver)
NeighborTalk.ChoiceSpeakType(driver, type = 3)
NeighborTalk.PostNewTopic(driver, price = 100, phone = 13435951753)
