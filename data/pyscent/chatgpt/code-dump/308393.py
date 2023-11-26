import scrapy
import hashlib
from bs4 import BeautifulSoup

class HuggingFaceSpider(scrapy.Spider):
    name = 'huggingface'
    allowed_domains = ['huggingface.co']
    start_urls = ['https://huggingface.co/docs/peft']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        page_content = soup.get_text()

        # Calculate the MD5 hash of the URL to use as the filename
        url_hash = hashlib.md5(response.url.encode('utf-8')).hexdigest()

        # Save the text content to a file
        with open(f"{url_hash}.txt", "w", encoding="utf-8") as file:
            file.write(page_content)

        # Follow all sublinks within the allowed domain
        for link in soup.find_all('a', href=True):
            sublink = response.urljoin(link['href'])
            if self.allowed_domains[0] in sublink:
                yield scrapy.Request(sublink, callback=self.parse)
