#coding:utf-8

"""
装饰器本质上是一个闭包
作用：
	在不改变原有函数的调用的情况下，给函数增加新的功能
	直白：可以在函数前后添加新功能，但是不改原来的代码

装饰器常用地方 ：在用户登陆的地方，日志，

通用装饰器的写法：

def weapper(fn):              wrapper：装饰器， fn:目标函数
	def inner(*args， **kwargs):
		#在目标函数执行之前....
		fn(*args, **kwargs)                #执行目标函数
		#在目标函数执行之后....
		retuen ret

	return inner         #千万别加括号


	@wrapper
	def target():
		pass


	target()  # =>  inner()




一个函数可以被多个装饰器 装饰

"""


def guanjia(game):
	def inner(*args, **kwargs):
		print ("打开外挂")
		ret = game(*args, **kwargs)   #这里是目标函数的执行，这里是能够拿到从目标函数返回的返回值的.
		print ("关闭外挂")
		return ret
	return inner

@guanjia
def play_dnf(username, password):
	print ("我要开始玩dnf了，", username, password)
	print ("你好啊，我叫赛利亚，今天又是美好的一天！")
	return "一把屠龙刀"




def play_lol(username, password, hero):
	print ("我要开始玩lol了，",username, password, hero)
	print ("德玛西亚！！！！")

ret = play_dnf("admin", "123456")    #运行的是inner
print (ret)

