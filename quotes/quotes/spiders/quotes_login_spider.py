import scrapy
from scrapy.http import FormRequest
from ..items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes_login'

    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css("form input::attr(value)").extract_first()
        print('CSRF_TOKEN: ', token)
        return FormRequest.from_response(response, formdata={
            'csrf_roken': token,
            'username': '6psdsdsd',
            'password': 'password'
        }, callback=self.start_scrapping)

    def start_scrapping(self, response):
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