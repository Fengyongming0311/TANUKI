#coding:utf-8
"""
init中，self.XXXXX名称是自己定义的，可以不是传进来的参数
"""
class Employee:
	#__init__方法是创建实例的初始化方法，也可以称为构造方法（构造函数）
	#self 当前的实例, 实例变量
	def __init__(self, first, last ,pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@company.com"
		self.pay = pay


	def fullname(self):
		return '{}{}'.format(self.first, self.last)




emp1 = Employee("Test","User1", 5000)
emp2 = Employee("Test","User2", 5000)

emp2.pay = 6000

print (emp1.pay, emp1.first, emp1.last, emp1.email)
print (emp2.fullname())

