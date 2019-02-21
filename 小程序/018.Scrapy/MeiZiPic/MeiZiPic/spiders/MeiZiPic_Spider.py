#coding=utf-8
import scrapy
from scrapy.http import Request,HtmlResponse
import os
#from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from fake_useragent import UserAgent

class MeiZiPicSpider(scrapy.spiders.Spider):
    name = 'MeiZiPic'#爬虫名
    allowed_domians = ["meizitu.com"]#允许域名列表
    start_urls = ['http://www.meizitu.com/a/',]#起始链接列表

    for i in range(2,91):
        start_urls.append('http://www.meizitu.com/a/list_1_'+str(i)+'.html')

    #随机的Scrapy增加随机请求头user_agent
    user_agent_list = UserAgent()
    ua = user_agent_list.random
    ub = user_agent_list.chrome
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'www.meizitu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua
    }

    #重写方法，设置请求头
    def make_requests_from_url(self, url):
        return Request(url, headers = self.headers, dont_filter = True)

    #下载图片方法
    def imageDownload(self, response):
        file_path = response.meta['file_path']
        with open(file_path, 'wb') as f:
            f.write(response.body)

    #解析单个图片集的响应
    """
    从此页面上提取到的其它图片集的链接，由scrapy请求后，仍将响应结果交给回调函数（callback = self.parseImageArticle）
    parseImageArticle来解析。而图片链接则在scrapy请求后交由下载函数处理（callback = self.imageDownload）。
    """
    def parseImageArticle(self,response):
        #获取图片链接列表
        src_links = response.xpath('//img[re:test(@src,"http://mm.howkuai.com/wp-content/uploads/20\d{2}a/\d{2}/\d{2}/\d+.jpg")]/@src').extract()
        #获取图片集名称，用以创建文件夹(NO)
        base_path = os.path.join("image",response.xpath('//div[contains(@class,"metaRight")]/h2/a/text()').extract()[0])
        #下载图片请求头(NO)
        header = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': MeiZiPicSpider.ub
        }
        #文件夹不存在则创建
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        #下载图片
        for i in range(len(src_links)):
            #获取用以存储的文件名
            file_path = os.path.join(base_path, str(i)+'.jpg')
            #传递文件名，并使用imageDownload方法解析(NO)
            yield Request(src_links[i],meta = {'file_path':file_path}, headers = header,callback = self.imageDownload)
        #获取当前页面的其他图片集链接
        links = response.xpath('//a[re:test(@href,"http://www.meizitu.com/a/\d+.html")]/@href').extract()
        print ("获取当前页面的其他图片集链接*********def parseImageArticle************",links)
        #请求其他图片集，使用此方法解析
        for url in links:
            yield Request(url, headers = self.headers, callback = self.parseImageArticle)

    #解析start_urls的响应
    def parse(self,response):
        #获取图片集连接（将所有的列表页面地址放在一个列表里links）
        links = response.xpath('//a[re:test(@href,"http://www.meizitu.com/a/\d+.html")]/@href').extract()
        print ("获取图片集连接地址为*********def parse************",links)
        #对所有的图片集进行请求
        for url in links:
            yield Request(url, headers = self.headers, callback = self.parseImageArticle)