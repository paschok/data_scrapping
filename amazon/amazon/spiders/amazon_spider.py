# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/s/browse?_encoding=UTF8&node=16225007011&ref_=nav_shopall-export_nav_mw_sbd_intl_computers'
    ]

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css(".s-access-title::text").extract()
        product_author = response.css(".a-color-secondary::text").extract()
        product_price = response.css(".sx-price-whole::text").extract()
        product_image_link = response.css(".cfMarker::attr(src)").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link

        yield items