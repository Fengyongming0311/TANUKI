#coding:utf-8
"""
init中，self.XXXXX名称是自己定义的，可以不是传进来的参数

类变量与实例变量区别
类变量：每个实例可以共享的变量，每个实例可以用类变量里的值也可以修改类变量的值不影响其他实例
self实例变量：每个实例自己使用的变量，修改里面的值不影响其他实例

"""
class Employee:
	#__init__方法是创建实例的初始化方法，也可以称为构造方法（构造函数）
	#self 当前的实例, 实例变量  每一次调用类都会有自己的实例 ，比如说dog1 dog2 dog3



	#raise_count是类变量！！类变量属于整个类   是每个实例可以共享的变量，不属于哪个实例
	raise_count = 1.04
	num_of_emp = 0
	#员工初始数量为0 ，在类中每创建一个（实例）,员工数都加1

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

	#类方法
	#因为是类方法，所以必须得有cls关键字，cls是class简写
	@classmethod
	def set_raise_count(cls, count):
		cls.raise_count = count
		#cls 就是class 所以能.raise_count
		#改的是cls所以 就是class里的都变了

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		#Employee(first, last, pay) 就是下边那个一样的东西创建了对象
		return cls(first, last, pay)


	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


import datetime
my_date = datetime.date(2021, 12, 4)
print(Employee.is_workday(my_date))

#类方法主要用途：通过类方法创建对象
# emp3_str_1 ="Jay-Chou-18000"
#
# emp3 = Employee.from_string(emp3_str_1)
#
# print (emp3.email)


emp1 = Employee("Test","User1", 5000)
emp2 = Employee("Test","User2", 5000)

# emp1.set_raise_count(1.9)
# print (emp1.raise_count)
# print (emp2.raise_count)