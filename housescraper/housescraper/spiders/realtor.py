# -*- coding: utf-8 -*-
import scrapy
from ..items import HousescraperItem


class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    allowed_domains = ['realtor.com']
    start_urls = ['http://realtor.com/realestateandhomes-search/Madison-WI/type-multi-family-home']

    def parse(self, response):
        city = response.xpath()
        state = response.xpath()
        address = response.xpath()
        beds = response.xpath()
        baths = response.xpath()
        sqft = response.xpath()
        price = response.xpath()
        url = response.xpath()
        return HousescraperItem(city = city, state = state, address = address, beds = beds, baths = baths, sqft = sqft, price = price, url = url)
