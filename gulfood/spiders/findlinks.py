"""
This spider was written to profile urls of the companies exhibiting in Gulfood 2023.
Author: Muhammad Owais
Date: 02-01-2023
"""

import scrapy


class findlinks(scrapy.Spider):
    name = "findlinks"
    pages = 166
    start_urls = []

    for i in range(pages):
        start_urls.append("https://www.gulfood.com/exhibitors?page="+str(i))

    def parse(self, response, **kwargs):
        urls = response.css(
            """body > div.site > div.content > main > div.content__main__body >
            div > div > div > div > ul.m-exhibitors-list__items.js-library-list >
            li > h2 > a::attr(href)""").getall()
        
        for url in urls:
            suffix = url.split("'")[1]
            prefix = "https://www.gulfood.com/"
            item = prefix + suffix
            yield {"urls" : item}