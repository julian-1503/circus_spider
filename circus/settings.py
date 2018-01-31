# -*- coding: utf-8 -*-

# Scrapy settings for circus project

BOT_NAME = 'circus'

SPIDER_MODULES = ['circus.spiders']
NEWSPIDER_MODULE = 'circus.spiders'

# ScrapySplash settings
SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':
    810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# database settings
DATABASE = {
    'drivername': 'sqlite',
    'database': 'circus.sqlite'
}

#pipelines
ITEM_PIPELINES = {
    'circus.pipelines.CircusPipeline': 300
}


DOWNLOAD_TIMEOUT = 40
