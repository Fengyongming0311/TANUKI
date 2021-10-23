#coding= utf-8

import os

DIR_PATH = "D:\\"

os.chdir(DIR_PATH)
#用于改变当前工作目录到指定的路径。



# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 %s" % retval)