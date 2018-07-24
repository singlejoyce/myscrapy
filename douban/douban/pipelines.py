# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


class DoubanPipeline(CsvItemExporter):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        print('==========pipeline==========from_crawler==========')
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        savefile = open('douban_movie_top250.csv', 'wb+')
        self.files[spider] = savefile
        print('==========pipeline==========spider_opened==========')
        self.exporter = CsvItemExporter(savefile)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        print('==========pipeline==========spider_closed==========')
        self.exporter.finish_exporting()
        savefile = self.files.pop(spider)
        savefile.close()

    def process_item(self, item, spider):
        print('==========pipeline==========process_item==========')
        print(type(item))
        self.exporter.export_item(item)
        return item
