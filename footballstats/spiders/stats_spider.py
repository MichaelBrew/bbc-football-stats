import scrapy

from footballstats.items import resultsItem
from footballstats.items import fixturesItem
from footballstats.items import ranksItem


# This is where you set the team that you'll be gathering data on and its league
# The team name is taken from the BBC URL, such as: http://www.bbc.com/sport/football/teams/bolton-wanderers
# In that URL, the team name is 'bolton-wanderers'
# You can see the league name in a URL such as: http://www.bbc.com/sport/football/championship/table
# There the league name is simply 'championship'
# I suggest just web searching 'bbc whatever_your_team_is' to view their BBC homepage so you can inspect the
# URL and determine the correct name formatting

TEAM_NAME = "INSERT_TEAM_NAME_HERE"
LEAGUE_NAME = "INSERT_LEAGUE_NAME_HERE"

class resultsSpider(scrapy.Spider):
    name = "results"
    allowed_domains = ["bbc.com"]
    start_urls = ["http://www.bbc.com/sport/football/teams/{0}/results".format(TEAM_NAME)]
    
    def parse(self, response):
        for sel in response.xpath('//tr[@class="report"]'):
            game = resultsItem()
            game['date'] = sel.xpath('td[@class="match-date"]/text()').extract()[0]
            game['homeTeam'] = sel.xpath('td[@class="match-details teams"]/p/span[@class="team-home teams"]/a/text()').extract()[0]
            game['awayTeam'] = sel.xpath('td[@class="match-details teams"]/p/span[@class="team-away teams"]/a/text()').extract()[0]
            game['score'] = sel.xpath('td[@class="match-details teams"]/p/span[@class="score"]/abbr/text()').extract()[0]
            
            competition = sel.xpath('td[@class="match-competition"]/text()').extract()[0]
            if sel.xpath('td[@class="match-competition"]/span'):
                competition = competition + sel.xpath('td[@class="match-competition"]/span/text()').extract()[0]
            game['competition'] = competition
            
            yield game

class fixturesSpider(scrapy.Spider):
    name = "fixtures"
    allowed_domains = ["bbc.com"]
    start_urls = ["http://www.bbc.com/sport/football/teams/{0}/fixtures".format(TEAM_NAME)]
    
    def parse(self, response):
        for sel in response.xpath('//tr[@class="preview"]'):
            game = fixturesItem()
            game['date'] = sel.xpath('td[@class="match-date"]/text()').extract()[0]
            game['homeTeam'] = sel.xpath('td[@class="match-details teams"]/p/span[@class="team-home teams"]/a/text()').extract()[0]
            game['awayTeam'] = sel.xpath('td[@class="match-details teams"]/p/span[@class="team-away teams"]/a/text()').extract()[0]
            
            competition = sel.xpath('td[@class="match-competition"]/text()').extract()[0]
            if sel.xpath('td[@class="match-competition"]/span'):
                competition = competition + sel.xpath('td[@class="match-competition"]/span/text()').extract()[0]
            game['competition'] = competition
    
            yield game

class ranksSpider(scrapy.Spider):
    name = "ranks"
    allowed_domains = ["bbc.com"]
    start_urls = ["http://www.bbc.com/sport/football/{0}/table".format(LEAGUE_NAME)]
    
    def parse(self, response):
        for sel in response.xpath('//table[@class="table-stats"]/tbody/tr'):
            team = ranksItem()
            team['rank'] = sel.xpath('td[@class="position"]/span[@class="position-number"]/text()').extract()[0]
            team['teamName'] = sel.xpath('td[@class="team-name"]/a/text()').extract()[0]
            team['points'] = sel.xpath('td[@class="points"]/text()').extract()[0]
            team['wins'] = sel.xpath('td[@class="won"]/span/text()').extract()[0]
            team['draws'] = sel.xpath('td[@class="drawn"]/text()').extract()[0]
            team['losses'] = sel.xpath('td[@class="lost"]/text()').extract()[0]
            
            yield team

