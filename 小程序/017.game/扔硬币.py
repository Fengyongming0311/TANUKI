#coding:utf-8
import random
zhengmian = 0
fanmian = 0
n = 0
while n < 100000000:
	jieguo = random.randint(1,2)

	if jieguo == 1:
		zhengmian +=1
	else:
		fanmian += 1

	n +=1

print (zhengmian)


print (fanmian)