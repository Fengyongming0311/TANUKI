#coding:utf-8
def func(an):    #此时an收到的是一个函数
	print (an)    #打印出的是target()的内存地址
	#上：函数名实际上就是一个变量名，都表示一个内存地址
	an()      #执行这个函数



def target():
	print ("我是target")


c = 456
func(target)