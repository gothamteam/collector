from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from yelpCollector.spiders.yelp_spider import yelpSpider
import json
import time
import multiprocessing

#get the name of the category file from input.tx
with open("store/input.txt") as file:
    content = file.readlines()
content[0]=content[0].strip('\n')
content[1]=content[1].strip('\n')
LocationFileName=content[1].replace(" ", "_")
LocationFileName=LocationFileName.replace(",", "_")


content[1]=content[1].replace(" ", "%20");
content[1]=content[1].replace(",", "%2C");

categoryFile= 'fetched/yelp'+content[0]+LocationFileName+'Categories_withNumberOfRecords_includeURL.json' 

#load Json file with category data
file2= open(categoryFile)
categoryData = json.load(file2)


print " number of start urls "+str(len(categoryData))




def doScrap(k):
    
    #generate the list of url with start param 
    
    url= categoryData[k]["url"]
    numberOfRecords= categoryData[k]["numberOfRecords"]
    numberOfPages=int(numberOfRecords)/10+1
    newurls=[]
    for i in range(numberOfPages):
        temp=url.split("&")
        newurl=''
        for j in range( len(temp)-1):
            newurl=newurl+temp[j]+"&"
            if j==1:
                newurl=newurl+"start="+str(i)+"0"+"&"
        newurl=newurl+temp[len(temp)-1] 
        newurls.append(newurl)
    
    
    
    spider = yelpSpider()
    spider.start_urls=newurls
    #get the name of the category file from input.tx
    with open("store/input.txt") as file:
        content = file.readlines()
    content[0]=content[0].strip('\n')
    content[1]=content[1].strip('\n')
    content[1]=content[1].replace(" ", "_");
    content[1]=content[1].replace(",", "_");
    
    overrides= {
        'FEED_URI': 'fetched/'+content[0]+content[1]+'/yelp'+content[0]+content[1]+'Results'+str(k)+'.json' , 
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
    
if __name__ == '__main__':
    jobs = []
    for i in range(len(categoryData)):
        p = multiprocessing.Process(target=doScrap, args=(i,))
        jobs.append(p)
        p.start()

