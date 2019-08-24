import scrapy
from ..items import QuotesItem


# inheriting from class scrapy.Spider
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # list of websites we want to scrap
    start_urls = ['http://quotes.toscrape.com/']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        # an instance variable
        items = QuotesItem()

        all_div_quotes = response.css("div.quote")

        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            # yield = return
            # yield works with generator
            yield items

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # callback tells Scrapy what to do next
            yield response.follow(next_page, callback=self.parse)