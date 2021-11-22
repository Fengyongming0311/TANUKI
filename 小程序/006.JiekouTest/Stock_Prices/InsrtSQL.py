# encoding=utf-8

import pymysql
import os, sys, string
import time,datetime

class sqlcontrol:
	"""
	SQL语句执行在这里
	"""
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
			sqlcontrol.stockbaseinsert(stockcode, stockname, lowprice, lowprice_date, high_price, highprice_date)

			sqlcontrol.gradeinsert(stockcode, stockname, grade, industry, keyword, business_scope, core, FYMtips, SPtips)

	def selectsql(*args, **kwargs):
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
		cur = conn.cursor()  # 使用cursor()方法获取操作游标
		if args:
			stockcode = args[0]
			selectstock = "SELECT * from stockbase where stockcode = %s"%stockcode
			cur.execute(selectstock)
			#查询数据库
			dondake = cur.fetchall()
			#获取所有的返回值
		else:
			selectstock = "SELECT * from stockbase"
			cur.execute(selectstock)
			#查询数据库
			dondake = cur.fetchall()
			#获取所有的返回值

		cur.close()
		#关闭游标
		conn.commit()
		#没有这个无法真正提交数据
		conn.close()
		#下，返回所有数据
		return dondake

	def stockbaseinsert(stockcode,stockname,lowprice,lowprice_date, high_price, highprice_date):
		try:
			conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
			cur = conn.cursor()  # 使用cursor()方法获取操作游标

			stockbaseinsert = "INSERT INTO stockbase (`stockcode`, `stockname`, `low_price`, `lowprice_date`, `high_price`, `highprice_date`) VALUES (\'%s\' , \'%s\', \'%.2f\', \'%s\', \'%.2f\',  \'%s\') ;" % (stockcode, stockname, lowprice, lowprice_date, high_price, highprice_date)
			#插入表stockbase
			cur.execute(stockbaseinsert)
			#插入单条数据
			sqlcontrol.sqlrecordlog(stockbaseinsert)
			#将执行的语句记录到日志中
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


	def stockbaseupdate(dondake,stockcode,price,price_date):
		try:
			conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
			cur = conn.cursor()  # 使用cursor()方法获取操作游标
			#print (dondake)
			#print (type(dondake))
			now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			if dondake == "low":
				stockbaseupdate = "UPDATE stockbase SET `low_price` =\'%s\', `lowprice_date` =\'%s\', `updatetime` =\'%s\' WHERE `stockcode`= \'%s\';" % (price, price_date, now, stockcode)
				#插入表stockbase
			elif dondake == "high":
				stockbaseupdate = "UPDATE stockbase SET `high_price` =\'%s\', `highprice_date` =\'%s\', `updatetime` =\'%s\' WHERE `stockcode`= \'%s\';" % (price, price_date, now, stockcode)

			cur.execute(stockbaseupdate)
			#插入单条数据
			#自己记录什么时间插入更改了什么数据
			sqlcontrol.sqlrecordlog(stockbaseupdate)
			#将执行的语句记录到日志中

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
			sqlcontrol.sqlrecordlog(gradeinsert)
			#将执行的语句记录到日志中
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



	def sqlrecordlog(*args, **kwargs):
		from datetime import datetime
		logday = datetime.now().strftime("%Y-%m-%d")
		log = open("日志记录\stocksql_%s.log" %logday, "a+")     #追加写log日志
		for new_context in args:
			#print (new_context)
			now = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(time.time()))
			log.write(now + "---------->")
			log.write(new_context + "\n")
		log.close()




#filename = "股票数据.xlsx"
#ReadEcxecl(filename)

