import scrapy
from ..items import GetDataItem
from scrapy.spiders import CrawlSpider
import json


class GetDataSpider(scrapy.Spider):
    name = "need_data"

    allowed_domains = ["www.texasbar.com"]

    try:
        with open('profiles.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = dict()

    start_urls = list(map(lambda x: x['url_profile'], data))

    def parse(self, response):
        item = GetDataItem()
        for each in response.selector.xpath('div[@class="vcard avatar-column"] h3'):
            item['name'] = each.xpath('.//span[@class="given-name"]/text()').extract()
        return item
