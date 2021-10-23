#coding:utf-8
import requests, json
import urllib3
"""
Customer_account_qasa    是第一个XL

Customer_account_uata    是第二个TX

"""


def Customer_account_qasa(Number):
	customer_account = []
	# urllib3.disable_warnings()
	url = "http://hq.sinajs.cn/list=sz"+"%s"%Number

	requests.packages.urllib3.disable_warnings()
	response = requests.get(url, verify=False)
	#print("DonDaKe",response.text)
	a = str(response.text)
	#所有数据

	customer_account = a.split(",")


	customer_now = customer_account[3]
	#取实时价格


	return	customer_now




def Customer_account_uata(Number):
	customer_auth = "http://qt.gtimg.cn/q=r_hk"+"%s"%Number

	requests.packages.urllib3.disable_warnings()
	response = requests.get(customer_auth, verify=False)

	don = str(response.text)

	customer_contact = don.split("~")


	print (don)
	#print (customer_contact)

	#zy_accredited_validdate = customer_contact[3]

	#return zy_accredited_validdate

Customer_account_qasa("002594")


Customer_account_uata("01810")