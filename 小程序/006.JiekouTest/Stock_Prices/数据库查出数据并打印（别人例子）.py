import pymysql
import xlwt
from self import self
#  �����װ��sql���
from aa.sql import qx_qb, None1
from aa.sql import qx_xy
from aa.sql import qx_gn


def open_sql():
	self.charset = "utf8"  # �趨���εĸ�ʽ
	self.database = "gy_core"  # ���ӵĿ���
	self.port = 3306  # �˿ں�
	self.password = "test112233"  # ���ݿ������
	self.user = 'gyadmin'  # ��¼���ݿ���˺�
	self.host = '127.0.0.1'  # ���ݿ��ip

	open_sql1 = pymysql.connect(host=self.host,
								user=self.user,
								password=self.password,
								port=self.port,
								database=self.database,
								charset=self.charset)

	#  ����mysql���α깦�ܣ�����һ���α����
	cur = open_sql1.cursor()
	if not cur:
		raise Exception("���ݿ�����ʧ�ܣ�")
	#   ��ѯ��䣬���÷�װ�õ����

	sql1 = qx_xy
	# ʹ���α����ִ��SQL��䣻
	cur.execute(sql1, None1)
	#  ��ȡ���еķ���ֵ
	res = cur.fetchall()
	for r in res:
		print(r)
	fields = cur.description
	#  ɾ��ȫ��֮ǰд���ı�����Ϣ
	open("C:/Users/dell/Desktop/jb.csv", 'w').close()
	#  �ѷ�������д��ָ���ı���
	book = xlwt.Workbook()
	#  �����ļ�������
	sheet = book.add_sheet('qiye_inf', cell_overwrite_ok=True)

	for fie_id in range(0, len(fields)):
		sheet.write(0, fie_id, fields[fie_id][0])
	for row in range(0, len(res) + 1):
		for col in range(0, len(fields)):
			sheet.write(row, col, u'%s' % res[row - 1][col])
	#  ָ�����ݴ洢�ļ��ľ���·��
	book.save('C:/Users/dell/Desktop/jb.csv')



