# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class resultsItem(scrapy.Item):
    date          = scrapy.Field()
    competition   = scrapy.Field()
    homeTeam      = scrapy.Field()
    awayTeam      = scrapy.Field()
    score         = scrapy.Field()

class fixturesItem(scrapy.Item):
    date        = scrapy.Field()
    competition = scrapy.Field()
    homeTeam    = scrapy.Field()
    awayTeam    = scrapy.Field()

class ranksItem(scrapy.Item):
    rank     = scrapy.Field()
    teamName = scrapy.Field()
    points   = scrapy.Field()
    wins     = scrapy.Field()
    draws    = scrapy.Field()
    losses   = scrapy.Field()