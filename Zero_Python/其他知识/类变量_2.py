#coding:utf-8
"""
init中，self.XXXXX名称是自己定义的，可以不是传进来的参数

类变量与实例变量区别
类变量：每个实例可以共享的变量，每个实例可以用类变量里的值也可以修改类变量的值不影响其他实例
self实例变量：每个实例自己使用的变量，修改里面的值不影响其他实例

"""
class Employee:
	#__init__方法是创建实例的初始化方法，也可以称为构造方法（构造函数）
	#self 当前的实例, 实例变量
	#raise_count是类变量！！是每个实例可以共享的变量
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

	def fullname(self):
		return '{}{}'.format(self.first, self.last)


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_count)


print (Employee.num_of_emp)
emp1 = Employee("Test","User1", 5000)
emp2 = Employee("Test","User2", 5000)

print (Employee.num_of_emp)

# Employee.raise_count = 1.04
# print(Employee.raise_count)
# emp1.raise_count = 1.05
# print (emp1.raise_count)
# print (emp2.raise_count)



# print (Employee.__dict__)
# 查看Employee类的字典：可以看到类里面的属性和方法
# print (emp1.__dict__)
#查看实例里面的字典属性

# print (emp1.pay)
# emp1.raise_count = 2
# emp1.apply_raise()
# print (emp1.pay)
#
#
#
# print (emp2.pay)
# emp2.apply_raise()
# print (emp2.pay)