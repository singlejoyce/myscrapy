# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from images.items import ImagesItem
from scrapy.selector import Selector
import json


class Download(CrawlSpider):
    name = "image"
    # start_urls = ["https://stocksnap.io/", ]

    # 百度图片搜索是动态js网页加载，需要获取加载的json文件
    # json地址:https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&
    #       ct=201326592&is=&fp=result&queryWord=%E6%B8%A9%E6%9A%96%E7%B3%BB&
    #       cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&
    #       word=%E6%B8%A9%E6%9A%96%E7%B3%BB&s=&se=&tab=&width=&height=&face=0&istype=2&
    #       qc=&nc=1&fr=&pn=0&rn=30&gsm=1e&1519900121322=
    # 根据对应的json文件的结构，我们可以用json.loads函数进一步提取想要的数据：
    page = 0
    data = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '%E6%B8%A9%E6%9A%96%E7%B3%BB',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'st': '-1',
        'adpicid': '',
        'z': '',
        'ic': '0',
        'word': '%E6%B8%A9%E6%9A%96%E7%B3%BB',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'pn': '0',
        'rn': '30',
        'gsm': '1e',
        '1519900121322': '',
    }

    start_urls = []
    for i in range(0, 10):
        data['pn'] = str(int(data['rn']) * i)
        temp = ''
        for key, value in data.items():
            temp = temp + str(key) + '=' + str(value) + '&'
        url = 'https://image.baidu.com/search/acjson?' + temp
        start_urls.append(url)
    print(start_urls)

    def parse(self, response):
        # hxs = Selector(response)
        # imgs = hxs.xpath('//*[@id="main"]/a/img/@src').extract()
        resultJson = json.loads(response.body)
        results = resultJson['data']
        imgs = []
        for result in results:
            if result:
                url = result['thumbURL']
                imgs.append(url)
            else:
                print("error!!!can not find imgurl!!!")

        item = ImagesItem()
        item['image_urls'] = imgs
        return item
