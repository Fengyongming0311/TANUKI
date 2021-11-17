#coding:utf-8

dic = {
	"赵四": "特别能歪嘴",
	"刘能": "老，老四啊...",
	"大脚": "跟这个和那个搞对象",
	"大脑袋": "瞎折腾...",
}

'''

#1.可以用for循环，直接拿到key

for key in dic:
	#print (key)
	print (key, dic[key])


#2.希望把所有的key全部保存在一个列表中
#print(dic.keys())
print(list(dic.keys()))             #拿到所有的key了   ！！！用keys

#3. 希望把所有的value放在一个列表中
#print(dic.values())
print(list(dic.values()))           #拿到所有的value



#4.直接拿到字典中的key和value
print (dic.items())



for iitem in dic.items():
	key = iitem[0]
	value = iitem[1]
	print (key, value)
	
#解构 （元组和列表都可以执行该操作）
a, b = (1,2)
print (a)
print (b)	

'''

for item in dic.items():
	key, value = item
	#确定 item中只有两项元素，所以用解构
	print (key, value)


#升级字典1_循环和嵌套.py
for key,value in dic.items():
	print (key, value)