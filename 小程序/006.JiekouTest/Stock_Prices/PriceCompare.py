#coding:utf-8
"""
从数据库中读取股票数据，然后和实时股票接口数据做对比，如果低于价格的话就发送提醒
selectsql() 只需要执行一次，返回所有股票代码数据
Run_interface()   用股票代码数据反复请求接口

"""
import pymysql
from Clean_Data import Clean_Data
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
		'''
		for i in dondake:
			print (i)
		'''
		return dondake


	def Run_interface(data):
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
			print (stockname)
			nowprice = float(dict['nowprice'])
			#如果实时价格小于数据库中的最低价，那么update数据库，然后发送通知
			print ("实时价格为：",nowprice)
			print ("数据库最低价格为：",low_price)
			if nowprice < low_price:
				from InsrtSQL import sqlcontrol
				sqlcontrol.stockbaseupdate(stockcode,nowprice,dict['date'])
				pass
				#发送通知SendMessage


		else:
			print ("股票名称数据不一致，请DeBug！！")
			print ("数据库股票名称:-------->",stockname)
			print ("接口获取股票名称：-------->",dict['stockname'])


		pass




if __name__ == '__main__':
	sqldata = PriceCompare.selectsql()
	#sqldata---所有股票代码数据
	"""
	for stockdata in sqldata:
		PriceCompare.Run_interface(stockdata)
	"""

	PriceCompare.Run_interface(sqldata[15])
