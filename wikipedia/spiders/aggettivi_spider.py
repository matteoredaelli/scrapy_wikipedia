# -*- coding: utf-8 -*-
import scrapy
##from scrapy.contrib.spiders import Rule
##from scrapy.linkextractors import LinkExtractor
##from lxml import html

from wikipedia.items import AggettivoItem

class AggettiviSpider(scrapy.Spider):
    name = "aggettivi"
    start_urls = [
        'https://en.wiktionary.org/wiki/Category:Italian_adjectives'
    ]

    ## rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@title="Category:Italian adjectives"]',)), callback="parse", follow= True),)
            
    def parse(self, response):
        pages = response.xpath('//a[@title="Category:Italian adjectives"]')
        for pg in pages:
            if pg.xpath('text()').extract_first() == 'next page':
                next_page = pg.xpath('@href').extract_first()
                if next_page is not None:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse, dont_filter = False)
        for row in response.xpath('//div[@class="mw-category-group"]//ul/li/a'):
            try:
                item = AggettivoItem()
                item['name'] = row.css('a').xpath('text()').extract()
                yield item
            except:
                continue


