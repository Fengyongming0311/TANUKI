# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunshineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    定义我要提取内容的字段名字
    '''
    Theme = scrapy.Field()
    #爬取的主题名字
    ZuoZhe = scrapy.Field()
    #由哪个作者发布的
    HuiFu = scrapy.Field()
    #回复数
    LastPost = scrapy.Field()
    #最后发表人
