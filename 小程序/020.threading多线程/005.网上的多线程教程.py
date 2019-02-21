#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)


def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
#创建线程 列表
t1 = threading.Thread(target = music,args=(u'周杰伦——轨迹',))
#定义线程一操作
threads.append(t1)
#把线程一加入到线程列表中
t2 = threading.Thread(target = move,args=(u'枪火',))
#定义线程2操作
threads.append(t2)
#将线程2加入到线程列表中
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        # setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
        # 如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，
        # 当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，
        # 直接就退出了，同时子线程也一同结束。
        t.start()
        #这么执行好像不是并发，而是顺序执行的...

    print ("all over %s" %ctime())
    #　从执行结果来看，子线程（muisc 、move ）
    # 和主线程（print "all over %s" %ctime()）都是同一时间启动，但由于主线程执行完结束，所以导致子线程也终止。
    # 程序仍需调整