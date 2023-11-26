import scrapy
import hashlib
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('div.quote')

        text_content = ""

        for quote in quotes:
            text = quote.select_one('span.text').get_text()
            author = quote.select_one('span small.author').get_text()
            text_content += f"{text} - {author}\n"

        # Calculate the MD5 hash of the URL to use as the filename
        url_hash = hashlib.md5(response.url.encode('utf-8')).hexdigest()

        # Save the text content to a file
        with open(f"{url_hash}.txt", "w", encoding="utf-8") as file:
            file.write(text_content)

        # Follow the next page link
        next_page = soup.select_one('li.next a')
        if next_page:
            next_page_url = next_page['href']
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
