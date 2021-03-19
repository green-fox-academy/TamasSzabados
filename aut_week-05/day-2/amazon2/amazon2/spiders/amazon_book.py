import scrapy


class AmazonBookSpider(scrapy.Spider):
    name = 'amazon_book'
    
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656020011&dc&qid=1615980518&rnid=618072011&ref=lp_1000_nr_p_n_feature_browse-bin_1']

    def parse(self, response):
        print("procesing:"+response.url)
        products = response.xpath("//div[@class='s-main-slot s-result-list']")
        
        print(product)                        
      
        for product in products:
            
            rating = product.xpath("//a[@class='a-link-normal']/span[@class='a-size-base' and 1]/text()").get()
            if rating is None:
                rating = "not available"
            
            yield {
                "product": product.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").get(),
                "price": product.xpath("//span[@class='a-price-whole']/text()").get(),
                "ratings": rating
                }
            

        next_path = response.xpath("//li[@class='a-last']/a[1]/@href").get()
        if next_path:
            yield scrapy.Request(response.urljoin(next_path), callback=self.parse)
           