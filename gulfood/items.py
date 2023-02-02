# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GulfoodItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    stand = scrapy.Field()
    address = scrapy.Field()
    website = scrapy.Field()
    facebook = scrapy.Field()
    instagram = scrapy.Field()
    youtube = scrapy.Field()
    linkedin = scrapy.Field()
    twitter = scrapy.Field()
    description = scrapy.Field()