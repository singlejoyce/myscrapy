# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名称
    title = scrapy.Field()
    # 评分
    rate = scrapy.Field()
    # 网址
    url = scrapy.Field()

