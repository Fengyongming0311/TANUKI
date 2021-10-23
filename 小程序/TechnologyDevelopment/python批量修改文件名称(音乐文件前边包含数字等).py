#coding:utf-8

import os


#设置你要删除的文件名
delete_name = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

filefolder = "初音miku"
#文件夹名称
count = 1





PROJECT_DIR_PATH = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
#获取当前python文件所在的路径
#C:\Users\1\Desktop\


DIR_PATH = os.path.join(PROJECT_DIR_PATH, filefolder)
#增加data文件路径
#C:\Users\1\Desktop\Mr.Children

files = os.listdir(DIR_PATH)
#获取文件夹下的所有文件名


for i in delete_name:
	#print (i)
	#i 是每次轮询中要删除的字符
	for filename in files:
		if i in filename:
			NewName = filename.lstrip(i)
			NewName = NewName.lstrip()
			#print (NewName)

			#开始将剔除的新名字替换
			try:
				os.chdir(DIR_PATH)
				#用于改变当前工作目录到指定的路径。
				os.rename(filename,NewName)
				print ("---重新命名了%s个数据---\n%s------旧名字\n%s------新名字"%(str(count),filename,NewName))
				count += 1

			except Exception as e:
				print ("%s重新命名为%s失败，失败原因---"%(filename,NewName), e)


