#coding:utf-8
import win32api
from time import sleep
import threading



filepath = "D:\\test.flac"

filepath2 = "D:\李荣浩-念念又不忘.flac"

#winmideaplayer = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"

#foobar2000 = "D:\\foobar2000\\foobar2000.exe"






def winmideaplayer():
	win32api.ShellExecute(0, 'open', "C:\\Program Files\\Windows Media Player\\wmplayer.exe", filepath, '' , 1)


def foobar2000():
	win32api.ShellExecute(0, 'open', "D:\\foobar2000\\foobar2000.exe", filepath2, '' , 1)


def Groove():
	win32api.ShellExecute(0, 'open', "C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe", filepath, '' , 1)
    
a = 1

if __name__ == '__main__':
	threads = [threading.Thread(target = winmideaplayer()),
			threading.Thread(target = foobar2000()),threading.Thread(target = Groove())]
	for t in threads:
		t.start()

		