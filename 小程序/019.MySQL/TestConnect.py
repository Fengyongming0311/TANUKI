# encoding=utf-8

import pymysql
import os, sys, string
import time
"""
name:               名称
type:               类型，类别
useshiduan:         使用时段 
usepinlv:           使用频率
season:             使用季节
biyaochengdu:       必要程度
guanlian:           关联产品
"""
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='00000000', db='mydata', charset='utf8')  # 连接数据库
cur = conn.cursor()  # 使用cursor()方法获取操作游标

# 增加数据

cur.execute(
    "INSERT INTO lifeneed(name, type, useshiduan, usepinlv, season, biyaochengdu, guanlian, beizhu) \
    VALUES('袜子', '衣物', '每天', '高', '秋冬', '高', '', '目前建议每天换一次')"
    )
    #插入单条数据
conn.commit()  # 没有这个无法真正提交数据



#查询出数据
selectall = "select * from lifeneed"
cur.execute(selectall)
alldata = cur.fetchall()
# 如果有数据返回，就全部输出
for i in alldata:
    print (i)

'''
sel = cur.execute("select * from lifeneed")
w = int(cur.rowcount)
print
'总共查询出', w, '条数据！'
k = raw_input('是否打印所有查询数据？Y/N？')
if k == 'y':
    for row in cur.fetchall():
        for r in row:
            print
            r
            print
            ""

else:
    print
    ""
'''

cur.close()  # 关闭游标，游标不可用

