import scrapy
import re
from datetime import datetime

from ..items import NewspaperItem


class NdtvSpider(scrapy.Spider):
    name = 'ndtv'
    allowed_domains = ['ndtv.com']
    start_urls = ['https://www.ndtv.com/business', 'https://sports.ndtv.com/',
                  'https://movies.ndtv.com/topic/entertainment']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    def parse(self, response):
        businessHeadlines = response.xpath(
            '/html/body/div[5]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div/ul/li')
        for headline in businessHeadlines:
            item = NewspaperItem()

            item['createdAt'] = datetime.now()
            item['clickCount'] = 0
            item['archived'] = False
            item['host'] = 'ndtv'
            item['category'] = 'business'

            headlineString = headline.xpath(
                './p/a/text()').extract_first()
            if headline:
                item['headline'] = headlineString.replace("\\\"", "\"")
            item['url'] = headline.xpath('./div/a/@href').extract_first()
            image = headline.xpath('./div/a/img/@src').extract_first()
            if image:
                item['image'] = re.sub(r'\?.+', '', image)
            item['date'] = ''

            yield item

        sportsHeadlines = response.xpath(
            '//*[@id="container"]/div[3]/div/div[1]/div/div[1]/div[1]/div/div/div')
        for headline in sportsHeadlines:
            item = NewspaperItem()

            item['createdAt'] = datetime.now()
            item['clickCount'] = 0
            item['archived'] = False
            item['host'] = 'ndtv'
            item['category'] = 'sports'

            item['headline'] = headline.xpath(
                './div/div[2]/div/h3/a/text()').extract_first()
            item['url'] = headline.xpath(
                './div/div[1]/a/@href').extract_first()
            image = headline.xpath('./div/div[1]/a/img/@src').extract_first()
            if image:
                item['image'] = re.sub(r'\?.+', '', image)
            item['date'] = ''

            yield item

        entertainmentHeadlines = response.xpath(
            '/html/body/div[1]/div[1]/div[1]/div/div/div[5]/div[1]/ul/li')
        for headline in entertainmentHeadlines:
            item = NewspaperItem()

            item['createdAt'] = datetime.now()
            item['clickCount'] = 0
            item['archived'] = False
            item['host'] = 'ndtv'
            item['category'] = 'entertainment'

            item['headline'] = headline.xpath(
                './div[2]/h4/a/text()').extract_first()
            item['url'] = headline.xpath('./div[1]/a/@href').extract_first()
            item['image'] = headline.xpath(
                './div[1]/a/img/@src').extract_first()
            item['date'] = ''

            yield item
