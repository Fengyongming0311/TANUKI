import threading
import random
import time
import requests
import logging

format = "%(asctime)s 线程id %(thread)d |||||(ﾉ>ω<)ﾉ - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
logging.basicConfig(format=format)
logging.root.setLevel(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format=format)

logging.info('==========测试开始==========')


class ThreadLocal():
    def __init__(self):
        self.local = threading.local()
        #self.url = 'http://release-api-pandora.limiketang.com/gorgons/user/getMyScholarship'
        self.url = 'http://api-pandora.limiketang.com/gorgons/user/getMyScholarship'
        # self.ids = [0,0,0,12,27,32,963,1002,1317,2099,2189,3443,3714,4469,4472,5250,9231,9337,9398,9430,10043,12496,13148,13476,14264,14883,15464,15579,15811,16193,16575,16666,16902,16997,17555,17994,17996,18307,18350,18568,20163,20333,20402,20442,20465,20515,20520,20579,20617,20805,20817,20821,20824,20842,20848,20851,20988,21057,21274,21310,21586,21627,21643,21668,21767,21775,22029,22146,22153,22640,23072,23708,24750,24943,25010,25694,26673,26676,27390,29678,29695,29981,29984,30643,30713,31267,31638,34468,34472,34489,34496,34505,34506,34514,34548,34566,34590,34892,35195,35487,35714,35766,35790,35949,37502,38755,43135,44339,44880,48949,51949,52031,53008,53253,54511,55533,56850,64001,69666,70978,71280,72445,80793,81767,85352,85917,86266,87777,88002,90164,90245,90368,91219,91842,92376,92380,92390,94153,95164,96568,96893,100043,101129,101861,102133,102387,102876,102982,103455,103482,103578,103581,103588,103592,103622,103768,103941,104748,104786,104796,105195,105207,105315,105396,105434,105642,105799,105903,105905,105912,105965]
        self.ids = [21310, 21586, 21627, 21643]

    def run(self):
        # time.sleep(random.random())
        # self.local.number = []
        # for i in range(10):
        #     self.local.number.append(random.choice(range(10)))
        id = iter(self.ids)
        self.local.r = ''
        while id:
            try:
                i = next(id)
                logging.info("迭代i=", i)
                self.local.r = requests.post(self.url,
                                             data='{"uid":"%s","token":"ODQ0NXAyRVUyY1ZSUFkzU1NhVThqYk9ETXJNbVR1VFd3WVhzQzBjSjd0SFJSOE1G"}' % i,
                                             headers={
                                                 "Content-Type": "application/json"})
                # print(i, threading.currentThread(), self.local.r.text)
                logging.info(self.local.r.text)
            except StopIteration:
                break


# threadLocal = ThreadLocal()
# threads = []
# for i in range(5):
#     t = threading.Thread(target=threadLocal.run)
#     t.start()
#     threads.append(t)
# # for i in range(5):
# #     threads[i].join

def getProvince():
    getProvince = ThreadLocal()
    return getProvince.run()


if __name__ == '__main__':
    getProvince()

try:
    i, j = 0
    # 开启线程数目
    tasks_number = 2
    threadLocal = ThreadLocal()
    threads = []
    logging.info('>>>>>>测试启动<<<<<<')
    time1 = time.perf_counter()
    while i < tasks_number:
        t = threading.Thread(target=threadLocal.run)
        t.start()
        threads.append(t)
        i += 1
    while j < tasks_number:
        threads[i].join
    time2 = time.perf_counter()
    times = time2 - time1
    print(f">>>>>>平均执行时间:{times / tasks_number}s<<<<<<")
    print(f">>>>>>总耗时时间:{times}s<<<<<<")
except Exception as e:
    logging.info(e)
