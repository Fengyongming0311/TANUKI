#coding:utf-8
import win32api
from time import sleep
import threading


filepath = "D:\\test.flac"


winmideaplayer = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"

foobar2000 = "D:\\foobar2000\\foobar2000.exe"








win32api.ShellExecute(0, 'open', winmideaplayer, filepath, '' , 1)

sleep(0.5)
    
win32api.ShellExecute(0, 'open', foobar2000, filepath, '' , 1)