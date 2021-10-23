class Student:  
	def __init__(self):  # 类似于c++中的默认构造函数
		self.name = None
		self.grade = None
		
	def print_grade(self):
		print("%s grade is %s" % (self.name,self.grade))


s1 = Student()  # 创建对象s1
s1.name = "Tom"
s1.grade = 8

s2 = Student()  # 创建对象s2
s2.name = "Jerry"
s2.grade = 7

s1.print_grade()
s2.print_grade()


"""
这种形式在__init__方法中，只有一个self，指的是实例的本身，但是在方法的类部，
包含两个属性，name， grade。它允许定义一个空的结构，当新数据来时，
可以直接添加。实例化时，需要实例化之后，再进行赋值。
"""