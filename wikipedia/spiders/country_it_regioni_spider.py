# -*- coding: utf-8 -*-
import scrapy

from wikipedia.items import CountryRegionItem

class CountryItRegions(scrapy.Spider):
    name = "country_it_regioni"
    start_urls = [
        'https://en.wikipedia.org/wiki/ISO_3166-2:IT'
    ]
        
    def parse(self, response):
        for row in response.xpath('//table[@class="wikitable sortable"][1]//tr'):
            try:
                item = CountryRegionItem()
                item['iso'] = row.xpath('td[1]/span/text()')[0].extract()
                item['region'] = row.xpath('td[2]//a/text()')[0].extract()
                yield item
            except:
                continue

        
  
