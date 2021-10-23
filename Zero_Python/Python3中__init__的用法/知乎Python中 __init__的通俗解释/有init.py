class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age





"""
因为定义了init，所以必须传入name,age ,否则不能称为"人类"
"""
'''
p1 = Person()

print (p1.name)

print (p1.age)
'''
p2 = Person('James', 10)

print (p2.name)

print (p2.age)

"""
当输入p1 = Person()
程序报错了，因为要创建一个人类新成员 就必须输入姓名和年龄两个必要选项


而当输入p2 = Person('James', 10)
程序运行成功，一个10岁的名叫James的人类新成员被创建成功！

并且可以通过输入

p2.name
p2.age

来查看这位新成员的名字和年龄

"""