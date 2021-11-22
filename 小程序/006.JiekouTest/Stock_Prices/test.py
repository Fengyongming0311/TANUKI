#coding:utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

from datetime import datetime

def bijiao(nowprice, sqlprice):
	if nowprice < sqlprice:

		print ("update SQL")
		intopricetime = datetime.now()
		if overmailtime == "":
			pass
		elif intopricetime > overemailtime:

		print ("发完邮件")
		overemailtime = datetime.now()
	else:
		pass
'''
now = datetime.now() # current date and time
print (now)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
print("date and time:",date_time)

'''
nowprice = 3
sqlprice = 6
while 1:
	shangciemail = bijiao()