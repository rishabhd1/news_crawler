import scrapy

from ..items import NewspaperItem


class TimesofindiaSpider(scrapy.Spider):
    name = 'timesofindia'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/home/headlines']
    custom_settings = {
        'CONCURRENT_REQUESTS': 1
    }

    def parse(self, response):
        businessHeadlines = response.xpath(
            '//*[@id="c_headlines_wdt_2"]/div[1]/ul/li')
        for businessHeadline in businessHeadlines:
            item = NewspaperItem()

            item['host'] = 'timesofindia'
            item['category'] = 'business'
            item['headline'] = businessHeadline.xpath(
                './span[@class="w_tle"]/a/text()').extract_first()
            item['url'] = "https://timesofindia.indiatimes.com" + \
                businessHeadline.xpath(
                    './span[@class="w_tle"]/a/@href').extract_first()
            # //*[@id="c_headlines_wdt_2"]/div[1]/ul/li[1]/span[2]/span
            item['date'] = businessHeadline.xpath(
                './span[@class="w_bylinec"]/span[@class="strlastupd"]/@rodate'
            ).extract_first()

            yield item
