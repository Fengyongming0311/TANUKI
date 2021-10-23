'''
for循环用于遍历一个集合，依次访问集合中的每个项目
集合可以是元组、列表、字典等数据结构
'''
"""
注意，for循环中的else子句也属于循环的一部分，最后一次循环结束后将执行else子句。
"""



for x in range(-1,2):
    if x > 0:
        print ("正数：", x)
    elif x == 0:
        print ("零:", x)
    else:
        print ("负数：", x)
else:
    print ("循环结束")