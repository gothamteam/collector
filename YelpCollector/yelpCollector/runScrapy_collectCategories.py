from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from yelpCollector.spiders.yelp_spider import yelpCategorySpider

spider = yelpCategorySpider()
#get the name of the category file from input.tx
with open("store/input.txt") as file:
    content = file.readlines()
content[0]=content[0].strip('\n')
content[1]=content[1].strip('\n')
content[1]=content[1].replace(" ", "_");
content[1]=content[1].replace(",", "_");
overrides= {
    'FEED_URI': 'fetched/yelp'+content[0]+content[1]+'Categories.json' , 
    'FEED_FORMAT': 'json',
}
settings = get_project_settings()
settings.overrides.update(overrides)
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel="DEBUG")
reactor.run()
