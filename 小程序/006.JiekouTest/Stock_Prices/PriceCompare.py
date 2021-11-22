#coding:utf-8

"""
从数据库中读取股票数据，然后和实时股票接口数据做对比，如果低于价格的话就发送提醒
selectsql() 只需要执行一次，返回所有股票代码数据
Run_interface()   用股票代码数据反复请求接口

"""
'''
#Ver 1.0   完成基本代码架构2021.11.21
#Version 1.1 修改两个底层逻辑BUG
1.每次数据都与第一次select出来的数据库价格做对比，这样更新出来的数据不是正确的数据，
修改方案，第一次查询数据库，只获得stockcode，然后每次循环，先重新select一次数据库查询出单条数据然后再进行比较
2.每个一分钟更新完一次数据都会发一次邮件，在数据库stockbase中新增一条字段，updatetime，每次查询数据库的时候，
如果需要更新价格，那么判断一下updatetime小于一定时间的话就不发邮件。 
'''
import time

import pymysql
from Clean_Data import Clean_Data
from InsrtSQL import sqlcontrol
#调用数据库语句更新字段
import Notify_Email   #调用发送通知邮件
class PriceCompare:
	def selectsql():
		conn = pymysql.connect(host='127.0.0.1', user='root', passwd='000000', db='stockmain', charset='utf8')  # 连接数据库
		cur = conn.cursor()  # 使用cursor()方法获取操作游标

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


	def Run_interface(data):
		#data为第一次查询数据库的值，如果执行中数据库值有变的话需要重新取
		stockcode = data[0]
		stockname = data[1]
		low_price = float(data[2])
		lowprice_date = data[3]
		high_price = float(data[4])
		highprice_date = data[5]
		if len(stockcode) > 5:
			dict = Clean_Data.Clean_Data_sina(stockcode)
		else:
			dict = Clean_Data.Clean_Data_gtimgHK(stockcode)

		#如果实时刷新的股票价格与数据库里股票价格一致的话，就进行比对操作，不一致爆出错误
		if dict['stockname'] == stockname:
			#print (stockname)
			nowprice = float(dict['nowprice'])
			#测试用nowprice = float(6)
			#如果实时价格小于数据库中的最低价，那么update数据库，然后发送通知
			#print ("实时价格为：",nowprice)
			#print ("数据库最低价格为：",low_price)
			#print ("数据库最高价格为：",high_price)
			if nowprice < low_price:
				dondake = "low"
				#更新数据库最低价格
				sqlcontrol.stockbaseupdate(dondake,stockcode,nowprice,dict['date'])

				#发送通知SendMessage
				subject = "监测到%s----price异动！"%stockname
				msg = """监测到股价异动！
						股票名称：%s      股票代码：%s
						数据库最低价格：-------->%.2f
						实时股票价格：---------->%.2f
						"""%(stockname,stockcode,low_price,nowprice)
				receiveaddress = ["fengyongming0311@sohu.com","guozilidazuo@qq.com","342469367@qq.com"]
				Notify_Email.send_email(subject = subject, msg = msg, address = receiveaddress )


			elif nowprice > high_price:
				dondake = "high"
				sqlcontrol.stockbaseupdate(dondake,stockcode,nowprice,dict['date'])

				#发送通知SendMessage
				subject = "监测到%s----price异动！"%stockname
				msg = """监测到股价异动！
						股票名称：%s      股票代码：%s
						数据库最高价格：-------->%.2f
						实时股票价格：---------->%.2f
						"""%(stockname,stockcode,high_price,nowprice)
				receiveaddress = ["fengyongming0311@sohu.com","guozilidazuo@qq.com","342469367@qq.com"]
				Notify_Email.send_email(subject = subject, msg = msg, address = receiveaddress )
			else:                    #如果价格既不低于最低价也不高于最高价则什么也不做
				#print (stockname + "..............." +"什么也没干")
				pass



		else:
			sqlcontrol.sqlrecordlog("股票名称数据不一致，请DeBug！！数据库股票名称:-------->%s"%stockname + "      "+ "股票代码: %s"%stockcode)
			sqlcontrol.sqlrecordlog("接口获取股票名称：-------->%s"%dict['stockname'] + "      "+ "股票代码: %s"%stockcode)


		pass




if __name__ == '__main__':
	sqldata = PriceCompare.selectsql()
	#sqldata---所有股票代码数据
	while 1:
		for stockdata in sqldata:
			PriceCompare.Run_interface(stockdata)
		time.sleep(60)
	#上  循环执行每条数据
	#测试数据用PriceCompare.Run_interface(sqldata[15])
