#coding:utf-8
import ChtwmCompare
import time
'''
600887 SH
002475 SZ
'''
"""
传入股票编号，深交所调用ChtwmCompare_qasaSZ 上交所调用ChtwmCompare_qasaSH 港股调用ChtwmCompare_qasaSH，传入的high是最高价，low是最低价，如果实时股票价格高于设置的最高或者最低都会print报警 
"""
######################
#这里是股票编号
#比如说伊利股份就是ylgf = "600887"
###########SH###########
zqlv = "600138"
#中青旅
jtty = "601609"
#金田铜业
lxjm = "002475"
#立讯精密
xbky = "601168"
#西部矿业
ylgf = "600887"
#伊利股份
slw = "600460"
#士兰微
baogang = "600010"
#包钢股份
zgzm = "601888"
#china中免
hsdz = '600570'
#恒生电子
#########SZ#########


bfhc = "002371"
gfly = "002460"
tqly = "002466"
shougang = "000959"
byd = "002594"
ofg = "002456"
fzcm = "002027"
#分众传媒
glm = "002340"
#格林美 做T
hdyy = "000963"
#华东医药
wly = "000858"
#五粮液

###########HK##########
zxgjhk = "00981"
zgyzhk = "08083"
gflyhk = "01772"
tengxun = "00700"
xm = "01810"
albb = "09988"
youzanhk = "08083"
sihuanyiyaohk = "00460"
#HK四环医药
jdwl = "02618"
#京东物流
SoundLock = "off"
#声音锁SoundLock，on就是开声音    off关闭声音
while 1:
	#600000 SH


	high1 = 92
	low1 = 85
	
	pl1 = ChtwmCompare.ChtwmCompare_qasaSH(high1, low1, SoundLock, hsdz)
	print (pl1)

	'''
	high2 = 19
	low2 = 12
	pl2 = ChtwmCompare.ChtwmCompare_qasaSH(high2, low2, SoundLock, xbky)
	print (pl2)


	high3 = 999
	low3 = 0
	pl3 = ChtwmCompare.ChtwmCompare_qasaSH(high3, low3, SoundLock, slw)
	print (pl3)


	high12 = 370
	low12 = 320
	pl12 = ChtwmCompare.ChtwmCompare_qasaSH(high12, low12, SoundLock, zgzm)
	print (pl12)
	'''
	###############################################################################
	'''
	#002475 SZ
	high4 = 666
	low4 = 1
	pl4 = ChtwmCompare.ChtwmCompare_qasaSZ(high4, low4, SoundLock, bfhc)
	print (pl4)


	high5 = 999
	low5 = 1
	pl5 = ChtwmCompare.ChtwmCompare_qasaSZ(high5, low5, SoundLock, fzcm)
	print ("FZCM",pl5)

	
	high11 = 320
	low11 = 280
	pl11 = ChtwmCompare.ChtwmCompare_qasaSZ(high11, low11, SoundLock, wly)
	print ("WLY",pl11)


	high6 = 999
	low6 = 90
	pl6 = ChtwmCompare.ChtwmCompare_qasaSZ(high6, low6, SoundLock, gfly)
	print (pl6)

	
	high8 = 190
	low8 = 148
	pl8 = ChtwmCompare.ChtwmCompare_qasaSZ(high8, low8, SoundLock, byd)
	print (pl8)
	'''

	##################
	
	#print ("#HK#")
	'''	
	high7 = 1.75
	low7 = 1.49
	pl7 = ChtwmCompare.ChtwmCompare_uataHK(high7, low7, SoundLock, youzanhk)
	print (pl7)
	

	high9 = 3.96
	low9 = 2.65
	pl9 = ChtwmCompare.ChtwmCompare_uataHK(high9, low9, SoundLock, sihuanyiyaohk)
	print (pl9)
	'''
	high10 = 500
	low10 = 0
	pl10 = ChtwmCompare.ChtwmCompare_uataHK(high10, low10, SoundLock, jdwl)
	print (pl10)

	
	##################
	print ("=====%s====="%(time.strftime('%H:%M:%S',time.localtime(time.time()))))
	#打印一下当前时间
	time.sleep(25)
	#这里设置多少秒调一次接口，太频繁会被封IP，一般5秒以上就行
