#调用全局变量

import gl
#导入前面创建的文件gl.py 即模块gl
def fun():
    print (gl._a)
    print (gl._b)

fun()
"""
应尽量避免使用全局变量，因为不同模块都可以自由访问全局变量，会导致全局变量的不可预知性
"""