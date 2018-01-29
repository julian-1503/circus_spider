import scrapy


class OddItem(scrapy.Item):
    odd_value = scrapy.Field()
    recording_time = scrapy.Field()


class OutcomeItem(scrapy.Item):
    outcome_name = scrapy.Field()


class MatchItem(scrapy.Item):
    event_name = scrapy.Field()
