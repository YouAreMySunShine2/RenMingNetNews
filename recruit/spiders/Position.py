# -*- coding: utf-8 -*-
import scrapy
from recruit.items import PositionItem
 
class PositionSpider(scrapy.Spider):
    name = 'Position'
    allowed_domains = ['www.people.com.cn']
    start_urls = ["http://www.people.com.cn/"]
    def parse(self, response):
        position_lists = response.xpath('//div[@class="box fl ml35 news_center"]/ul/li')
        for position in position_lists:
            item = PositionItem()
            text_list = position.xpath('*/a/text()').extract()
            if len(text_list) == 0:
                text_list = position.xpath('./a/text()').extract()
            if len(text_list) > 0:
                item["position_title"] = text_list[0]
            link_list = position.xpath('*/a/@href').extract()
            if len(link_list) == 0:
                link_list = position.xpath('a/@href').extract()
            if len(link_list) > 0:
                item["position_link"] = link_list[0].strip('\n')
            #yield item
            if len(link_list) > 0:
                request = scrapy.Request(link_list[0].strip('\n').strip(), dont_filter=True, callback=self.next_parse)
                request.meta['item']=item
                yield request
    @staticmethod
    def next_parse(response):
       item_list = response.xpath('//*[@id="rwb_zw"]')
       for item in item_list:
           position_item = response.meta['item']
           position_item['context_list'] = item.xpath('./p').extract()
           yield position_item
       
       
      
            
            
