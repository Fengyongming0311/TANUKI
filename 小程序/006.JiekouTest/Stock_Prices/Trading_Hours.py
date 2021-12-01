#coding:utf-8
#判断交易时间
"""
先判断今天是不是在周一到周五

然后在判断时间是否在9：30-11:30
下午13：00-15：00
"""
import tanuki
import time,datetime


#判断当前日期是周几
def get_week_day(date):
	week_day_dict = {
		0 : True, #'周一'
		1 : True, #'周二'
		2 : True, #'周三'
		3 : True, #'周四'
		4 : True, #'周五'
		5 : False, #'周六'
		6 : False, #'周日'
	}

	day = datetime.datetime.strptime(date,'%Y-%m-%d').weekday()

	return week_day_dict[day]

now = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
date,time = now.split("_")


#tanuki.printtype(time)

def intime(start,end):
	# 范围时间
	start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '%s'%start, '%Y-%m-%d%H:%M')
	# 开始时间
	#tanuki.printtype(start_time)
	end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '%s'%end, '%Y-%m-%d%H:%M')
	# 结束时间
	#tanuki.printtype(end_time)
	# 当前时间
	now_time = datetime.datetime.now()
	#tanuki.printtype(now_time)
	# 方法一：
	# 判断当前时间是否在范围时间内
	if start_time < now_time < end_time:
		return True
	else:
		return False


def tradetime():
	am = intime("9:30","11:30")
	pm = intime("13:00","15:00")
	day = get_week_day(date)
	if day and am or pm:
		return True
	else:
		return False

