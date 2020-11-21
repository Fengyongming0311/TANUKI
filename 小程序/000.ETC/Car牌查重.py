#coding:utf-8


newdata = []
#定义列表

#获取文档内容
with open ('TaxiNo.txt', 'r') as f:
	data = f.readlines()
#print (data)
#获得所有车号


data = [x.strip() for x in data if x.strip() != '']
#print (data)
#清洗数据，删除空行，删除回车符

try:
	#小写字母转大写字母
	for i in data:
		i = i.upper()
		newdata.append(i)
except Exception as e:
	print ("小写字母转大写字母，并添加到新列表报错=========",e)
	pass

#print (newdata)



#查重
from collections import Counter

ChaChong = dict(Counter(newdata))

print ({key:value for key,value in ChaChong.items()if value > 1})
# 展现重复元素和重复次数