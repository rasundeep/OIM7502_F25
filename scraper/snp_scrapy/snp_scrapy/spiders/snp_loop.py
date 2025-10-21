import Myscrapy
from snp_scrapy.items import SnpScraperItem

class SnpLoopSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"]

    def parse(self, response):
        stock = SnpScraperItem()
        rows = response.xpath('//*table[@id="constituents"]/tbody/tr')
        for row in rows:
        stock['symbol'] = rows[0].xpath('.//td[1]/text()').get()
       stock['name'] = rows[0].xpath('.//td[1]/text()').get()
       stock['symbol'] = rows[0].xpath('.//td[1]/text()').get()
       stock['symbol'] = rows[0].xpath('.//td[1]/text()').get()
       stock['symbol'] = rows[0].xpath('.//td[1]/text()').get()