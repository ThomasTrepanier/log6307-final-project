import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('div.quote')

        for quote in quotes:
            text = quote.select_one('span.text').get_text()
            author = quote.select_one('span small.author').get_text()
            yield {
                'text': text,
                'author': author,
            }

        next_page = soup.select_one('li.next a')
        if next_page:
            next_page_url = next_page['href']
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
