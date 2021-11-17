#coding:utf-8



"""
装饰器本质上是一个闭包
作用：
	在不改变原有函数的调用的情况下，给函数增加新的功能
	直白：可以在函数前后添加新功能，但是不改原来的代码

装饰器常用地方 ：在用户登陆的地方，日志，

装饰器雏形：

def weapper(fn):              wrapper：装饰器， fn:目标函数
	def inner():
		#在目标函数执行之前....
		fn()                #执行目标函数
		#在目标函数执行之后....

	return inner         #千万别加括号
	#不加括号是返回 inner函数
	#return inner()
	#加了括号 是返回 inner函数的执行结果

"""


def guanjia(game):
	def inner():
		print ("打开外挂")
		game()            #玩起来了
		print ("关闭外挂")
	return inner

@guanjia                         # 相当于play_dnf = guanjia(play_dnf)
def play_dnf():
	print ("你好啊，我叫赛利亚，今天又是美好的一天！")



@guanjia
def play_lol():
	print ("德玛西亚！！！！")

play_dnf()
play_lol()

"""
如果游戏多了，什么守望先锋、饥荒、拳皇都开挂， 导致满篇的下边赋值，所以用@guanjia替换

play_dnf = guanjia(play_dnf)    #让管家把游戏重新封装一遍，我这边把原来的游戏替换了
play_lol = guanjia(play_lol)    #让管家把lol也重新封装一遍

play_dnf = guanjia(play_dnf)    #让管家把游戏重新封装一遍，我这边把原来的游戏替换了
play_lol = guanjia(play_lol)    #让管家把lol也重新封装一遍

play_dnf = guanjia(play_dnf)    #让管家把游戏重新封装一遍，我这边把原来的游戏替换了
play_lol = guanjia(play_lol)    #让管家把lol也重新封装一遍

play_dnf = guanjia(play_dnf)    #让管家把游戏重新封装一遍，我这边把原来的游戏替换了
play_lol = guanjia(play_lol)    #让管家把lol也重新封装一遍


"""