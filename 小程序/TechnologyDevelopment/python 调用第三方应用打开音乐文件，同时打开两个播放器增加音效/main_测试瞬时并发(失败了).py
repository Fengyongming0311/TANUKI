#coding:utf-8
import win32api
from time import sleep
import threading


filepath = "D:\\California.flac"


winmideaplayer = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"

foobar2000 = "D:\\foobar2000\\foobar2000.exe"






from threading import Thread  # 导入线程函数
from time import sleep  # 导入时间休眠函数


def task1():  # 定义任务1
    win32api.ShellExecute(0, 'open', winmideaplayer, filepath, '' , 1)


def task2():  # 定义任务2
    win32api.ShellExecute(0, 'open', foobar2000, filepath, '' , 1)


def main():  # 定义main函数
    t1 = Thread(target=task1)  # 定义线程t1，线程任务为调用task1函数，task1函数的参数是6
    t2 = Thread(target=task2)  # 定义线程t2，线程任务为调用task2函数，task2函数无参数
    t1.start()  # 开始运行t1线程
    t2.start()  # 开始运行t2线程


if __name__ == '__main__':
    main()  # 调用main函数