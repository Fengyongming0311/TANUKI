#coding:utf-8
from Base_StockInterface import Base_StockInterface

import time

class Clean_Data:
	@staticmethod
	def Clean_Data_sina(number):
		everydata = Base_StockInterface.Stock_sinajs(number)
		dict = {}
		dict['stockname'] = everydata[0].split("=\"")[1].replace(" ","")
		#股票名字
		dict['stockcode'] = number
		#股票代码
		dict['today_kaipanjia'] = everydata[1]
		#今日开盘价
		dict['yday_price'] = everydata[2]
		#昨日收盘价
		dict['nowprice'] = everydata[3]
		#当前价格
		dict['todayhigh'] = everydata[4]
		#今日最高价
		dict['todaylow'] = everydata[5]
		#今日最低价
		dict['dealstock'] = everydata[8]
		#成交的股票数【成交量】，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
		dict['dealamount'] = everydata[9]
		#成交金额【成交额】
		dict['date'] = everydata[30].replace("-", "/")
		#日期
		dict['time'] = everydata[31]
		#时间
		return dict




		"""		
		
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
	@staticmethod
	def Clean_Data_gtimgHK(number):
		alldata = Base_StockInterface.Stock_gtimg_HK(number)
		dict = {}
		dict['stockname'] = alldata[1].replace(" ","")
		#股票名字
		dict['stockcode'] = alldata[2]
		#股票代码
		dict['today_kaipanjia'] = alldata[5]
		#今日开盘价
		dict['yday_price'] = alldata[4]
		#昨日收盘价
		dict['nowprice'] = alldata[3]
		#当前价格
		dict['todayhigh'] = alldata[41]
		#今日最高价[没有]
		dict['todaylow'] = alldata[42]
		#今日最低价[没有]
		#dealstock = float(alldata[6]) / 100
		dict['dealstock'] = alldata[6]
		#成交的股票数【成交量】，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
		dict['dealamount'] = alldata[37]
		#成交金额

		dict['date'] = alldata[30].split(" ")[0]
		#日期
		dict['time'] = alldata[30].split(" ")[1]
		#时间[也可以用30的数据]
		return dict


		"""		
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


	@staticmethod
	def fund_CleanData(fundcode):
		import re
		import json
		don = Base_StockInterface.fund_1234567(fundcode)

		# 正则表达式
		pattern = r'^jsonpgz\((.*)\)'
		# 查找结果
		search = re.findall(pattern, don)
		for i in search:
			data = json.loads(i)
			return data
