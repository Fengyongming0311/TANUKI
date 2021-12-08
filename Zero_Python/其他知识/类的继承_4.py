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


#公司的开发类继承了公司的员工类
class Developer(Employee):
	raise_count = 1.5


	def __init__(self, first, last, pay, pro_language):
		super().__init__(first, last, pay)
		#super 显式的调用父类的f l p
		self.pro_language = pro_language

#经理类，employees是经理手下管理的人数
class Manager(Employee):
	def __init__(self, first, last, pay, employees = None):
		super().__init__(first, last, pay)
		if employees is None:
			employees = []
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)


	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emp(self):
		for emp in self.employees:
			print (emp.fullname())


dev1 = Developer('John', 'Schafer', 50000, 'Python')
dev2 = Developer('Bob', 'Schafer', 60000, 'Java')
# print (dev1.first, dev1.last, dev1.email, dev1.pay, dev1.pro_language)
# print (dev2.first, dev2.last, dev2.email, dev2.pay, dev2.pro_language)


mgr_1 = Manager('Sue', 'Smith', 9000, [dev1])
# print (mgr_1.first, mgr_1.last, mgr_1.email, mgr_1.pay)
#
# mgr_1.add_emp(dev2)
# mgr_1.print_emp()
#
# mgr_1.remove_emp(dev2)
# mgr_1.print_emp()


#判断哪个类是哪个类的实例
#判断mgr_1 是不是Manager实例
print (isinstance(mgr_1, Manager))
print (isinstance(mgr_1, Employee))
#判断mgr_1 是不是Employee实例


#判断继承关系
#判断Developer 是不是Employee子类
print (issubclass(Developer, Employee))



#判断Manager 是不是Employee子类
print (issubclass(Manager, Employee))



#判断Manager 是不是Developer子类
print (issubclass(Manager, Developer))