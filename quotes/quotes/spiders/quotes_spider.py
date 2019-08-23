import scrapy


# inheriting from class scrapy.Spider
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # list of websites we want to scrap
    start_urls = ['http://quotes.toscrape.com/']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        title = response.css('title::text').extract()

        # yield = return
        # yield works with generator
        yield {'title': title}

