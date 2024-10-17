import scrapy


class QuoteSprider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        title = response.css("title::text").extract()
        description = response.css("span.text::text").extract_first() #or we can do [2].extract()
        yield {'titletext' : title, "description" : description}




"""
import scrapy


class QuoteSprider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        title = response.css("title::text").extract()
        description = response.css("span.text::text").extract_first() #or we can do [2].extract()
        yield {'titletext' : title, "description" : description}
"""