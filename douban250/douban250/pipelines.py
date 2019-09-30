# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class Douban250Pipeline(object):
    def __init__(self):
        self.fp = open("douban.csv", "wb")
        self.exporter = CsvItemExporter(self.fp, fields_to_export=['movie_name',
                                                                   'movie_director_actors',
                                                                   'movie_time_country',
                                                                   'movie_grade',
                                                                   'comment_number',
                                                                   'movie_introduce',
                                                                   ])
        # self.exporter.start_exporting()

    def open_spider(self, spider):
        print("爬虫开始了")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self):
        # self.exporter.finish_exporting()
        self.fp.close()
