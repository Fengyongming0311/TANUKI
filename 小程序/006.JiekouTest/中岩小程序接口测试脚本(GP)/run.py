#coding:utf-8
import Customer_account
import time

while 1:
	zy_accredited_investor_audit = Customer_account.Customer_account("002594")
	#中岩小程序通过客户编号查询客户信息

	#zy_accredited_investor_audit = Customer_account.Bak_Customer_account("002594")
	

	zy_accredited_investor_audit = float(zy_accredited_investor_audit)

	#print (zy_accredited_investor_audit)

	YDmax = float(177.00)
	YDmin = float(176.00)

	if zy_accredited_investor_audit >= YDmax:
		print ("大查询数据库zy_accredited_investor_audit表~~ 手机号为：13333002594,",zy_accredited_investor_audit)

	if zy_accredited_investor_audit <= YDmin:
		print ("小查询数据库zy_accredited_investor_audit表~~ 手机号为：13333002594,",zy_accredited_investor_audit)



	########################################################################################
	zy_accredited_validdate = Customer_account.Customer_auth("01810")

	zy_accredited_validdate = float(zy_accredited_validdate)

	#print (zy_accredited_validdate)


	XMmax = float(26.20)
	XMmin = float(25.00)

	if zy_accredited_validdate >= XMmax:
		print ("大查询数据库zy_accredited_validdate表~~ZR客户编号为01810 手机号为：13333301810,",zy_accredited_validdate)

	if zy_accredited_validdate <= XMmin:
		print ("小查询数据库zy_accredited_validdate表~~ZR大客户编号为01810 手机号为：13333300354,",zy_accredited_validdate)




	#######################################################################################
	customer_no = Customer_account.Customer_auth("00354")

	customer_no = float(customer_no)

	#print (customer_no)
	#print (type(customer_no))

	ZRmax = float(7.55)
	ZRmin = float(7.00)

	if customer_no >= ZRmax:
		print ("大查询数据库customer_account表~~ZR客户编号为00354 手机号为：13333300354,",customer_no)

	if customer_no <= ZRmin:
		print ("小查询数据库customer_account表~~ZR大客户编号为00354 手机号为：13333300354,",customer_no)




	#########################
	#print (zy_accredited_investor_audit)
	#print (zy_accredited_validdate)
	#print (customer_no)
	#########################

	time.sleep(30)
