from scrapy import Request
from scrapy.spiders import CrawlSpider
from douban.items import DoubanMovieItem
import os
import urllib


class DoubanMovieTop250Spider(CrawlSpider):
    name = 'douban_movie_top250'
    start_urls = {
        'https://movie.douban.com/top250'
        }

    def parse(self, response):
        imgs_path = 'pics'
        if not os.path.exists(imgs_path):
            os.makedirs(imgs_path)
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            movie_name = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['movie_name'] = movie_name
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            item['movie_url'] = movie.xpath(
                './/div[@class="pic"]/a/@href').extract()[0]

            movie_image_url = movie.xpath(
                './/div[@class="pic"]/a/img/@src').extract()[0]
            urllib.request.urlretrieve(movie_image_url, (imgs_path +'\\%s.jpg') % movie_name)
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url)
