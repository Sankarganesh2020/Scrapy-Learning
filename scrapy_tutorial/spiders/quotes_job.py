# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyTutorialItem

class QuotesJobSpider(scrapy.Spider):
    name = 'quotes_job'

   # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        
        items = ScrapyTutorialItem()


        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('span small.author::text').get()
            tag = quote.css('div.tags a.tag::text').getall()

            items['text'] = text
            items['author'] = author
            items['tag'] = tag

            yield items

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)

"""            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse) """
