#coding:utf-8
import gevent
from gevent import monkey
monkey.patch_all()
import requests
from locust import TaskSet, task, HttpUser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Msg(TaskSet):
    #@task(1)
    #def get_blog(self):

    def on_start(self):
        payload = {"registerId":"1114a89792c4c2a6b2e","userAgent":"恒天基金\/5.4.0 (iPhone; iOS 13.2.3; Scale\/3.00)","version":"13.2.3","netType":"1","channelType":"3","mobile":"18612859513","brand":"iPhone6sPlus","clientIp":"192.168.200.101","deviceId":"2ba48ebf1298766850588dc6af9591a6","accountType":"1","password":"F\/VkkFhAWbGw5JJCSj4HJ0GuB5tuUqDJ3nbGED4fdJ+KvM+T\/LX\/b+XkT7y5p5FtFoen5Nejh5o2ct98JGtucpdCUifFmu43JpxxKKFy3jyC4DIzOjLqaF6GL3xyR7Xw5BuihOvG4BJ3bavSL64bFZT\/lMUnDNFJ06WfjhlHiG0=","ignoreVerify":"true","operator":"1"}
        header = {"Content-Type": "application/json"
                  }



        req = self.client.post("/login",data=payload ,headers=header, verify=False)
        if req.status_code == 0000:
            print("success")
        else:
            print("fails")

    @task(3)
    def My (self):
        header1 = {"Content-Type": "application/json"
                   }
        req = self.client.post("/My",data={} ,headers=header1, verify=False)
        if req.status_code == 0000:
            print("view_my success")
        else:
            print("view_my fails")

class websitUser(HttpUser):
    tasks = [Msg]
    min_wait = 1000  # 单位为毫秒
    max_wait = 3000  # 单位为毫秒


if __name__ == "__main__":
    import os

    os.system("locust -f locust_masai_test.py --host=https://app.haomaojf.com/app/account/frontend/loginCheckNew")