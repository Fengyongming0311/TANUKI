import pymysql
import xlwt
from self import self
#  导入封装的sql语句
from aa.sql import qx_qb, None1
from aa.sql import qx_xy
from aa.sql import qx_gn


def open_sql():
	self.charset = "utf8"  # 设定传参的格式
	self.database = "gy_core"  # 连接的库名
	self.port = 3306  # 端口号
	self.password = "test112233"  # 数据库的密码
	self.user = 'gyadmin'  # 登录数据库的账号
	self.host = '127.0.0.1'  # 数据库的ip

	open_sql1 = pymysql.connect(host=self.host,
								user=self.user,
								password=self.password,
								port=self.port,
								database=self.database,
								charset=self.charset)

	#  开启mysql的游标功能，创建一个游标对象
	cur = open_sql1.cursor()
	if not cur:
		raise Exception("数据库连接失败！")
	#   查询语句，调用封装好的语句

	sql1 = qx_xy
	# 使用游标对象执行SQL语句；
	cur.execute(sql1, None1)
	#  获取所有的返回值
	res = cur.fetchall()
	for r in res:
		print(r)
	fields = cur.description
	#  删除全部之前写入文本的信息
	open("C:/Users/dell/Desktop/jb.csv", 'w').close()
	#  把返回数据写入指定文本内
	book = xlwt.Workbook()
	#  定义文件的名称
	sheet = book.add_sheet('qiye_inf', cell_overwrite_ok=True)

	for fie_id in range(0, len(fields)):
		sheet.write(0, fie_id, fields[fie_id][0])
	for row in range(0, len(res) + 1):
		for col in range(0, len(fields)):
			sheet.write(row, col, u'%s' % res[row - 1][col])
	#  指定内容存储文件的绝对路径
	book.save('C:/Users/dell/Desktop/jb.csv')



