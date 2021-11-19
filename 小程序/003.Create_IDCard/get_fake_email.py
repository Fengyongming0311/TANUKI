#coding:utf-8
"""
随机生成邮箱数据
fengyongming0311 @ 163 .com

1.自定义前缀 name
全英文     1
全数字 (只有qq邮箱是纯数字)
英文数字混合 2    随机，不能超过18位 前边是英文后边是数字不能混着来
首字母是英文其余是数字邮箱    3    2,3可以和一起写
英文下划线数字    下划线也写个随机数，如果是1 那就有下划线，如果是0就没有下划线

2. @
3.各种邮箱服务器域名  email
可以弄个列表随机取，又分为国外邮箱和国内邮箱
国内用1  国外用2   默认1
"""
import random
import string

#生成随机名称
def username():
	type = random.randint(0,1)
	if type == 0:
		n = list()
		length = random.randint(6,18)
		for i in range(length):
			w = random.choice(string.ascii_lowercase)
			n.append(w)
		str  = ''.join(n)
		return str
	else:
		n = list()
		m = list()
		#建立空列表
		length = random.randint(6,18)
		#length所有字符长度
		abc = random.randint(1,length -1)
		#字母长度
		no = length - abc
		#数字长度

		for i in range(abc):
			w = random.choice(string.ascii_lowercase)
			n.append(w)
		part1 = ''.join(n)   #生成随机字符串
		#b  = ''.join((random.choice(range(10))) for k in range(no))
		#b = {''.join(random.choices(s,k=8)) for I in range(60000)}
		for i in range(no):
			k = random.choice(string.digits)
			m.append(k)
			#print (m)
		part2 = ''.join(m)   #生成随机数字
		#下方判断下划线
		underline = random.randint(0,1)
		#print ("uuuuuuuuuuuuuuuuunderline=====",underline)
		if underline == 0:
			return part1 + part2
			#无下划线
		else:
			return part1 + "_" + part2

def addressname():
	email = ["@gmail.com","@yahoo.com", "@msn.com", "@hotmail.com", "@live.com", "@qq.com", "@163.com","@126.com", "@sina.com", "@sohu.com"]
	return random.choice(email)


def get_fake_email(username, addressname):
	fake_email = username() + addressname()
	return fake_email



for i in range (10000):
	print (get_fake_email(username,addressname))







