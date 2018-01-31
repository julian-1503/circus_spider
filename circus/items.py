import scrapy


class OddItem(scrapy.Item):
    odd_value = scrapy.Field()
    odd_name = scrapy.Field()
    match_name = scrapy.Field()


class MatchItem(scrapy.Item):
    match_name = scrapy.Field()
    match_date = scrapy.Field(serializer=str)
