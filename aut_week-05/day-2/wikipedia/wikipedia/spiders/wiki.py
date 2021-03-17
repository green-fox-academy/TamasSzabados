import scrapy
import random


class WikiSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    
    start_urls = ['https://en.wikipedia.org/wiki/Albert_Einstein']

    def parse(self, response):
        print("procesing:"+response.url)
        
        name = response.xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[1]/th/div/text()").get()
        birth = response.xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[contains(.,'Born')]/td/text()").get()
                          
        if name is not None and birth is not None:
            yield {
                "name": name,
                "birth": birth
                }
        else:
            next_path = response.xpath("//a/@href").getall()[random.randint(6,10)]
            yield scrapy.Request(response.urljoin(next_path), callback=self.parse)

        next_path = response.xpath("//a[contains(@href,'wiki')]/@href").getall()[random.randint(6,10)]
        print(next_path)
        if next_path:
            yield scrapy.Request(response.urljoin(next_path), callback=self.parse)