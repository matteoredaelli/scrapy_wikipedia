# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AggettivoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

    
class CountryCapitalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    capital = scrapy.Field()
    #flag_url = scrapy.Field()

class CountryIsoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    iso = scrapy.Field()

class CountryRegionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    iso = scrapy.Field()
    region = scrapy.Field()

class CountryProvinciaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    iso = scrapy.Field()
    region = scrapy.Field()
    provincia = scrapy.Field()
