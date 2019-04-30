# -*- coding: utf-8 -*-
import scrapy
from recruit.items import PositionItem,NewContext
 
class PositionSpider(scrapy.Spider):
    name = 'Position'
    allowed_domains = ['www.people.com.cn']
    start_urls = ["http://www.people.com.cn/"]
    def parse(self, response):
        position_lists = response.xpath('//div[@class="box fl ml35 news_center"]')
        for postion in position_lists:
            position_title = position_lists.xpath('./ul[@class="list14 top"]/li/a/text()').extract()
            position_link = position_lists.xpath('./ul[@class="list14 top"]/li/a/@href').extract()
            index = 0;
            for link in position_link:
               item = PositionItem()
               item["position_title"] = position_title[index]
               index=index+1
               item["position_link"] = link
               yield item
               yield scrapy.Request(link, dont_filter=True, callback=self.next_parse)
    def next_parse(self, response):
       item_list = response.xpath('//*[@id="rwb_zw"]')
       for item in item_list:
           book = NewContext()
           book['content'] = item.xpath('./p').extract()
           yield book
       
       
      
            
            
