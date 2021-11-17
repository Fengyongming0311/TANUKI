#coding:utf-8
"""
global:  在局部，引入全局变量

nonlocal： 在局部，引入外层的局部变量

"""
'''
a = 10

def func():
	global a     #把外部的全局变量引入到局部
	a = 20


print (a)


'''


def func():
	a = 10
	def func2():
		nonlocal a    #向外找一层，看看有没有该变量，如果有就引入，如果没有，继续向外一层，直到全局（不包括全局变量）
		a =20
	func2()
	print (a)

func()