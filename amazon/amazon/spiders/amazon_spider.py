# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
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

        next_page = 'https://www.amazon.com/s?rh=n%3A16225007011&page=2&qid=1566690295&ref=lp_16225007011_pg_' + str(AmazonSpiderSpider.page_number) + ''
        if AmazonSpiderSpider.page_number < 10:
            AmazonSpiderSpider.page_number += 1
            print('AmazonSpiderSpider.page_number: ', AmazonSpiderSpider.page_number)
            yield response.follow(next_page, callback=self.parse)