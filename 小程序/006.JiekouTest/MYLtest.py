# -*- coding: utf-8 -*-
import requests
import threading
import time
import logging

format = "线程 %(thread)d,时间 %(asctime)s %(message)s"
logging.basicConfig(format=format)
logging.root.setLevel(level=logging.INFO)
cityIDs = [110000, 120000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000, 340000, 350000, 360000, 370000, 410000, 420000, 430000, 440000, 450000, 460000, 500000, 510000, 520000,530000, 610000, 620000, 630000, 640000, 650000]

class postrequests():
    def __init__(self):
        #self.url = "http://release-api-pandora.limiketang.com/gorgons/school/getProvince"
        self.url = "http://api-pandora.limiketang.com/gorgons/school/getCityByProvinceId"

    def post(self,chuancanshu):
        try:
            #r = requests.post(self.url)
            #r = requests.post(self.url, data= {"id":110000, "keyword": "", "token": ""} ,headers={'Content - Type': 'application / json'})
            #r = requests.post(self.url, data='{"id":120000, "keyword": "", "token": ""}',headers={"Content-Type": "application/json"})
            r = requests.post(self.url, data='{"id":%s, "keyword": "", "token": ""}'%chuancanshu,headers={"Content-Type": "application/json"})
            print("r.text,为============",r.text)
            logging.info("")
        except Exception as e:
            print(e)


def getProvince(chuancanshu):
    getProvince = postrequests()
    return getProvince.post(chuancanshu)


if __name__ == '__main__':
    for chuancanshu in cityIDs:
        getProvince(chuancanshu)
'''
try:
    i = 0
    # 开启线程数目
    tasks_number = 5
    print('>>>>>>测试启动<<<<<<')
    time1 = time.perf_counter()
    while i < tasks_number:
        t = threading.Thread(target=getProvince)
        t.start()
        i += 1
    time2 = time.perf_counter()
    times = time2 - time1
    print(f">>>>>>平均执行时间:{times / tasks_number}s<<<<<<")
    print(f">>>>>>总耗时时间:{times}s<<<<<<")
except Exception as e:
    print(e)
'''