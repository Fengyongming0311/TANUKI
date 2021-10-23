#coding:utf-8
import Customer_account
import time
import winsound

#qasa AGU
#uata HKGU

def ChtwmCompare_qasaSZ(high, low, soundlock, customer_no):
	Middle = Customer_account.Customer_account_qasaSZ(customer_no)
	#中岩小程序通过客户编号查询客户信息 查询出所有结果
	Middle = float(Middle)
	#转化为float格式
	qasa_max = float(high)
	qasa_min = float(low)
	if qasa_max == 0 or qasa_min == 0:
		pass
	elif Middle >= qasa_max:
		if soundlock == "on":
			winsound.PlaySound("up.wav", flags = 0)
		print ("查询数据库customer_account表======手机号为：UP  18633|%s========>  %s    UP"%(customer_no, Middle))
	elif Middle <= qasa_min:
		if soundlock == "on":
			winsound.PlaySound("down.wav", flags = 0)
		print ("查询数据库customer_account表======手机号为：Down  18633|%s========>  %s    Down"%(customer_no, Middle))

	return Middle



def ChtwmCompare_qasaSH(high, low, soundlock, customer_no):
	Middle = Customer_account.Customer_account_qasaSH(customer_no)
	#中岩小程序通过客户编号查询客户信息 查询出所有结果
	Middle = float(Middle)
	#转化为float格式
	qasa_max = float(high)
	qasa_min = float(low)
	if qasa_max == 0 or qasa_min == 0:
		pass
	elif Middle >= qasa_max:
		if soundlock == "on":
			winsound.PlaySound("up.wav", flags = 0)
		print ("查询数据库customer_account表======手机号为：UP  18633|%s========>  %s    UP"%(customer_no, Middle))
	elif Middle <= qasa_min:
		if soundlock == "on":
			winsound.PlaySound("down.wav", flags = 0)
		print ("查询数据库customer_account表======手机号为：Down  18633|%s========>  %s    Down"%(customer_no, Middle))

	return Middle




def ChtwmCompare_uataHK(high, low, soundlock, customer_no):
	Middle = Customer_account.Customer_account_uataHK(customer_no)
	#中岩小程序通过客户编号查询客户信息 查询出所有结果
	Middle = float(Middle)
	#转化为float格式
	uata_max = float(high)
	uata_min = float(low)

	if uata_max == 0 or uata_min == 0:
		pass
	elif Middle >= uata_max:
		if soundlock == "on":
			winsound.PlaySound("up.wav", flags = 0)
		print ("查询数据库compliance_auth表======手机号为：18633|%s========>  %s    UP"%(customer_no, Middle))
	elif Middle <= uata_min:
		if soundlock == "on":
			winsound.PlaySound("down.wav", flags = 0)
		print ("查询数据库compliance_auth表======手机号为：18633|%s========>  %s    Down"%(customer_no, Middle))

	return Middle
