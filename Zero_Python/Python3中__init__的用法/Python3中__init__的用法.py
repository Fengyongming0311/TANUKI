class Cat:
	"""定义了一个Cat类"""
	
	#初始化对象
	def __init__(self, new_name, new_age):
		self.name = new_name
		self.age = new_age

	#方法
	def eat(self):
		print("猫在吃鱼....")

	def drink(self):
		print("猫正在喝kele.....")

	def introduce(self):
		print("%s的年龄是:%d"%(self.name, self.age))

#创建一个对象
tom = Cat("汤姆", 40)
tom.eat()
tom.drink()
#tom.name = "汤姆"
#tom.age = 40
tom.introduce()
print ("#############################################################################")
lanmao = Cat("蓝猫", 10)
#lanmao.name = "蓝猫"
#lanmao.age = 10
lanmao.introduce()

"""
__init__()方法，在创建一个对象时默认被调用，不需要手动调用(重要)
 __init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形  参，例如__init__(self,x,y)
 __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
"""