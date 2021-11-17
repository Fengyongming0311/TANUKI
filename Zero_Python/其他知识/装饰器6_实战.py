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
@wrapper1
@wrapper2
def target():
	print ("我是目标")


规则和规律 wrapper1  wrapper2  TRAGET wrapper2  wrapper1
"""


def wrapper1(fn):    #fn:
	def inner(*args, **kwargs):
		print ("这里是wrapper1  进入")   # 1
		ret = fn(*args, **kwargs)   # wrapper2.inner
		print ("这里是wrapper1  出去")   # 5
		return ret
	return inner

def wrapper2(fn):  # fn:target
	def inner(*args, **kwargs):
		print ("这里是wrapper2  进入")  #2
		ret = fn(*args, **kwargs)   #target
		print ("这里是wrapper2  出去")  #4
		return ret
	return inner

@wrapper1        #target = wrapper1(wrapper2(target))    => target: wrapper1.inner
@wrapper2        #target = wrapper2(target)    => target: wrapper2.inner
def target():
	print ("我是目标")  #3


target()


"""
这里是wrapper1  进入
这里是wrapper2  进入
我是目标
这里是wrapper2  出去
这里是wrapper1  出去
"""