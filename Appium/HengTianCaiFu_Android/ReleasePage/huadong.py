#coding:utf-8
__author__ = 'TANUKI'
from appium import webdriver
import time



#获得机器屏幕大小x,y
def getSize(driver):
	x = driver.get_window_size()['width']

	y = driver.get_window_size()['height']

	return (x, y)


#屏幕向上滑动
def shanghua(driver, t):
	l = getSize(driver)

	x1 = int(l[0] * 0.5)  #x坐标

	y1 = int(l[1] * 0.75)   #起始y坐标

	y2 = int(l[1] * 0.25)   #终点y坐标

	driver.swipe(x1, y1, x1, y2,t)


#屏幕向下滑动
def xiahua(driver, t):
	l = getSize(driver)

	x1 = int(l[0] * 0.5)  #x坐标

	y1 = int(l[1] * 0.25)   #起始y坐标

	y2 = int(l[1] * 0.75)   #终点y坐标

	driver.swipe(x1, y1, x1, y2,t)


#屏幕向左滑动
def zuohua(driver, t):
	l = getSize(driver)

	x1 = int(l[0]*0.75)

	y1 = int(l[1]*0.5)

	x2 = int(l[0]*0.05)

	driver.swipe(x1,y1,x2,y1,t)

#屏幕向右滑动
def youhua(driver, t):
	l = getSize(driver)

	x1 = int(l[0]*0.05)

	y1 = int(l[1]*0.5)

	x2 = int(l[0]*0.75)

	driver.swipe(x1,y1,x2,y1,t)

def custom(driver, _x1, _y1, _x2, _y2, move, t):
	"""
	:param driver: driver
	:param _x1: x1坐标
	:param _y1: y1坐标
	:param _x2: x2坐标
	:param _y2: y2坐标
	:param move: 方向
	:param t: 滑动距离
	:return:  无
	"""
	l = getSize(driver)

	x1 = int(l[0] * _x1)

	y1 = int(l[1] * _y1)

	x2 = int(l[0] * _x2)

	y2 = int(l[1] * _y2)

	if move == 'shang':
		print ("执行上滑")
		driver.swipe(x1, y1, x1, y2,t)

	elif move == 'xia':
		driver.swipe(x1, y1, x1, y2,t)

	elif move == 'zuo':
		driver.swipe(x1,y1,x2,y1,t)

	elif move == 'you':
		driver.swipe(x1,y1,x2,y1,t)




	


'''
#调用向左滑动  5为持续时间
zuohua(driver,1000)

#调用向右滑动
youhua(driver,1000)

#调用向上滑动
shanghua(driver,1000)

#调用向下滑动
xiahua(driver,1000)
'''