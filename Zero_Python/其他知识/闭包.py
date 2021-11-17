#coding:utf-8
"""
闭包：本质，内层函数对外层函数的局部变量的使用，此时内层函数被称为闭包函数
    1.可以让一个变量常驻于内存
	2.可以避免全局变量被修改

"""

def func():
	a = 10
	def inner():
		#print (a)
		#写一个计数器
		nonlocal a
		a += 1

		return a

	return inner
ret = func()

#inner  => ret =>什么时候执行
#执行时间不确定
#得保证inner常驻与内存
r1 = ret()
print (r1)


r2 = ret()
print (r2)
