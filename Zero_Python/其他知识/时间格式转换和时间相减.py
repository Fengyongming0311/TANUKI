#coding:utf-8
import time
import datetime
tup = datetime.datetime(2021, 11, 22, 23, 27, 4)
#数据库返回的时间 类型为datetime.datetime
# print (tup)
# print (type(tup))
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#此时now的类型为 str
now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
#再将str转为datetime.datetime， 就可以进行比较或者相减了
# print (now)
# print (type(now))



c = str(now - tup)
h,m,s = c.split(":")
print (c)
print (type(c))
print (h)
print (int(m))
print (type(int(m)))
print (s)
