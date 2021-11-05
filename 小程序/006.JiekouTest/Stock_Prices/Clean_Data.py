#coding:utf-8
import Base_StockInterface
import time



def Clean_Data_sina(Number):
	everydata = Base_StockInterface.Stock_sinajs(Number)
	#print (everydata)

	stockname = everydata[0].split("=\"")[1]
	#股票名字
	stockcode = Number
	#股票代码
	today_kaipanjia = everydata[1]
	#今日开盘价
	yday_price = everydata[2]
	#昨日收盘价
	nowprice = everydata[3]
	#当前价格
	todayhigh = everydata[4]
	#今日最高价
	todaylow = everydata[5]
	#今日最低价
	dealstock = everydata[8]
	#成交的股票数【成交量】，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
	dealamount = everydata[9]
	#成交金额【成交额】
	date = everydata[30].replace("-", "/")
	#日期
	time = everydata[31]
	#时间

	"""
	print (stockname)
	print (stockcode)
	print (today_kaipanjia)
	print (yday_price)
	print (nowprice)
	print (todayhigh)
	print (todaylow)
	print (dealstock)
	print (dealamount)
	print (date)
	print (time)
	"""

def Clean_Data_gtimgHK(Number):
	alldata = Base_StockInterface.Stock_gtimg_HK(Number)
	#everydata = alldata.split("~")
	stockname = alldata[1]
	#股票名字
	stockcode = alldata[2]
	#股票代码
	today_kaipanjia = alldata[5]
	#今日开盘价
	yday_price = alldata[4]
	#昨日收盘价
	nowprice = alldata[3]
	#当前价格
	todayhigh = alldata[41]
	#今日最高价[没有]
	todaylow = alldata[42]
	#今日最低价[没有]
	#dealstock = float(alldata[6]) / 100
	dealstock = alldata[6]
	#成交的股票数【成交量】，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
	dealamount = alldata[37]
	#成交金额

	date = alldata[30].split(" ")[0]
	#日期
	time = alldata[30].split(" ")[1]
	#时间[也可以用30的数据]
	"""
	print (stockname)
	print (stockcode)
	print (today_kaipanjia)
	print (yday_price)
	print (nowprice)
	print (todayhigh)
	print (todaylow)
	print (dealstock)
	print (dealamount)
	print (date)
	print (time)
	"""



Clean_Data_gtimgHK("01810")

Clean_Data_sina("600570")


Clean_Data_sina("002594")