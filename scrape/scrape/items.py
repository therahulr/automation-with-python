import scrapy
from scrapy.item import Item, Field


class ScrapeItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()

