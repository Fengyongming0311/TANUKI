#coding:utf-8

import random


#1到100中每次随机生成一个数字
a = random.randint(0,100)
#print (a)


#用于生成一个0到1的随机符点数: 0 <= n < 1.0
b = random.random()
#print (b)


#从一个列表，元组或字符串中随机选一个值
lst = ["比亚迪","伊利股份","微软集团","中软国际","恒生电子"]
c = random.choice(lst)
#print (c)

yuanzu = ("足球","跳远","钓鱼","篮球","棒球","跳水","赛车","艺术体操")
d = random.choice(yuanzu)
#print (d)

str = "祖国完全统一一定能够实现"
e = random.choice(str)
#print (e)



#用于将一个列表中的元素打乱。
f = ["比亚迪","伊利股份","微软集团","中软国际","恒生电子","分众传媒", "卓胜微","广汽集团"]
random.shuffle(f)
#print (f)


#随机生成小写字母
import random
import string
zimu = random.choice(string.ascii_lowercase)
num = random.choice(string.digits)
#print (zimu)
#print (num)
#print (type(num))


