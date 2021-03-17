import scrapy


class AmazonKindleSpider(scrapy.Spider):
    name = 'amazon_kindle'
    allowed_domains = ['https://www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=kindle']

    def parse(self, response):
        print("procesing:"+response.url)
        product = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span/text()").getall()                    
        price = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/a/span[1]/span[1]/text()").extract()   
        ratings = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/span[2]/a/span/text()").extract()

        print(product)                        
        print(price )
        print(ratings)
        print(len(product))
        print(len(price))
        print(len(ratings))

        for i in range(len(product)):
            try:
                yield {
                    "product": product[i],
                    "price": price[i],
                    "ratings": ratings[i]
                    }
            except IndexError:
                print(error, "error occurred")