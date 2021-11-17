#coding:utf-8
#set集合交集 并集 差集
"""
s1 = {"刘能", "赵四", "皮长山"}
s2 = {"刘科长", "冯乡长", "皮长山"}

print (s1 & s2)
#交集
print (s1.intersection(s2))


print(s1 | s2)
#并集
print (s1.union(s2))



print(s1 - s2)
print (s1.difference(s2))
#差集


#重要作用：可以去除重复

s1 = {"周杰伦", "昆凌", "蔡依林", "侯佩岑"}

s1.add("周杰伦")
#两个一模一样的元素不可能在同一集合
"""

lst = ["周杰伦", "昆凌", "蔡依林", "侯佩岑","周杰伦", "昆凌", "蔡依林", "侯佩岑","周杰伦", "昆凌", "蔡依林", "侯佩岑"]
print (lst)

don = list(set(lst))

print (don)
print (type(don))
#去除重复数据之后是无序的，但是可以去重