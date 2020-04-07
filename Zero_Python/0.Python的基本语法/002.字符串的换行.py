#字符串的换行
#写法1
sql = "select id,name \
from dept \
where name = 'A'"

print (sql)

#写法2
sql2 = "select id,name " \
    "from dept " \
    "where name = 'A'"

print (sql2)