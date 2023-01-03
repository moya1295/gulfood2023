"""
This spider is written extract relavent company data from each url.
There are a total of 2125 companies right now. starturls are obtained from a csv file.
Author: Muhammad Owais
Data: 02-01-2022
"""

import scrapy
import csv
import re

class company_data(scrapy.Spider):
    name = "companydata"
    filename = "urls.csv"
    start_urls = []

    with open(filename,"r") as f:
        for row in f:
            start_urls.append(row)
    

    def parse(self, response, **kwargs):
        
        final_data = {}

        company_name = response.css("div.m-exhibitor-entry__item__header__wrapper h1::text").get()
        company_name = re.sub(r'[\r\n\t]','',company_name)

        stand_position = response.css("div.m-exhibitor-entry__item__header__wrapper div::text").get()
        stand_position = re.sub(r'[\r\n\t]','',stand_position)

        company_desc = response.css("div.m-exhibitor-entry__item__body__description__profile::text").get()
        company_desc = re.sub(r'[\r\n\t]','',company_desc)

        company_address = response.css("div.m-exhibitor-entry__item__body__contacts__address::text").getall()
        final_address = []
        for x in company_address:
            x = re.sub(r'[\r\n\t]','',x)
            if x != "":
                final_address.append(x)
        
        company_website = response.css("div.m-exhibitor-entry__item__body__contacts__additional__website a").attrib['href']

        yield {
            "Name" : company_name,
            "Stand" : stand_position,
            "Description" : company_desc,
            "Address" : final_address,
            "Website" : company_website
        }



