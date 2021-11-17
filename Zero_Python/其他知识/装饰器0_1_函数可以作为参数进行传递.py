#coding:utf-8
"""
1.函数可以作为参数进行传递
"""

def func():
	print ("我是函数")


def gggg(fn):     #fn要求是个函数     在函数里传参为函数的不能带括号，带了意义就变了
	fn()          #func()  传了进来


gggg(func)
