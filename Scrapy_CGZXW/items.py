# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

""" 对应SQL Server CunZiLiDB 中 Article 的字段结构 """
class ScrapyCgzxwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    content = scrapy.Field()
    dealedContent = scrapy.Field()
    newsType = scrapy.Field()
    newsFrom = scrapy.Field()
    clickCount = scrapy.Field()
    addDate = scrapy.Field()
    updateDate = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()

    pass































































































