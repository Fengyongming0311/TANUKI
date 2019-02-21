#coding:utf-8
from fake_useragent import UserAgent
user_agent_list = UserAgent()
ua = user_agent_list.random
headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'www.meizitu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua
    }



print (headers)