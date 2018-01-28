import scrapy
from scrapy_splash import SplashRequest

from circus.items import OddItem, OutcomeItem, EentItem

class OutcomeOddsSpider(scrapy.Spider):
    name = 'outcome_odds'

    def start_requests(self):
        yield SplashRequest(
            url='https://www.circus.be/en/sport/sports-bets/844/227875758',
            callback=self.parse,
            args={
                'wait': 20
            }
        )

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # for response.xpath(
            # "//div[contains(@class,'OutcomeOdd')]/div[1]/span/text()"
        # )
        yield {
            'title': title
        }
