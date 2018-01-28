# -*- coding: utf-8 -*-

import scrapy


class OddItem(scrapy.Item):
    odd_value = scrapy.Field()


class OutcomeItem(scrapy.Item):
    outcome_name = scrapy.Field()


class EventItem(scrapy.Item):
    event_name = scrapy.Field()
