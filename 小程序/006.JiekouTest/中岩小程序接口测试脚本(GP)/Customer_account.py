#coding:utf-8
import requests, json
import urllib3
"""
Customer_account   是第一个XL

Customer_auth     是第二个TX

"""


def Customer_account(Number):
	customer_account = []
	# urllib3.disable_warnings()
	url = "http://hq.sinajs.cn/list=sz"+"%s"%Number

	requests.packages.urllib3.disable_warnings()
	response = requests.get(url, verify=False)
	#print("DonDaKe",response.text)
	a = str(response.text)

	customer_account = a.split(",")


	customer_now = customer_account[3]


	return	customer_now




def Customer_auth(Number):
	customer_auth = "http://qt.gtimg.cn/q=r_hk"+"%s"%Number

	requests.packages.urllib3.disable_warnings()
	response = requests.get(customer_auth, verify=False)

	don = str(response.text)

	customer_contact = don.split("~")
	#print (customer_contact)

	zy_accredited_validdate = customer_contact[3]

	return zy_accredited_validdate




def Bak_Customer_account(Number):
	customer_account = []
	# urllib3.disable_warnings()
	url = "http://qt.gtimg.cn/q=r_sz"+"%s"%Number

	requests.packages.urllib3.disable_warnings()
	response = requests.get(url, verify=False)
	#print("DonDaKe",response.text)
	a = str(response.text)
	print ("444444444444444444444")
	print (a)
	print ("@@@@@@@@@@@@@@@@@@@@")
	customer_account = a.split(",")


	customer_now = customer_account[3]


	return	customer_now