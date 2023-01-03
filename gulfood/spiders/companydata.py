"""
This spider is written extract relavent company data from each url.
There are a total of 2125 companies right now. starturls are obtained from a csv file.
Author: Muhammad Owais
Data: 02-01-2022
"""

import scrapy
import csv
import re
import logging
from scrapy.utils.log import configure_logging

class company_data(scrapy.Spider):
    name = "companydata"
    filename = "urls.csv"
    start_urls = []

    configure_logging(install_root_handler=False)
    logging.basicConfig(filename="log.txt", format='%(levelname)s: %(message)s', level=logging.INFO)

    
    with open(filename,"r") as f:
        for row in f:
            start_urls.append(row)
    

    def parse(self, response, **kwargs):
        

        company_name = response.css("div.m-exhibitor-entry__item__header__wrapper h1::text").get()
        if company_name != None:
            company_name = re.sub(r'[\r\n\t]','',company_name)

        stand_position = response.css("div.m-exhibitor-entry__item__header__wrapper div::text").get()
        if company_name != None:
            stand_position = re.sub(r'[\r\n\t]','',stand_position)

        company_desc = response.css("div.m-exhibitor-entry__item__body__description__profile::text").get()
        if company_desc != None:
            company_desc = re.sub(r'[\r\n\t]','',company_desc)

        company_address = response.css("div.m-exhibitor-entry__item__body__contacts__address::text").getall()
        final_address = []
        for x in company_address:
            x = re.sub(r'[\r\n\t]','',x)
            if x != "":
                final_address.append(x)
        
        company_website = response.css("div.m-exhibitor-entry__item__body__contacts__additional__website a::attr(href)").get()

        company_socials = response.css("ul.m-exhibitor-entry__item__body__contacts__social a::attr(href)").getall()

        instagram = None
        youtube = None
        facebook = None
        linkedin = None
        twitter = None

        for url in company_socials:
            if re.search("instagram",url) != None:
                instagram = url
            elif re.search("youtube", url) != None:
                youtube = url
            elif re.search("facebook", url) != None:
                facebook = url
            elif re.search("linkedin",url) != None:
                linkedin = url
            elif re.search("twitter",url) != None:
                twitter = url

        yield {
            "Name" : company_name,
            "Stand" : stand_position,
            "Address" : final_address,
            "Website" : company_website,
            "Facebook" : facebook,
            "Instagram" : instagram,
            "Youtube" : youtube,
            "LinkedIn": linkedin,
            "Twitter" : twitter,
            "Description": company_desc
        }



