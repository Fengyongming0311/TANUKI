# -*- coding: utf-8 -*-
import scrapy
from SunShine.items import SunshineItem
import time


class SunShineSpider(scrapy.Spider):
    # 爬虫名
    name = 'SunShine'
    # 爬虫域
    allowed_domains = ['jpfans.com']
    # 设置URL
    url = 'http://www.jpfans.com/thread.php?fid=68&search=&page='
    # 设置页码
    Page = 1
    # 默认url
    start_urls = [url + str(Page)]
    # 如果没有特别指定其他的url，spider会以start_urls中的链接为入口开始爬取

    #parse是scrapy.Spider处理http response的默认入口
    def parse(self, response):
        # xpath匹配规则
        '''
        print ("********************ここからスタートするのは俺様のプログラムだ**************************")
        print (response)
        print ("********************俺様のプログラムが終わった、結果を見ってくれ**************************")
        '''
        for each in response.xpath("//tr[@class='t_two']"):

            item = SunshineItem()
            #item["Theme"] = each.xpath("./td[2]/a/text()")
            item["Theme"] = each.xpath("./td[2]/a/text()").extract()
            #print ("开始打印书局开始打印书局开始打印书局开始打印书局开始打印书局开始打印书局")
            #print (item["Theme"])
            #print (type(item["Theme"]))
            #print ("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGZZZZZZZZZZZZZZZZ")
            #item["Theme"] = each.xpath("./td[2]/a/text()").extract()[0]
            #item["Theme"] = each.xpath("./td[2]/a/text()")[0].extract()
            #item["Theme"] = each.xpath("./td[2]/a/text()")[0].extract()[0]
            #爬取的主题名字
            if item["Theme"]:
                pass
            else:
                item["Theme"] = each.xpath("./td[2]/a/b/font/text()").extract()
            '''
            print("找寻内容为item[Theme]==========================================================")
            print (item["Theme"])
            print("========================================================找寻结束.....")
            '''

            item["ZuoZhe"] = each.xpath("./td[3]/a/text()").extract()
            #由哪个字幕组发布的

            item["HuiFu"] = each.xpath("./td[4]/font/text()").extract()
            #回复数

            item["LastPost"] = each.xpath("./td[5]/a/text()").extract()
            #最后发表人

            yield item
            #把数据交给管道文件

        # 设置新URL页码
        if (self.Page < 3):
            self.Page += 1
        # 把请求交给控制器
        time.sleep(3)
        yield scrapy.Request(self.url + str(self.Page), callback = self.parse)