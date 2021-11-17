#coding:utf-8
"""
3.函数名称可以当作变量一样进行赋值操作
"""

def func1():
	print ("我是函数1")

def func2():
	print ("我是函数2")




func1 = func2
#将一个函数当作变量赋值给了另一个函数

func1()

