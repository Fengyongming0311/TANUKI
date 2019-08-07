#coding:utf-8
__author__ = 'TANUKI'

import xlrd
import configparser
import datetime,os,sys,time
from xlrd import xldate_as_tuple
'''
#从Excel中读取数据
#显示周几
#超过早上10点打卡算迟到
#下班时间减去上班时间不足9小时，算早退
#最后以Excel显示
2018.11.01 修改可以读取时间格式为2018.11.1   以前为2018/11/1
2018.11.01 下午解决不用再转存excel表问题
2018.12.05  使用新考勤系统导出数据为乱码，重新解码成为可以看的中文
2018.12.20  之前那个版本想加个方法转码，还没实现，这个版本尝试实现
2019.04.08  1.增加原数据中部门数据
            2.算出每天的工作时长
            3.算出每个人的工作天数（漏打卡数据不算在内，每日工作时间不足9小时算在内但是要标黄数据）
            4.算出总共工作时长
            5.算出每日平均工作时长
            6.做出两个execl 表格
2019.04.26  1.小于9小时不计算当日工作时长
            统计有效时长产生的天数的和  比如冯泳铭当月有效工作18日
'''


def main():
	config = get_config()	#读取配置文件Config.ini

	filename = config.get("filename", "filename")
	#从Config.ini中读取excel文件名

	data = xlrd.open_workbook(filename, encoding_override = 'GBK')  #打开文件，用GBK格式解码

	biao1 = data.sheet_by_index(0)  #默认选择第一个表作为数据表

	nrows = biao1.nrows	#获取表中共有多少行数据（横行）

	#创建所有数据的列表存在alldata中
	alldata = []
	
	#获取所有日期信息存入date中
	date = []

	#获取所有员工姓名存入allstaff中
	allstaff = []


	for i in range(nrows):
		if (i == 0):
			continue	#当i == 0 第一行标题，直接略过 i 为行数
		######
		zhongzhuan = biao1.row_values(i)
		#print ("参数zhongzhuan",zhongzhuan)
		#zhongzhuan 为中转参数保存每行数据['技术部', '冯泳铭', '239', '2019/3/6 18:31:08', '1', '', '指纹/密码/卡/面部', '']
		#zhongzhuan[0] 为部门
		#zhongzhuan[1] 为姓名
		#zhongzhuan[3] 为一次打卡数据
		if isinstance(zhongzhuan[3], float):
			#这里处理328476.12736时间格式的转化,没有此类数据不走这一项
			#xldate_as_tuple从excel中读取浮点数
			temp = datetime.datetime(*xldate_as_tuple(zhongzhuan[3], 0))
			zhongzhuan[3] = temp.strftime('%Y/%m/%d %H:%M:%S')
		else:
			#转换成时间数组
			try:
				zhongzhuan[3] = time.strptime(zhongzhuan[3], '%Y.%m.%d %H:%M:%S')
			except:
				zhongzhuan[3] = time.strptime(zhongzhuan[3], '%Y/%m/%d %H:%M:%S')
			#下行，统一转换成新的时间格式('%Y/%m/%d %H:%M:%S')
			zhongzhuan[3] = time.strftime('%Y/%m/%d %H:%M:%S',zhongzhuan[3])
		######

		zhongzhuan = geshihuashuju(zhongzhuan)
		#print (zhongzhuan[0],zhongzhuan[1],zhongzhuan[2],zhongzhuan[3])
		# 业务创新部 西永恒 2019/03/21 07:53:41
		#zhongzhuan 是包含所有数据的列表单条的
		zhongzhuan[3] = chuli_time(zhongzhuan[3])       #对时间进行了处理格式化

		date.append(zhongzhuan[2])
		#这里把所有时间列出来
		allstaff.append(zhongzhuan[1])
		zhongzhuan = apm(zhongzhuan)             #判断是上班时间还是下班时间
		#print ("ddddddddddddddddddddd",zhongzhuan)
		alldata.append(zhongzhuan)
		#print ("this is alldata=======",alldata)
		#所有数据，包含重复

	date = datesort(date)
	#把所有日期变为每月通勤时间，去除没有任何人打卡天数

	allstaff = list(set(allstaff))
	#去重的所有员工姓名
	#print (allstaff)


	#在这转一下码 废弃
	#allstaff = name_zhuanma(allstaff)废弃
	#print (allstaff)废弃


	#加入写Excel
	import xlwt
	workbook = xlwt.Workbook() #注意Workbook的开头W要大写
	sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok = True)
	#cell_overwrite_ok参数用于确认同一个cell单元是否可以重设值。
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = 'SimSun'    # 指定“宋体”
	font.height = 230
	style.font = font
	#上设置字体
	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour = 0x3A
	style.borders = borders
	#上设置框线

	alignment = xlwt.Alignment()
	alignment.horz = xlwt.Alignment.HORZ_CENTER    #水平居中
	alignment.vert = xlwt.Alignment.VERT_CENTER    #垂直居中
	style.alignment = alignment
	#设置字体居中
	first_col = sheet1.col(0)
	first_col.width = 270 * 20

	second_col = sheet1.col(1)
	second_col.width = 270 * 20

	third_col = sheet1.col(2)
	third_col.width = 270 * 20

	fourth_col = sheet1.col(3)
	fourth_col.width = 270 * 20

	fifth_col = sheet1.col(4)
	fifth_col.width = 270 * 20

	sixth_col = sheet1.col(5)
	sixth_col.width = 270 * 20

	seventh_col = sheet1.col(6)
	seventh_col.width = 270 * 20

	seventh_col = sheet1.col(7)
	seventh_col.width = 270 * 20

	seventh_col = sheet1.col(8)
	seventh_col.width = 270 * 20

	#上设置横行的长度

	################设置第一行字体的格式###############
	geshi = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = 'SimSun'    # 指定“宋体”
	font.height = 350
	font.bold = 'on'
	geshi.font = font
	#上设置字体
	borders = xlwt.Borders()
	borders.left = 1
	borders.right = 1
	borders.top = 1
	borders.bottom = 1
	borders.bottom_colour = 0x3A
	geshi.borders = borders
	##############设置第一行字体的格式完成#############

	sheet1.write(0, 0, '部门', geshi)
	sheet1.write(0, 1, '姓名', geshi)
	sheet1.write(0, 2, '日期', geshi)
	sheet1.write(0, 3, '上班打卡', geshi)
	sheet1.write(0, 4, '下班打卡', geshi)
	sheet1.write(0, 5, '漏打卡', geshi)
	sheet1.write(0, 6, '迟到', geshi)
	sheet1.write(0, 7, '是否早退', geshi)
	sheet1.write(0, 8, '上班时长', geshi)

	num = 1

	#现在只要把单个人的数据传进去就能得出单个人的整合数据了
	for name in allstaff:
		app = []
		for i in alldata:
			if name == i[1]:
				app.append(i)

		#print ("this is app==========",app)
		#app 是每个人的数据的总和
		last_data = data_merge(app, date)                                 #合并上下班日期，上班取最早下班取最晚
		#print (last_data)
		for don in last_data:
			#print ("this is don========",don)
			#['小狗财务', '李京', '2019/03/01', '', '']
			#['项目部', '赵文辉', '2019/03/01', '09:19:57', '18:31:01']
			#['硬件产品部', '陈继伟', '2019/03/01', '', '']
			#['业务创新部', '刘庆朝', '2019/03/01', '09:26:45', '19:00:38']
			#最终数据在这里！！！！
			don = get_week_day(don)											#判断日期是周几
			don = loudaka(don)												#判断漏打卡
			don = daylate(don)                                              #判断上班是否迟到
			don = worktime(don)                                             #判断是否早退
			don = shichang(don)                                             #增加上班时长数据

			#print (don[0],'%',don[1],'%',don[2],'%',don[3],'%',don[4],'%',don[5],'%',don[6], '%', don[7])

			sheet1.write(num, 0, don[0], style)  # 部门
			sheet1.write(num, 1, don[1], style)  # 姓名
			sheet1.write(num, 2, don[2], style)  # 日期
			sheet1.write(num, 3, don[3], style)  # 上班打卡
			sheet1.write(num, 4, don[4], style)  # 下班打卡
			sheet1.write(num, 5, don[5], style)  # 漏打卡
			sheet1.write(num, 6, don[6], style)  # 迟到
			sheet1.write(num, 7, don[7], style)  # 是否早退
			sheet1.write(num, 8, don[8], style)  # 上班时长

			#打开计数
			print (num)
			#打开计数

			
			num = num + 1


	#跳出循环后保存Excel
	now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
	workbook.save(now + '生成统计结果.xls')
	print ("===================统计完成===================")

	'''
	#这是按照配置文件姓名排序的
	for name in STAFF_name:
		app = []
		for i in alldata:
			if name == i[0]:
				app.append(i)
		

		last_data = data_merge(app, date)
		for don in last_data:
			#print (don)
			pass
	'''


#打出来如果是乱码
'''
字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。

decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。

'''

#此功能暂时废弃掉，没有实现...
def name_zhuanma(name):
	listname = name
	print ("这是listname",listname)
	for i in listname:
		print ("这是i",i)
		'''
		print (type(i))
		zhuanma = i.encode("GBK")
		print (zhuanma)
		print (type(zhuanma))
		dondake = str(zhuanma,'GBK')
		print (dondake)
		'''
	

def shichang(data):
	if not data[3] == '' and not data[4] == '':
		time1 = datetime.datetime.strptime(data[3], '%H:%M:%S')
		time2 = datetime.datetime.strptime(data[4], '%H:%M:%S')

		#times = str((time2 - time1)).split(":")
		times = str(time2 - time1)
		data.append(times)
	else:
		data.append("")

	return data

#判断是否早退，上班打卡和上班打卡时差大于就小时算正常
def worktime(data):
	if not data[3] == '' and not data[4] == '':
		time1 = datetime.datetime.strptime(data[3], '%H:%M:%S')
		time2 = datetime.datetime.strptime(data[4], '%H:%M:%S')

		times = str((time2 - time1)).split(":")
		if int(times[0]) >= 9:
			data.append("")
		else:
			data.append("打卡时间不足9小时")
	else:
		data.append("")

	return data

#判断上班是否迟到，上班打卡超过10点判定为迟到
def daylate(data):
	if not data[3] == '':
		time1 = datetime.datetime.strptime(data[3], '%H:%M:%S')
		time2 = datetime.datetime.strptime("10:00:59", '%H:%M:%S')
		#哈哈哈哈哈这里修改一下10:00:59内都不算迟到
		if time1 > time2:
			data.append("上班迟到" + data[3])
		else:
			data.append("")

	else:
		data.append("")
	return data


#判断漏打卡
def loudaka(data):
	#上班与下班都有打卡时间 加入空
	if not data[3] == '' and not data[4] == '':
		data.append("")
	#漏打上班卡
	elif data[3] == '' and not data[4] == '':
		data.append("未打上班卡")
	elif not data[3] == '' and data[4] == '':
		data.append("未打下班卡")
	elif data[3] == '' and data[4] == '':
		xingqi = data[2][-2:]
		if xingqi == '周六' or xingqi == '周日':
			#data.append(xingqi)
			#这块可能有问题，如果周六为正常上班的话判断不了漏打卡....BUG
			data.append("")
		else:
			data.append("旷工一天")


	return data

		


#通过相同的姓名和日期合并数据
def data_merge(app, date):
	#print ("this is app==========",app)
	#print ("this is date==========",date)
	allshuju = []
	
	for evday in date:
		#print (evday)
		
		merge = ['', '', '', '', '']
		#['运营部', '黄建雄', '2019/03/01', '08:56:52', '']
		#可能会在这里调整所有数据的数据量merge
		merge[2] = evday
		for evdata in app:
			merge[0] = evdata[0]
			merge[1] = evdata[1]
			if evdata[2] == evday:
				#print (evdata)
				#判断上班打卡时间        取最早的打卡时间
				#case1: 数据空  case为空    pass
				if merge[3] == '' and evdata[3] == '':
					pass
				#case2: 数据空  case不为空   取case
				elif merge[3] == '' and not evdata[3] == '':
					merge[3] = evdata[3]
				#case3: 数据不为空  case为空   pass
				elif not merge[3] == '' and evdata[3] == '':
					pass
				#case4: 数据不为空  case不为空    比较大小，取最小值
				elif not merge[3] == '' and not evdata[3] == '':
					time1 = datetime.datetime.strptime(merge[3], '%H:%M:%S')
					time2 = datetime.datetime.strptime(evdata[3], '%H:%M:%S')
					if time1 < time2:
						pass
					elif time1 > time2:
						merge[3] = evdata[3]
					else:
						pass

				
				#判断下班打卡时间        取最晚的打卡时间
				#case1: 数据空  case为空    pass
				if merge[4] == '' and evdata[4] == '':
					pass
				#case2: 数据空  case不为空   取case
				elif merge[4] == '' and not evdata[4] == '':
					merge[4] = evdata[4]
				#case3: 数据不为空  case为空   pass
				elif not merge[4] == '' and evdata[4] == '':
					pass
				#case4: 数据不为空  case不为空    比较大小，取最大值
				elif not merge[4] == '' and not evdata[4] == '':
					time1 = datetime.datetime.strptime(merge[4], '%H:%M:%S')
					time2 = datetime.datetime.strptime(evdata[4], '%H:%M:%S')
					if time1 < time2:
						merge[4] = evdata[4]
					elif time1 > time2:
						pass
					else:
						pass
		#最后
		if not merge[1] == '':
			allshuju.append(merge)
	return allshuju
		



	#最后
	#print ('所有数据',allshuju)





#判断是上班时间还是下班时间(普及的打卡不涉及空数据的问题)
def apm(time):
	#print (time)
	try:
		rentime = datetime.datetime.strptime(time[3], '%H:%M:%S')
		zhengwutime = datetime.datetime.strptime('12:00:00', '%H:%M:%S')
		if rentime < zhengwutime:
			#print (rentime,"上午")
			time.append("")
			return time
		elif rentime > zhengwutime:
			#print (rentime,"下午")
			don = time[3]
			time[3] = ''
			time.append(don)
			return time
		elif rentime == zhengwutime:
			#print (rentime,"中午12点")
			time.append("")
			return time
	except Exception as e:
		time.append("")
		return time


#处理上下班时间
def chuli_time(lie_time):
	#把 9:28:03 变成 09:28:03 因为try中只处理float的数据所以 直接的str时间也需要在except中增加处理
	#使用replace(' ' , '')去除中间空格
	try:
		float(lie_time)
		new_time = float(lie_time)
		new_time = xlrd.xldate_as_tuple(new_time ,0)
		d = new_time[3]
		if (d < 10):
			d = '0' + str(d)
		else:
			d = str(new_time[3])
		e = new_time[4]
		if (e < 10):
			e = '0' + str(e)
		else:
			e = str(new_time[4])
		f = new_time[5]
		if (f < 10):
			f = '0' + str(f)
		else:
			f = str(new_time[5])
		return (d + ":" + e + ":" + f)
	except:
		if (lie_time == ''):		#判断传入空字符串直接退出方法
			return lie_time
		lie_time = lie_time.replace(' ' ,'')
		(a,b,c) = lie_time.split(':')
		if (int(a) < 10):
			a = int(a)
			a = '0' + str(a)
		'''
		if (int(b) < 10):
			b = '0' + b
		if (int(c) < 10):
			c = '0' + c
		'''
		return (a + ":" + b + ":" + c)




#获取配置文件把节假日等不可控日期写在配置文件中
def get_config():
	config = configparser.ConfigParser()
	config_file = open('Config.ini')
	config.readfp(config_file)
	config_file.close()

	return config

#格式化初始数据，删除不必要的列
def geshihuashuju(zhongzhuan):
	#del zhongzhuan[0]	#删除第一行部门数据(部门数据保留下来)
	del zhongzhuan[2]   #删除考勤号码列
	#['小狗财务', '李京', '2019/03/26 13:03:43', '1', '', '指纹/密码/卡/面部', '']

	try:
		for m in range(6):
			#循环4次 0-3=====#删除机器号#删除编号#删除比对方式#删除卡号
			del zhongzhuan[3]
	except:
		pass
	#print("TANUKI,,,,,,,,zhongzhuan", zhongzhuan)
	#zhongzhuan ['小狗财务', '张姗', '2019/03/29 13:24:06']
	try:
		date, time = zhongzhuan[2].split(' ')
	except Exception as e:
		date = ''
		time = ''

	#将zhongzhuan中的日期和时间分离为两个数据
	del zhongzhuan[2]	#删除时间和日期一条list数据
	zhongzhuan.append(date)
	zhongzhuan.append(time)
	#print("TANUKI,,,,,,,,zhongzhuan", zhongzhuan)
	#['技术部', '冯泳铭', '2019/03/06', '18:31:08']
	return zhongzhuan

#对date进行从小到大的排序
def datesort(date):
	date = list(set(date))
	for i in range(0, len(date)):
		for j in range (0, i):
			if datetime.datetime.strptime(date[i], '%Y/%m/%d') <= datetime.datetime.strptime(date[j], '%Y/%m/%d'):
				date[i],date[j] = date[j],date[i]

	return date


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
		6 : '周日',
  }
	
	day = datetime.datetime.strptime(date[2], '%Y/%m/%d').weekday()
	date[2] = date[2] + " " + week_day_dict[day]
	return date






if __name__ == "__main__":
	main()
	input("程序执行完毕，请手动关闭窗口...")