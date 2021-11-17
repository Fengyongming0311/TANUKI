#coding:utf-8
"""
从数据库中读取股票数据，然后和实时股票接口数据做对比，如果低于价格的话就发送提醒
"""
import pymysql
import Clean_Data


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

	for i in dondake:
		print (i)


	#print (dondake)
	#print (type(dondake))


selectsql()
