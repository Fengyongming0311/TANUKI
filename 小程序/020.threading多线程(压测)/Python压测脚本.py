# -*- coding: utf-8 -*-

from http import client


#接口请求调用的模块
import urllib
import urllib.parse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json
import threading, time
from fake_useragent import UserAgent

interface = "/api/user/loginPC?"
url = "https://core.qasa.chtfund.com"
#调通了以后url改为interface  host改为url
param = "code=H029829&password=MTIzNDU2"
#请求参数

#起的线程数
concurrent_thread_count = 10

#每个线程循环多少次
iterate_count = 1

#设置headers
ua = UserAgent()
header = {'Host': 'core.qasa.chtfund.com',
			'User-Agent': ua.random,
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

class RequestThread(threading.Thread):
	def __init__(self, thread_name):
		threading.Thread.__init__(self)
		self.test_success_count = 0
		self.test_fail_count = 0

	def run(self):
		i = 0
		while i < iterate_count:
			self.Post_Request()
			i += 1

	def Post_Request(self):
		try:
			response = requests.request('POST', url + interface, params=param, headers=header, verify=False)
			#response = requests.request('POST', url + interface, params=param, headers=header, verify=False,allow_redirects=False)
			print('dondake')
			#rsps = response.getresponse()
			rsps = response.text
			rsps = json.loads(rsps)
			#print(rsps)
			if rsps["status"] == '0000':
				self.test_success_count += 1
			else:
				self.test_fail_count += 1
		except Exception as e:
			print(e)
		finally:
			response.close()



start_time = time.time()
#获取开始时间的时间戳
threads = []
#
i = 0
#while 如果i 小于开局设置的起的线程数
while i < concurrent_thread_count:
	t = RequestThread("thread" + str(i))
	t.run()
	threads.append(t)
	t.start()
	i += 1

for thr in threads:
	thr.join()

print("测试完成...")
time_span = time.time() - start_time
#time_span 执行时间 等于 结束时间减去开始时间
all_count = total_success = total_fail = 0
#设置所有次数和总成功次数和总失败次数

for t in threads:
	total_success += t.test_success_count
	total_fail += t.test_fail_count
all_count += total_success + total_fail

print("total %s Requests. " % all_count)
print("%s Requests success. " % total_success)
print("%s Requests fail. " % total_fail)
print("total %s seconds." % time_span)











































































