class Student: 
	def __init__(self, name, grade):  #类似于C++中的有参构造函数
		self.name = name
		self.grade = grade

	def print_grade(self):
		print("%s grade is %s" % (self.name,self.grade))

s1 = Student("Tom", 8)  # 创建对象s1
s2 = Student("Jerry", 7)  # 创建对象s2

s1.print_grade()
s2.print_grade()


"""
这种形式在定义方法时，就直接给定了两个参数name和grade，且属性值不允许为空。实例化时，直接传入参数。


总结：
1、self是形式参数，当执行s1 = Student(“Tom”, 8)时，self等于s1；当执行s2 = Student(“sunny”, 7)时，self=s2。
2、两种方法的区别在于定义函数时属性赋值是否允许为空和实例化时是否直接传入参数，个人觉得第二种更为简洁。
"""