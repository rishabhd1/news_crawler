import scrapy
from ..items import NewspaperItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item = NewspaperItem()

            item['text'] = quote.xpath(
                    './span[@class="text"]/text()').extract_first(),
            item['author'] = quote.xpath(
                    './/small[@class="author"]/text()').extract_first(),
            item['tags'] = quote.xpath(
                    './/div[@class="tags"]/a[@class="tag"]/text()').extract()

            yield item
