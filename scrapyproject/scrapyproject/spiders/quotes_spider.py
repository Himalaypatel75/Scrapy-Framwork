import scrapy
from ..items import ScrapyprojectItem

class QuoteSprider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://quotes.toscrape.com/"]

    # def parse(self, response):
    #     title = response.css("title::text").extract()
    #     description = response.css("span.text::text").extract_first() #or we can do [2].extract()
    #     yield {'titletext' : title, "description" : description}

    def parse(self, response):

        items = ScrapyprojectItem()

        all_div_quotes = response.css("div.quote")
        for div_quotes in all_div_quotes:
            description = div_quotes.css("span.text::text").extract() #or we can do [2].extract()
            title = div_quotes.css(".author::text").extract()
            author = div_quotes.css(".tag::text").extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = description

            yield items



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