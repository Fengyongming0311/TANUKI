import requests, json
import urllib3
from fake_useragent import UserAgent

ua = UserAgent()
# urllib3.disable_warnings()
url = "http://172.16.1.44:8080/village/vip/list/1"
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': ua.random,
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }

'''
headers释义：
Accept:客户端可识别的内容类型列表。
Accept-Language: 访问者希望采用的语言或语言组合
Cache-Control:控制缓存
User-Agent:产生请求的浏览器类型
Connection:keep-alive保持长链接，close为不希望使用长链接
Referer: 链接来源
:
:
'''