# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst


class PlaystoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AppItem(scrapy.Item):

    APP_NAME = "//div[@class='info-box-top']/h1[@class='document-title']/div/text()"
    # "//div[@class='info-container']/div[@class='document-title']/div/text()"

    APP_CATEGORY = "//div/a[@class='document-subtitle category']/span/text()"
    APP_VERSION = "//div[@class='content' and @itemprop='softwareVersion']/text()"
    APP_DESCRIPTION = "//div[@class='show-more-content text-body' and @itemprop='description']//text()"
    APP_PUBLISH_DATE = "//div[@class='meta-info']/div[@itemprop='datePublished']/text()"
    APP_IMPROVEMENT = "//div[@class='details-section-contents show-more-container']/div[@class='recent-change']/text()"
    APP_SCORE_VALUE = "//div[@class='rating-box']/div[@class='score-container']/meta[@itemprop='ratingValue']/@content"
    APP_INSTALLS = "//div[@class='content' and @itemprop='numDownloads']/text()"

    market = scrapy.Field()
    name = scrapy.Field()
    app_id = scrapy.Field()
    category = scrapy.Field()
    version = scrapy.Field()
    description = scrapy.Field()
    improvement = scrapy.Field()
    url = scrapy.Field()
    update_date = scrapy.Field()
    score = scrapy.Field()
    download_count = scrapy.Field()


class AppItemLoader(ItemLoader):
    default_output_processor = Compose(TakeFirst(), lambda value: value.strip())

    # override
    def load_item(self):
        for field_name, attr in self.item.fields.items():
            xpath = attr.get('xpath')
            css = attr.get('css')
            callback = attr.get('callback')

            if xpath:
                self.add_xpath(field_name, xpath)

            elif css:
                self.add_css(field_name, css)

            elif callback:
                self.add_value(field_name, callback(self.context.get('response')))

        return super(AppItemLoader, self).load_item()
