import scrapy

class SteamSpider(scrapy.Spider):
    name = 'steamspider'
    start_urls = ["https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/",]

    def parse(self, response):
        title = response.xpath("//*[@class='apphub_AppName']/text()").extract_first().strip()
        tag_name = [item.strip() for item in response.xpath('//*[contains(@class,"popular_tags")]/*[@class="app_tag"]/text()').extract()]
        yield {"title":title,"tagname":tag_name}
