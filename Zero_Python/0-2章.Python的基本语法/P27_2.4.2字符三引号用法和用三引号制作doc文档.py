#python字符串可以有单引号和双引号两个等价

#三引号用法
str = '''he say "hello world!"'''

print (str)


'''
三引号另一用法是制作文档字符串。Python每个对象都有一个属性__doc__,这个属性用于描述该对象的作用。
'''

#三引号制作doc文档

class Hello:
    '''这是hello class'''
    #对Hello类的描述，该字符串将被存放在类的__doc__属性中
    def printHello():
        """print hello world"""
        #描述了printHello,并把字符串存放在该函数的__doc__属性中。
        print ("hello world!")


print (Hello.__doc__)

print (Hello.printHello.__doc__)
