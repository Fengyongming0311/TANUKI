#coding:utf-8
import threading
from time import sleep, ctime

loops = [8,2]

def loop(nloop, nsec):
    print ('开始独立线程========', nloop, 'at:', ctime())
    sleep(nsec)
    print ('loop', nloop, 'done at:', ctime())


def main():
    print ('开始整体线程 at:', ctime())
    threads = []
    #创建一个空线程组

    nloops = range(len(loops))
    #循环次数？？把数字强制转化成range(0,2)

    #创建线程
    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i]))
        threads.append(t)


    #开始线程
    for i in nloops:
        threads[i].start()
        #所有的线程都创建了之后，再一起调用 start()函数启动，而不是创建一个启动一个。
        # 而且，不用再 管理一堆锁（分配锁，获得锁，释放锁，检查锁的状态等），
        # 只要简单地对每个线程调用 join()函数就可 以了。

    print ("threads[i].start()--------------执行结束")
    #等待所有结束线程
    for i in nloops:
        threads[i].join()
        #.join()等待线程终止


    print ('结束整体线程====:', ctime())


if __name__ == '__main__':
    main()