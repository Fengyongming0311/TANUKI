#coding:utf-8
import requests, json
import urllib3
"""
Stock_Interface_SZ    是第一个SZ
Stock_Interface_SH    是第一个SZ
Stock_Interface_HK    是第三个HK

01810
目前已知可用接口为：腾讯股票接口、和讯网股票接口、新浪股票接口、雪球股票数据、网易股票数据

上交所股票代码以6开头，全部都属于主板;

深交所股票分为三类：以000，001 开头的是深圳主板，以002开头的为中小板;以300开头的为创业板。
"""

class Base_StockInterface:
	@staticmethod
	def Stock_sinajs(stockcode):
		# urllib3.disable_warnings()

		if int(stockcode[0]) > 3:
			url = "http://hq.sinajs.cn/list=sh"+"%s"%stockcode
		else:
			url = "http://hq.sinajs.cn/list=sz"+"%s"%stockcode
		requests.packages.urllib3.disable_warnings()
		response = requests.get(url, verify=False)
		#print("DonDaKe",response.text)
		a = str(response.text)
		#所有数据

		All_list = a.split(",")

		#now_price = All_list[3]
		#取实时价格


		return	All_list

	@staticmethod
	def Stock_gtimg(stockcode):

		if int(stockcode[0]) > 3:
			url = "http://hq.sinajs.cn/list=sh"+"%s"%stockcode
		else:
			url = "http://hq.sinajs.cn/list=sz"+"%s"%stockcode

		requests.packages.urllib3.disable_warnings()
		response = requests.get(url, verify=False)

		a = str(response.text)

		All_list = a.split("~")
		#print (customer_contact)

		#now_price = All_list[3]

		return All_list



	@staticmethod
	def Stock_gtimg_HK(stockcode):
		url = "http://qt.gtimg.cn/q=r_hk"+"%s"%stockcode

		requests.packages.urllib3.disable_warnings()
		response = requests.get(url, verify=False)

		a = str(response.text)

		All_list = a.split("~")
		#print (customer_contact)
		#print (All_list)
		#now_price = All_list[3]
		#print ("========================================")
		return All_list

	@staticmethod
	def fund_1234567(fundcode):
		url = "https://fundgz.1234567.com.cn/js/%s.js"%fundcode

		requests.packages.urllib3.disable_warnings()
		response = requests.get(url, verify=False)

		a = str(response.text)

		return a




