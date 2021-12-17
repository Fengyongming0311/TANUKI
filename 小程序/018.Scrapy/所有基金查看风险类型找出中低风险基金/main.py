#coding:utf-8
"""
如果用爬虫需要加上假的请求头欺骗
不行的话就使用Selenium方式访问
"""
'''
headers释义：
Accept:客户端可识别的内容类型列表。
Accept-Language: 访问者希望采用的语言或语言组合
Cache-Control:控制缓存
User-Agent:产生请求的浏览器类型
Connection:keep-alive保持长链接，close为不希望使用长链接
Referer: 链接来源
'''
"""
发送请求后，返回各种形式的响应内容：
　　1）r.text：以文本格式返回响应内容
　　2)r.content：以字节格式返回响应内容
　　3)r.json()：以json格式返回相应内容，因为就算请求出错也会返回一串json格式的字符串。所以可以使用r.status_code或者r.raise_for_status来判断响应是否成功
　　4)如果在原始请求中设置了stream=True，可以使用r.raw.read()
"""
import time
import requests
testdata = "000689,001933,001704"

data = testdata.split(",")

index = "http://fund.eastmoney.com/"

def getdata(*args, **kwargs):
    from fake_useragent import UserAgent

    ua = UserAgent()
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': ua.random,
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
                #'Content-Type':'application/json',
               }

    for i in data:
        url = index + i + ".html"
        #拼出了整个请求地址
        #print(url)

        html = requests.get(url = url, headers = headers)
        html = html.text.encode("utf-8", 'ignore').decode("gbk", 'ignore')
        print (html)

        time.sleep(60)



getdata()

