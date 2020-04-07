#可以把全局变量放到一个专门的文件中，便于统一管理和修改。
#这里调用全局变量文件global_bianliang
"""
注意：尽可能避免使用全局变量。因为不同的模块（包）都可以自由的访问全局变量，可能会导致全局变量的不可预知性。对于global_bianliang.py中的全局变量
如果程序员甲修改了_a 的值，程序员乙同时也要使用_a 这时可能导致程序中的错误，这种错误很难发现和更正
"""
import global_bianliang

def fun():
    print (global_bianliang._a)
    print (global_bianliang._b)


fun()