# -*- coding: utf-8 -*-
import scrapy

from wikipedia.items import CountryCapitalItem

class CountryCapitalSpider(scrapy.Spider):
    name = "countrycapital"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order'
    ]

    def parse(self, response):
        for row in response.xpath('//table[@class="wikitable sortable"]//tr'):
            try:
                item = CountryCapitalItem()
                item['country'] = row.xpath('td//a/text()')[0].extract()
                item['capital'] = row.xpath('td//a/text()')[1].extract()
                ##item['flag_url'] = row.xpath('td//img/@src')[0].extract()
                yield item
            except:
                continue
