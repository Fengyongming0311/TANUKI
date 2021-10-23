#coding:utf-8
import _thread
from time import sleep, ctime

#loops = [4, 2]


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('start:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    #启动多线程，两个线程同时开始
    sleep(6)
    #如果我们没有让主线程停下来，那主线 程就会运行下一条语句，显示“all end”，
    #然后就关闭运行着 loop0()和 loop1()的两个线程并退出了。
    print('all end:', ctime())


if __name__ == '__main__':
    main()