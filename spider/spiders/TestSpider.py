# !/usr/bin/python
# coding: utf-8

import scrapy
import re
from scrapy import log
from scrapy import Selector


class PlayStoreSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/details?id=com.tencent.mm"]

    def parse(self, response):

        APP_NAME = '//h1[@class="document-title"]/div/text()'
        print len(response.xpath(APP_NAME).extract())