class Anything:
	def init_person(self, _name, _age):
		self.name = _name
		self.age = _age


#a1 = Anything('Dick', 5)
#因为创造了Anything(任何生物)的类别，该类别没有"属性"，有一方程init_person 以及方程的两个变量name和age
#因为没有__init__方程，所以创建a1不需要输入任何的"属性"参数
#这也导致了这个类定义的模糊--这个类别下的新成员a1到底是神马？
#所以在创建新成员试图输入名字和年龄这两个属性时，报错了

a2 = Anything()
#因为之前报错了，所以我们创建了一个对他毫无任职的新成员a2

a2.init_person('Dick', 5)
#但是，这个类里有一个方程叫做“创建人类成员”（init_person），并且它有俩个输入变量"名字"和"年龄"。
#我们尝试调用这个方程把a2"变成"一个人类
print (a2.name)
print (a2.age)