import scrapy
from scrapy_splash import SplashRequest

from datetime import datetime

from circus.items import OddItem, MatchItem

class OutcomeOddsSpider(scrapy.Spider):
    name = 'outcome_odds'
    home_url = 'https://www.circus.be/en/sport/sports-bets/844/227875758'
    event_url = 'https://www.circus.be/en/sport/event/844/65587/227875758/{}'
    splash_args = { 'wait': 25 }

    def start_requests(self):
        yield SplashRequest(
            url=self.home_url,
            callback=self.parse,
            args=self.splash_args
        )


    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        for next_page in response.xpath("//div[starts-with(@id,'EventId_')]/@id").extract():
            event_id = next_page.replace('EventId_', '')

            yield SplashRequest(
                url=self.event_url.format(event_id),
                callback=self.parse_match,
                args=self.splash_args
            )



    def parse_match(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        match_name = response.xpath("//div[contains(@class,'event__name')]"
                                    "/span/text()").extract_first()

        match_date = response.xpath("//span[contains(@class,'event__date')]"
                                    "/text()").extract_first()

        if match_date is not None:
            match_date = datetime.strptime(match_date, '%d/%m/%Y - %H:%M')

        if match_name is not None:
            yield MatchItem(match_name=match_name, match_date=match_date)
