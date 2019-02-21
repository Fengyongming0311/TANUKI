# encoding: utf-8
import importlib,sys
importlib.reload(sys)
import requests
import re
import time
time1=time.time()


link=u'ftp://ygdy8:ygdy8@yg72.dydytt.net:8202/阳光电影www.ygdy8.com.暴裂无声.HD.1080p.国语中英双字.mp4'
dest_resp = requests.get(link.strip())
#dest_resp = requests.get(link)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#保存数据的路径及文件名
path = u'C:\\白夜追凶\\baoliewusheng.mp4'
f = open(path, 'wb')
f.write(data)
f.close()


time2 = time.time()

print (u'ok,下载完成!')
print (u'总共耗时：' + str(time2 - time1) + 's')