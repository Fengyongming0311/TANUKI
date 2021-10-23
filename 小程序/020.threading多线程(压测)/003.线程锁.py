#coding:utf-8
"""
我们先调用 thread.allocate_lock()函数创建一个锁的列表，并分别调用各个锁的 acquire()函数 获得锁。
获得锁表示“把锁锁上”。锁上后，我们就把锁放到锁列表 locks 中。
下一个循环创建线程，每个线程都用各自的循环号，睡眠时间和锁为参数去调用 loop()函数。
为什 么我们不在创建锁的循环里创建线程呢？有以下几个原因：
(1) 我们想到实现线程的同步，所以要让“所 有的马同时冲出栅栏”。
(2) 获取锁要花一些时间，如果你的线程退出得“太快”，可能会导致还没有获得 锁，线程就已经结束了的情况。
在线程结束的时候，线程要自己去做解锁操作。
最后一个循环只是坐在那一直等（达到暂停主线程的目的），直到两个锁都被解锁为止才继续运行。
"""
#我们应该避免使用 thread 模块，原因是它不支持守护线程。当主线程退出时，
# 所有的子线程不论它 们是否还在工作，都会被强行退出。有时我们并不期望这种行为，
# 这时就引入了守护线程的概念。threading 模块则支持守护线程。



import _thread
from time import sleep, ctime
loops = [6, 2]

def loop(nloop, nsec, lock):
    print ('开始循环', nloop, 'at:', ctime())
    print (nsec)
    sleep (nsec)
    print ('循环结束', nloop, 'Done at:', ctime())

    #解锁
    lock.release()


def main():
    print ('整体程序开始at:', ctime())

    locks = []
    #以loops数组创建列表，并赋值给nloops
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        #开始锁定
        lock.acquire()   #acquire 获得，取得
        #获得锁表示'把锁锁上'。
        # 追加到locks[]数组中(下)
        locks.append(lock)
        #锁上后，我们就把锁放到锁列表locks中。


    #执行多线程

    for i in nloops:
        _thread.start_new_thread(loop, (i,loops[i], locks[i]))

    '''
    下面代码为加锁，没下边代码称居开始就结束了
    '''
    for i in nloops:
        #lock.locked()   返回锁的状态：如果已经被某个线程获取，则返回True，否则返回False。
        while locks[i].locked():
            pass


    print ('整体程序结束:', ctime())

if __name__ == '__main__':
    main()
