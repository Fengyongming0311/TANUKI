#coding:utf-8
class Dog:
	dogbook = {"黄色": 30, "黑色": 20, "白色": 10}
	#__init__是构造方法
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		#此处省略若干行，应该更新dogbook的数量

	#实例方法：定义时，必须把self作为第一个参数，可以访问实例变量，只能通过实例名访问
	def bark(self):
		print (f"{self.name} 叫了起来")


	#类方法可以访问类变量，可以通过实例名或类名访问
	#类方法是不用传self,能直接调用类变量
	#定义时，必须把类作为第一个参数
	@classmethod
	def dog_num(cls):
		num = 0
		for v in cls.dogbook.values():
			num = num + v
		return num

	#静态方法其实就是类里的普通方法（函数）,def的时候不用传入self了
	#静态方法，不强制传入self或者cls,他对类和实例都一无所知，就是普通方法做一件事而已，不能访问类变量，也不能访问实例变量；
	#可以通过实例名或者类名访问
	@staticmethod
	def total_weights(dogs):
		total = 0
		for i in dogs:
			total = total + i.weight
		return total


print (f'共有 {Dog.dog_num()}  条狗')

d1 = Dog('大黄', '黄色', 10)
#定义了一条狗 d1
d1.bark()
print (f'共有 {Dog.dog_num()}  条狗')

d2 = Dog('旺财', '黑色', 8)
d2.bark()

print (f'狗共重 {Dog.total_weights([d1,d2])}  公斤')

