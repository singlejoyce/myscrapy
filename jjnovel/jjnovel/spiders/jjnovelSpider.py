# coding=utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jjnovel.items import JjnovelItem
import urllib


class Jjnovel(CrawlSpider):
    name = 'jjnovel'
    start_urls = ['http://www.jjwxc.net/topten.php?orderstr=16']  # 完结金榜

    def parse(self, response):
        item = JjnovelItem()
        selector = Selector(response)
        articles = selector.xpath('//div[@class="wrapper box_06"]')

        for article in articles:
            sort = article.xpath('h5/text()').extract()
            item['sort'] = sort
            novel_info = article.xpath('ul[@class="list_01"]/li')
            for j in novel_info:
                novel_author = j.xpath('a/span/text()').extract()
                novel_title = j.xpath('a[@target="_blank"]/text()').extract()
                novel_url = j.xpath('a[@target="_blank"]/@href').extract()

                item['title'] = novel_title
                item['url'] = 'http://www.jjwxc.net/' + novel_url[0]
                item['author'] = novel_author
                yield item
