# -*- coding: utf-8 -*-
import scrapy
from douban250.items import Douban250Item


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        li_list = response.xpath('//ol[@class="grid_view"]/li')
        for li in li_list:
            movie_name = li.xpath('.//a/span[1]/text()').get()
            # print(movie_name)
            movie_director_actors = li.xpath('.//div[@class="bd"]/p/text()').getall()[0]
            movie_director_actors = movie_director_actors.replace(' ', '').replace('\n', '')
            movie_time_country = li.xpath('.//div[@class="bd"]/p/text()').getall()[1]
            movie_time_country = movie_time_country.replace(' ', '').replace('\xa0', '').replace('\n', '')
            # print(movie_director_actors)
            # print(movie_time_country)
            movie_grade = li.xpath('.//div/span[@class="rating_num"]/text()').get()
            # print(movie_grade)
            comment_number = li.xpath('.//div[@class="star"]/span[4]/text()').get()
            comment_number = comment_number[:-3]
            # print(comment_number)
            movie_introduce = li.xpath('.//p[@class="quote"]/span/text()').get()
            # print(movie_introduce)
            item = Douban250Item(movie_name=movie_name,
                                 movie_director_actors=movie_director_actors,
                                 movie_time_country=movie_time_country,
                                 movie_grade=movie_grade,
                                 comment_number=comment_number,
                                 movie_introduce=movie_introduce)
            yield item
        next_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').get()
        if not next_url:
            return
        else:
            next_url = "https://movie.douban.com/top250" + next_url
            yield scrapy.Request(next_url, callback=self.parse)

