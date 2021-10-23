#局部变量是函数（方法）中的变量
#全局变量是能够被不同函数，类或者文件共享的变量，在函数之外定义的变量都可以称为全局变量
#全局变量可以被文件内部的任何函数和外部的文件访问
# 在文件开头定义全局变量
_a = 1

_b = 2

def add():
    global _a
    #引用全局变量_a ,这里使用了global关键字，global用于引用全局变量

    _a = 3
    #在方法中引用了全局变量，并改变全局变量的内容，会导致全局变量的内容出了函数内容也发生改变
    return "_a = _b = ", _a + _b

def sub():
    global _b
    _b = 4
    print (_a)
    print (_b)
    return "_a - _b = ", _a - _b

print (add())

print (sub())

print (_b)