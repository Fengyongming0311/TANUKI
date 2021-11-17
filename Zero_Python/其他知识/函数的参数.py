#coding:utf-8
"""
形参:在函数定义的时候，需要准备一些变量来接受信息
	1.位置参数，按照位置一个一个去声明变量
	2.默认值参数，在函数声明的时候给变量一个默认值，如果实参不传递信息，此时默认值生效，否则就不生效
	顺序： 位置参数在前面 ，默认值参数在后边
	3.动态传参，
		1.*args, 表示接收所有的位置参数的动态传参
		2.**kwargs, 表示接收所有的关键字的动态传参

	4.混合使用
		顺序： 位置 >*args > 默认值 > **kwargs

	上述参数可以随意搭配使用

实参：实际调用的时候传递的信息
	1.位置参数，按照位置进行传递参数
	2.关键字参数，按照参数的名字进行传递参数
	3.混合参数，
		顺序：位置参数放前面，关键字参数放后面  -->否则报错！官方不让这么干
		实参在执行的时候，必须要保障形参有数据

"""

"""
def chi(zhu, fu, tang, tian):
	print (zhu, fu, tang, tian)



#chi("大米饭", "西红柿炒鸡蛋", "紫菜蛋花汤", "哈根达斯")

#chi(zhu = "小米饭", tang = "胡辣汤", fu = "韭菜炒大腰子", tian = "老中街冰棍")

chi(zhu = "小米饭", "胡辣汤", fu="韭菜炒大腰子", tian="老中街冰棍")


def luru(name, age, gender = "男"):
	print (name, age, gender)
"""

'''
def chi(*food):          # * 表示位置参数的动态传参， *接收到的值会被统一放在一个元组里面
	print(food)


chi ("大米饭", "烧茄子", "紫菜蛋花汤", "哈根达斯")
chi ("大米饭")
chi ("大米饭", "烧茄子")
chi ("大米饭", "紫菜蛋花汤")
chi ("大米饭", "紫菜蛋花汤", "紫菜蛋花汤")


def chi(**food):           # **表示接收关键字的动态传参，接收到的所有参数都会被处理成字典
	print(food)


chi(fu = "木须柿子", zhu= "小米饭")


def func(a, b, c = "哈哈", *args, **kwargs):
	print (a, b, c, args, kwargs)

#这样的话 c = "哈哈"会被 *args里的第三个替换掉，如果 需要c必须等于哈哈，得把*args放在前边

func(1,2,3,4,5,6,7,8,9, hello = 456, hahalou = 654)


def func(a, b,  *args, c = "哈哈", **kwargs):
	print (a, b, c, args, kwargs)

#这时如果想把c = 哈哈改变值， 则在传参的时候直接改就可以
func(1,2,3,4,5,6,7,8,9, hello = 456, hahalou = 654)

func(1,2,3,4,5,6,7,8,9, c = "马上没钱吃饭了！！！", hello = 456, hahalou = 654)


def func(*args, **kwargs):       #没有限制的接收任何参数
	print (args, kwargs)

func()
func(1)
func (1,2,3,4,4, a = 2)
func(1,2,3,4, c = 4,a = 2)


'''

stu_lst = ["流川枫", "樱木花道","大老王", "本田夏树", "花泽类", "木村拓哉", "中居正广","V6", "相叶雅纪"]

def func(*args):
	print(args)



func(*stu_lst)          # *在实参位置，是把列表打散成位置参数进行传递
						# **在实参位置，可以把字典自动转化成关键字参数进行传递

