#coding:utf-8
#判断交易时间
"""
先判断今天是不是在周一到周五

然后在判断时间是否在9：30-11:30
下午13：00-15：00

直接调用tradetime  返回True就是在交易时间，返回False就是不在交易时间
"""

import time,datetime



#判断当前日期是周几
def get_week_day(date):
	week_day_dict = {
		0 : '周一',
		1 : '周二',
		2 : '周三',
		3 : '周四',
		4 : '周五',
		5 : '周六',
		6 : '周日'
	}

	day = datetime.datetime.strptime(date,'%Y-%m-%d').weekday()

	return week_day_dict[day]


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


def tradetime(now,tradeswitch = False):
	#设置一个交易开关，如果开关是False 则去下方判断交易时间，如果开关是True直接返回True不做下方判断，主要是怕节假日也是交易时间
	#print (tradeswitch)
	if tradeswitch != True:
		date, time = now.split("_")
		day = get_week_day(date)
		if day in ["周一","周二","周三","周四","周五"]:
			am = intime("9:30","11:30")
			pm = intime("13:00","15:00")
			# 直接return am or pm
			#print ("date在周一到周五的范围内，做了intime的判断")
			return  am or pm
		else:
			#不在周一到周五时间内
			print ("今天的日期不在周一到周五返回False")
			return False

	else:
		return True

