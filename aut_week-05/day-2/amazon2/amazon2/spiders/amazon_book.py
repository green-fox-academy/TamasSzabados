import scrapy


class AmazonBookSpider(scrapy.Spider):
    name = 'amazon_book'
    allowed_domains = ['https://www.amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656020011&dc&qid=1615980518&rnid=618072011&ref=lp_1000_nr_p_n_feature_browse-bin_1']

    def parse(self, response):
        print("procesing:"+response.url)
        product = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span/text()").getall()
        price = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/span[2]/a/span/text()").extract()   
        ratings = response.xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[2]/div/div/span/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/a/span[1]/span[1]/text()").extract()

        print(product)                        
        print(price )
        print(ratings)
        print(len(product))
        print(len(price))
        print(len(ratings))

        next_path = response.xpath("//a[@class = 'a-last']/@href").extract_first()
        if next_path is not None:
            yield scrapy.Request(response.urljoin(next_path), callback=self.parse)

        for i in range(len(product)):
            yield {
                "product": product[i],
                "price": price[i],
                "ratings": ratings[i]
                    }
           