# -*- coding: utf-8 -*-
import scrapy

from wikipedia.items import CountryRegionItem
from wikipedia.items import CountryProvinciaItem

class CountryItRegions(scrapy.Spider):
    name = "country_it_province"
    start_urls = [
        'https://en.wikipedia.org/wiki/ISO_3166-2:IT'
    ]
        
    def parse(self, response):
        for row in response.xpath('//table[@class="wikitable sortable"][2]//tr'):
            try:
                item = CountryProvinciaItem()
                item['iso'] = row.xpath('td[1]//span/text()').extract()
                item['provincia'] = row.xpath('td[2]//a/text()')[0].extract()
                item['region'] = xpath('td[3]//span/text()').extract()
                yield item
            except:
                continue

        
  
