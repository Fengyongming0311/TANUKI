"""
break语句可以使程序跳出循环语句，从而执行循环体之外的程序，即break语句可以提前结束循环。
"""


x = int(input("输入x的值："))

y = 0

for y in range(0,100):
    if x == y:
        print ("找到数字：",   x)
        break

else:
    print ("没有找到数字")