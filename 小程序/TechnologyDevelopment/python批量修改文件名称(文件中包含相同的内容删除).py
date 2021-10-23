#coding:utf-8

import os


#设置你要删除的文件名
delete_name = "Aqua Timez -"

filefolder = "AQ"
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


for filename in files:
	#先判断文件名中是否包含要被删除的字符串
	if delete_name in filename:
		#包含进入下面改名字

		a,b = filename.split(delete_name)
		#通过delete_name 将需要修改的文件名取出来
		#print ("aaaaaaaaaaa",a)
		#print ("Newname---------",NewName)

		NewName = b.lstrip()



		
		try:
			os.chdir(DIR_PATH)
			os.rename(filename,NewName)
			#print ("------重新命名了%s个数据------"%str(count))
			print ("---重新命名了%s个数据---\n%s------旧名字\n%s------新名字"%(str(count),filename,NewName))
			count += 1
		except Exception as e:
			#print ("重新命名数据失败，失败原因---------",e)
			print ("%s重新命名为%s失败，失败原因---"%(filename,NewName), e)



	else:
		pass
		#不包含delete_name直接pass




