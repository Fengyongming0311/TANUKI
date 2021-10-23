#coding:utf-8
import random
zongshu = 100000000
yi = 0
er = 0
san = 0
si = 0
wu = 0
liu = 0
n = 0


while n <= zongshu:
	jieguo = random.randint(1,6)

	if jieguo == 1:
		yi +=1
	elif jieguo == 2:
		er += 1
	elif jieguo == 3:
		san += 1
	elif jieguo == 4:
		si += 1
	elif jieguo == 5:
		wu += 1
	elif jieguo == 6:
		liu += 1
	n +=1

def zhuanhua(num):
	number = num /zongshu
	number = str(number).split('.')[0] + '.' + str(number).split('.')[1][:4]

	number = str(float(number)*100) + '%'
	return number


one = zhuanhua(yi)
two = zhuanhua(er)
three = zhuanhua(san)
four = zhuanhua(si)
five = zhuanhua(wu)
six = zhuanhua(liu)


print (one)
print (two)
print (three)
print (four)
print (five)
print (six)