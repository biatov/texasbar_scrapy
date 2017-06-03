# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetProfileItem(scrapy.Item):
    url_profile = scrapy.Field()


class GetDataItem(scrapy.Item):
    name = scrapy.Field()
    firm_name = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip = scrapy.Field()
    phone = scrapy.Field()
    practice_areas = scrapy.Field()
