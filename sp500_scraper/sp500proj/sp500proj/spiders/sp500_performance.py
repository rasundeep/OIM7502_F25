import scrapy


class Sp500PerformanceSpider(scrapy.Spider):
    name = "sp500_performance"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        # Select only rows in the performance table
        rows = response.css("table.table tbody tr")

        for row in rows:
            rank = row.css("td:nth-child(1)::text").get()
            company = row.css("td:nth-child(2) a::text").get()
            # symbol is inside an <a>; fall back to plain text if needed
            symbol = row.css("td:nth-child(3) a::text, td:nth-child(3)::text").get()
            ytd_return = row.css("td:nth-child(4)::text").get()

            # Skip non-data rows (like "Companies", "Annual Returns", etc.)
            if not rank or not rank.strip().isdigit():
                continue

            # Clean text
            rank = rank.strip() if rank else None
            company = company.strip() if company else None
            symbol = symbol.strip() if symbol else None
            ytd_return = ytd_return.strip() if ytd_return else None

            yield {
                "rank": rank,
                "company": company,
                "symbol": symbol,
                "ytd_return": ytd_return
            }
