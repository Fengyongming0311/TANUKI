#coding:utf-8

import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
'''
当我们要爬一个网页的时候，只需要如下流程
导入两个库，一个用于请求，一个用于网页解析
请求网页，获得源代码
初始化soup对象，使其可以调用更简单易用的方法
用浏览器打开网页，右键-检查，使用那个鼠标定位你要找的资源的位置
分析那个位置的源代码，找到合适的用于定位的标签及属性
编写解析代码，获得想要的资源
'''
# 传入URL
r = requests.get('https://www.csdn.net/')

# 解析URL
soup = BeautifulSoup(r.text, 'html.parser')
content_list = soup.find_all('div', attrs = {'class': 'title'})

for content in content_list:
    print(content.h2.a.text)