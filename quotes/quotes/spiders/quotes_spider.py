import scrapy


# inheriting from class scrapy.Spider
class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # list of websites we want to scrap
    start_urls = ['http://quotes.toscrape.com/']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        all_div_quotes = response.css("div.quote")
        title = all_div_quotes.css("span.text::text").extract()
        author = all_div_quotes.css(".author::text").extract()
        tag = all_div_quotes.css(".tag::text").extract()

        # yield = return
        # yield works with generator
        yield {
            'title': title,
            'author': author,
            'tag': tag
        }

