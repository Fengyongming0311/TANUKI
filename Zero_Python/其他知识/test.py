#coding:utf-8
def func(*args, **kwargs):       #没有限制的接收任何参数
	if 'address' in kwargs.keys():
		print (kwargs['address'])
	else:
		print ("没有")


func()
func(1)
func (1,2,3,4,4, a = 2)
func(1,2,3,4, c = 4,a = 2,address = ["fengyongming0311@sohu.com","guozilidazuo@qq.com","342469367@qq.com"])

