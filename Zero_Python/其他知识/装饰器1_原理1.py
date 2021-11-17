#coding:utf-8

#外挂管家


"""
这样成了管家在玩游戏了，所以加inner()
def guanjia(game):
	print ("打开外挂")
	game()            #玩起来了
	print ("关闭外挂")
"""
def guanjia(game):
	def inner():
		print ("打开外挂")
		game()            #玩起来了
		print ("关闭外挂")
	return inner


def play_dnf():
	print ("你好啊，我叫赛利亚，今天又是美好的一天！")




def play_lol():
	print ("德玛西亚！！！！")


play_dnf = guanjia(play_dnf)    #让管家把游戏重新封装一遍，我这边把原来的游戏替换了

play_dnf()         #此时运行的是管家给的内层函数inner

play_lol = guanjia(play_lol)    #让管家把lol也重新封装一遍


"""

print ("打开dnf外挂")
play_dnf()  
print ("关闭dnf外挂")

print ("打开lol外挂")
play_lol()  
print ("关闭lol外挂")
每次都得手动开不同的游戏，麻烦，所以想方便需要一个管家让他按照我每次的游戏自动开启外挂

"""
