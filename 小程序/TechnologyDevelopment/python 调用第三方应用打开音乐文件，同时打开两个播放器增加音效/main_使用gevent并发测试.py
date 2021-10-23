#coding:utf-8
import win32api
from time import sleep
import threading


filepath = "D:\\test.flac"


winmideaplayer = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"

foobar2000 = "D:\\foobar2000\\foobar2000.exe"

potplayer = "C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe"


import gevent
from gevent.queue import Queue


def func():
    #sleep(0.3)
    #win32api.ShellExecute(0, 'open', winmideaplayer, filepath, '' , 1)
    win32api.ShellExecute(0, 'open', potplayer, filepath, '' , 1)

def func2():
    #sleep(0.3)
    win32api.ShellExecute(0, 'open', foobar2000, filepath, '' , 1)
    #win32api.ShellExecute(0, 'open', potplayer, filepath, '' , 1)

q = Queue()
gevent.joinall(
    [
        gevent.spawn(func2),
        gevent.spawn(func),
    ]
)