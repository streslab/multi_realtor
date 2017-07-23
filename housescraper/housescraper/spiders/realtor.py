# -*- coding: utf-8 -*-
import scrapy
from ..items import HousescraperItem


class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    allowed_domains = ['realtor.com']
    start_urls = ['http://realtor.com/']

    def parse(self, response):
        # TODO
        return HousescraperItem(name='multifamily')
