#coding:utf-8
import tanuki

import requests



url = "http://hq.sinajs.cn/list=sh515030"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)

a = str(response.text)
tanuki.printtype(a)

