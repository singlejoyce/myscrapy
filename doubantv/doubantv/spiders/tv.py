# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider
from doubantv.items import DoubantvItem
import os
import urllib
import json


class TvSpider(CrawlSpider):
    name = 'tv'
    data = {
        'type': 'tv',  # movie-电影，tv-电视剧
        'tag': '韩剧',  # url编码 韩剧=%E9%9F%A9%E5%89%
        'sort': 'recommend',  # recommend-按热度排序，time-按时间排序，rank-按评价排序
        'page_limit': '20',
        'page_start': '0'
    }
    # 网页为动态js加载方式 获取对应的json文件
    start_urls = []
    for i in range(0, 10):
        temp = ''
        data['page_start'] = str(int(data['page_limit']) * i)
        for key, value in data.items():
            temp = temp + str(key) + '=' + str(value) + '&'
        url = 'https://movie.douban.com/j/search_subjects?' + temp
        start_urls.append(url)
    print(start_urls)

    def parse(self, response):
        imgs_path = 'cover'
        if not os.path.exists(imgs_path):
            os.makedirs(imgs_path)
        resultjson = json.loads(response.body)
        results = resultjson['subjects']
        item = DoubantvItem()
        for result in results:
            if result:
                item['title'] = result['title']
                item['url'] = result['url']
                item['rate'] = result['rate']
                urllib.request.urlretrieve(result['cover'], (imgs_path + '\\%s.jpg') % item['title'])
                # //*[@id="comments-section"]/div[@class="mod-hd"]/h2/span/a/@herf
                # //*[@id="comments-section"]/div[@class="mod-hd"]/h2/span/a/text()
            else:
                print("error!!!can not find !!!")

            yield item


