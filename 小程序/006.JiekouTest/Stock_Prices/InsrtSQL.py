# encoding=utf-8

import pymysql
import os, sys, string
import time



def ReadEcxecl(filename):
	"""
	读取excel 每次读取一行数据
	:param filename: 读取的excel文件名称
	:return:
	"""
	#从excel读取
	import xlrd

	data = xlrd.open_workbook(filename, encoding_override = 'GBK')
	#打开文件，用GBK格式解码

	biao1 = data.sheet_by_index(0)
	#默认选择第一个表作为数据表

	nrows = biao1.nrows	#获取表中共有多少行数据（横行）

	for i in range(nrows):
		#跳过第一行数据
		if i == 0:
			continue
		dondake = biao1.row_values(i)
		#上为获取每一行数据

		stockcode = dondake[0]
		stockname = dondake[1]
		lowprice = float(dondake[2])
		lowprice_date = dondake[3]
		high_price = float(dondake[4])
		highprice_date = dondake[5]
		grade =  dondake[6]
		industry = dondake[7]
		keyword = dondake[8]
		business_scope = dondake[9]
		core = dondake[10]
		FYMtips = dondake[11]
		SPtips = dondake[12]

		'''
		print (stockcode)
		print (stockname)
		print (lowprice)
		print (lowprice_date)
		print (high_price)
		print (highprice_date)
		print (grade)
		print (industry)
		print (keyword)
		print (business_scope)
		print (core)
		print (FYMtips)
		print (SPtips)
		print ("########################################")
		'''
		stockbaseinsert(stockcode, stockname, lowprice, lowprice_date, high_price, highprice_date)

		gradeinsert(stockcode, stockname, grade, industry, keyword, business_scope, core, FYMtips, SPtips)



def stockbaseinsert(stockcode,stockname,lowprice,lowprice_date, high_price, highprice_date):
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
		cur = conn.cursor()  # 使用cursor()方法获取操作游标

		stockbaseinsert = "INSERT INTO stockbase (`stockcode`, `stockname`, `low_price`, `lowprice_date`, `high_price`, `highprice_date`) VALUES (\'%s\' , \'%s\', \'%.2f\', \'%s\', \'%.2f\',  \'%s\') ;" % (stockcode, stockname, lowprice, lowprice_date, high_price, highprice_date)
		#插入表stockbase
		cur.execute(stockbaseinsert)
		#插入单条数据

	except Exception as e:
		#如果插入报错可以在这里用update
		#因该不用，到时候直接在实时刷价格的时候写update代码，或者说有新字段增加的话需要update
		print (e)
		pass
	finally:
		cur.close()
		#关闭游标
		conn.commit()
		#没有这个无法真正提交数据
		conn.close()
		#关闭数据库连接


def gradeinsert(stockcode,stockname, grade,industry, keyword, business_scope, core, FYMtips,SPtips):
	try:
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
		cur = conn.cursor()  # 使用cursor()方法获取操作游标

		gradeinsert = " INSERT INTO grade (`stockcode`, `stockname`, `grade`, `industry`, `keyword`, `business_scope`, `core`, `FYMtips`, `SPtips`) VALUES ('%s' , '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') ;"
		cur.execute(gradeinsert %(stockcode, stockname, grade, industry, keyword, business_scope, core, FYMtips, SPtips))
		#插入表grade
	except Exception as e:
		#如果插入报错可以在这里用update
		#因该不用，到时候直接在实时刷价格的时候写update代码，或者说有新字段增加的话需要update
		print (e)
		pass
	finally:
		cur.close()
		#关闭游标
		conn.commit()
		#没有这个无法真正提交数据
		conn.close()
	#关闭数据库连接


filename = "股票数据.xlsx"
ReadEcxecl(filename)

