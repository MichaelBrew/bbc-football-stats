import scrapy

class resultsItem(scrapy.Item):
  date = scrapy.Field()
  competition = scrapy.Field()
  homeTeam = scrapy.Field()
  awayTeam = scrapy.Field()
  score = scrapy.Field()

class fixturesItem(scrapy.Item):
  date = scrapy.Field()
  competition = scrapy.Field()
  homeTeam = scrapy.Field()
  awayTeam = scrapy.Field()

class ranksItem(scrapy.Item):
  rank = scrapy.Field()
  teamName = scrapy.Field()
  points = scrapy.Field()
  wins = scrapy.Field()
  draws = scrapy.Field()
  losses = scrapy.Field()
