# Scrapy settings for yelpCollector project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yelpCollector'

SPIDER_MODULES = ['yelpCollector.spiders']
NEWSPIDER_MODULE = 'yelpCollector.spiders'

FEED_URI= 'items.json'  
FEED_FORMAT= 'json'
LOG_LEVEL ='DEBUG'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yelpCollector (+http://www.yourdomain.com)'
