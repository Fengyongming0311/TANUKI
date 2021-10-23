"""
continue 语句也是用来跳出循环的语句，但是与break不同，continue不会跳出整个循环体，
只是跳出当前的循环，然后继续执行后边的循环。
"""

x = 0

for i in [1,2,3,4,5]:
    if x == i:
        continue
    x += i


print ("x的值为", x)