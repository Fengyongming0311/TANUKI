#coding:utf-8
"""

"""
class Employee:
	raise_count = 1.04
	num_of_emp = 0

	def __init__(self, first, last ,pay):
		self.first = first
		self.last = last
		self.email = first + "." + last + "@company.com"
		self.pay = pay
		Employee.num_of_emp += 1
		#在类中每创建一个（实例）,员工数都加1


	#这个是实例方法
	def fullname(self):
		return '{}{}'.format(self.first, self.last)


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_count)


	#将实例内容输出成字符串
	#重写了__repr__,repr 用于调试开发中，如果有重写__str__则调用str
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return "{}-{}".format(self.fullname(), self.email)


	def __add__(self, other):
		return self.pay + other.pay


dev1 = Employee('John', 'Schafer', 50000)
dev2 = Employee('Bob', 'Schafer', 60000)

"""
from datetime import datetime

now = datetime.now()
print (str(now))
print (repr(now))
"""