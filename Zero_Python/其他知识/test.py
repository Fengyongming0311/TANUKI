class dog(object):   #用class定义类
	"dog class"     #对类的说明
	#构造函数或者是构造方法，也可以叫初始化方法
	def __init__(self,name):       #self 相当于d = dog(d,"AAAA")
		self.name = name


	def sayhi(self):    #类方法
		"sayhi funcation"    #对类方法的说明
		print("hello,i am a dog,my name is ",self.name)


d = dog("AAAA")   #定义一个d的对象，叫实例
d.sayhi()    #调用实例的方法