# -*- coding: utf-8 -*-
#定义我们需要获取的字段
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    定义我要提取内容的字段名字
    '''
    # 职位名
    positionname = scrapy.Field()
    # 详细链接
    positionLink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 招聘人数
    peopleNum = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
