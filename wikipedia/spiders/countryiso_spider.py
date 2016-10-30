# -*- coding: utf-8 -*-
import scrapy

from wikipedia.items import CountryIsoItem

class CountryisoSpider(scrapy.Spider):
    name = "countryiso"
    start_urls = [
        'https://en.wikipedia.org/wiki/ISO_3166-1'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@class="wikitable sortable"]//tr'):
            try:
                item = CountryIsoItem()
                item['country'] = row.xpath('td/a/text()')[0].extract()
                item['iso'] = row.xpath('td//a')[1].xpath('span/text()').extract()
                yield item
            except:
                continue
