list = ["apple", "banana", "grape", "orange"]


list.append("watermelon")
#在列表的末尾追加了一个西瓜

list.insert(1,"grapefruit")
#在列表的第二个位置插入葡萄柚

print (list)


list.remove("grape")

print (list)

#list.remove("a")
#从列表中移除a，因为没有这个元素，所以会报错

print (list.pop())
#pop()取出列表中最后一个元素，即"弹出"最后一个进入列表的元素