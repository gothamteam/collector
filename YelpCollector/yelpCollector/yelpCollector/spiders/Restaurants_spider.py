from scrapy.spider import Spider
from scrapy.selector import Selector
import json

from yelpCollector.items import RestaurantItem,categoryItem
class yelpSpider(Spider):
    
    name = "yelp"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls = [
        "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true",
        "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true"
    ]
    def __init__(self):
        super(Spider, self).__init__()
        print 'Do something else'
        with open("generatedUrlLists.txt") as urlList:
            urlListData = urlList.readlines()
        #self.start_urls=urlListData
        print urlListData
    def parse(self, response):
        jsonresponse=json.loads(response.body)
        response=response.replace(body=jsonresponse["search_results"])
        #print("eeee")
        #print(response)
        #print("eee")
        sel = Selector(response)
        sites = sel.xpath('//ul/li/div')
        items = []
        for site in sites:
            item = RestaurantItem()
            item['name'] = site.xpath('div/div[@class="media-story"]/h3/span/a/text()').extract()
            item['neighborhood'] = site.xpath('div[@class="secondary-attributes"]/span[@class="neighborhood-str-list"]/text()').extract()
            item['address'] = site.xpath('div[@class="secondary-attributes"]/address/text()').extract()
            item['phone'] = site.xpath('div[@class="secondary-attributes"]/span[@class="biz-phone"]/text()').extract()
            item['priceRange'] = site.xpath('div/div[@class="media-story"]/div[@class="price-category"]/span[@class="bullet-after"]/span/text()').extract()
            item['category'] = site.xpath('div/div[@class="media-story"]/div[@class="price-category"]/span[@class="category-str-list"]/a/text()').extract()
            item['starRating'] = site.xpath('div/div[@class="media-story"]/div/div[@class="rating-large"]/i/@title').extract()
            item['numberOfReviews'] = site.xpath('div/div[@class="media-story"]/div/span[@class="review-count rating-qualifier"]/text()').extract()
            
            #get the geo location for each restaurants
            key=site.xpath('@data-key').extract()
            latitude=jsonresponse['search_map']['markers'][key[0]]['location']['latitude']
            longitude=jsonresponse['search_map']['markers'][key[0]]['location']['longitude']
            item['geoLocation']=[latitude,longitude]
            
            #trim the content
            item['neighborhood'] = [i.strip() for i in item['neighborhood']]
            item['phone'] = [i.strip() for i in item['phone']]
            item['address'] = [i.strip() for i in item['address']]
            item['numberOfReviews'] = [i.strip() for i in item['numberOfReviews']]
            items.append(item)
        return items
    
#category Spider    
class yelpRestaurantCategory(Spider):
    name = "yelpRestaurantCategory"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls = [
       "http://www.yelp.com/search?find_desc=restaurants&find_loc=New+York%2C+NY&ns=1#start=0"
    ]
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="more place-more"]/li/div/ul/li')
        categoryLists = []
        for site in sites:
            categoryList = categoryItem()
            categoryList['category'] = site.xpath('label/input/@value').extract()
            categoryLists.append(categoryList)
        return categoryLists