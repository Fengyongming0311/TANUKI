#coding:utf-8

"""
装饰器本质上是一个闭包
作用：
	在不改变原有函数的调用的情况下，给函数增加新的功能
	直白：可以在函数前后添加新功能，但是不改原来的代码

装饰器常用地方 ：在用户登陆的地方，日志，

装饰器雏形：

def weapper(fn):              wrapper：装饰器， fn:目标函数
	def inner(*args， **kwargs):
		#在目标函数执行之前....
		fn(*args, **kwargs)                #执行目标函数
		#在目标函数执行之后....

	return inner         #千万别加括号
	#不加括号是返回 inner函数
	#return inner()
	#加了括号 是返回 inner函数的执行结果

"""


def guanjia(game):
	#                        这里的* 表示接受所有参数，打包成元组和字典
	def inner(*args, **kwargs):  #inner 添加了参数， args 一定是一个元组   kwargs 一定是字典
		print ("打开外挂")
		#下   这里的*，** 表示把args元组和kwargs字典打散成 位置参数以及关键字参数传递进去
		game(*args, **kwargs)            #玩起来了
		print ("关闭外挂")
	return inner

@guanjia
def play_dnf(username, password):
	print ("我要开始玩dnf了，", username, password)
	print ("你好啊，我叫赛利亚，今天又是美好的一天！")



@guanjia
def play_lol(username, password, hero):
	print ("我要开始玩lol了，",username, password, hero)
	print ("德玛西亚！！！！")

play_dnf("admin", "123456")    #运行的是inner
play_lol("adminadmin", "88888888","大盖伦")

