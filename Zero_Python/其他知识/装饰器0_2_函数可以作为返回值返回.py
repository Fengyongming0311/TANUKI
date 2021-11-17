#coding:utf-8
"""
2.函数可以作为返回值返回
"""

def func():
	def inner():
		print ("123木头人")
	return inner


ret = func()

ret()
#想让内层函数运行（在最外边），那就是ret加括号
