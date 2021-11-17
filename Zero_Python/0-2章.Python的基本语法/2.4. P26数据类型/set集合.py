#coding:utf-8
#set集合

#s = {1,2,3, "呵呵"}
#集合存的可哈希数据类型，  即不可变的数据类型， int,str,tuple,bool
#print (s)

"""
#创建空,元组，列表，字符串
s = set()
t = tuple()
l = list()
str = str()
"""
s = set()
#创建空集合

s.add("赵本山")
s.add("范伟")
s.add("马化腾")


s.remove("范伟")
#删除

s.add("沈腾")
#修改，想要修改先删除再新增


print(s)

for item in s:
	print (item)