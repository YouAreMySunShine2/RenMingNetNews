# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
 
 
class PositionItem(scrapy.Item):
    # 新闻标题
    position_title = scrapy.Field()
    # 新闻URL
    position_link = scrapy.Field()
    # 新闻内容
    context_list = scrapy.Field()
class NewContext(scrapy.Item):
    content = scrapy.Field()
