import scrapy


class AmazonBookSpider(scrapy.Spider):
    name = 'amazon_book'
    
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_feature_browse-bin%3A2656020011&dc&qid=1615980518&rnid=618072011&ref=lp_1000_nr_p_n_feature_browse-bin_1']

    def parse(self, response):
        print("procesing:"+response.url)
        product = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").getall()
        price = response.xpath("//span[@class='a-price-whole']/text()").getall()
        ratings = response.xpath("//a[@class='a-link-normal']/span[@class='a-size-base' and 1]/text()").getall()
             
        print(product)                        
      
        for i in range(len(product)-1):
            try:
                yield {
                    "product": product[i],
                    "price": price[i],
                    "ratings": ratings[i]
                }
            except Exception:
                print("error occurred")
            

        next_path = response.xpath("//li[@class='a-last']/a[1]/@href").get()
        if next_path:
            yield scrapy.Request(response.urljoin(next_path), callback=self.parse)
           