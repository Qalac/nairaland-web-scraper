import scrapy

class NairalandSpider(scrapy.Spider):

    name = 'nairaland_spider'
    start_urls = ['https://www.nairaland.com/']

    def parse(self, response):
        SET_SELECTOR = '.featured W'

        for element in response.css(SET_SELECTOR):
            HEADLINE_SELECTOR = 'a ::text'

            yield {
                'headline': element.css(HEADLINE_SELECTOR).extract_first()
            }
