from scrapy.spider import Spider
from scrapy.selector import Selector
import json

from yelpCollector.items import RestaurantItem,categoryItem,NumberofRecordsItem,NumberofRecordsItem_withUrl
class yelpSpider(Spider):
    
    name = "yelpSpider"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls = [
        "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true",
        "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true"
    ]
    def __init__(self):
        super(Spider, self).__init__()
        with open("generatedUrlLists.txt") as urlList:
            urlListData = urlList.readlines()
        #self.start_urls=urlListData
        print urlListData
    def parse(self, response):
        jsonresponse=json.loads(response.body)
        response=response.replace(body=jsonresponse["search_results"])

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
class yelpCategorySpider(Spider):
    name = "yelpCategorySpider"
    allowed_domains = ["http://www.yelp.com/"]
   
    def __init__(self):
        super(Spider, self).__init__()
        self.getInput()
    
    #get the search field from input.txt
    def getInput(self):
        with open("store/input.txt") as file:
            content = file.readlines()
        
        #modify the city and state name so that it is like what is in a url
        content[1]=content[1].strip('\n')
        content[1]=content[1].replace(" ", "+");
        content[1]=content[1].replace(",", "%2C");
        self.start_urls=[
                    "http://www.yelp.com/search?find_desc="+content[0].strip('\n')+"&find_loc="+content[1]+"&ns=1"
        ]
        
    start_urls=[]
    
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="more place-more"]/li/div/ul/li')
        categoryLists = []
        for site in sites:
            categoryList = categoryItem()
            categoryList['category'] = site.xpath('label/input/@value').extract()
            categoryLists.append(categoryList)
        return categoryLists
    
    #category Spider    
class yelpNumberOfRecordsSpider(Spider):
    name = "yelpNumberOfRecordsSpider"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls=[
    ]
    def __init__(self):
        super(Spider, self).__init__()
        self.getInput()
    
    #get the search field from input.txt
    def getInput(self):
        with open("store/input.txt") as file:
            content = file.readlines()
            self.start_urls=content
            content[0]=content[0].strip('\n')
            content[1]=content[1].strip('\n')
            LocationFileName=content[1].replace(" ", "_")
            LocationFileName=LocationFileName.replace(",", "_")

            CategoriizedURLs= 'generated/yelp'+content[0]+LocationFileName+'CategorizedURLs.txt'
            
        with open(CategoriizedURLs) as file:
            content = file.readlines()
            self.start_urls=content
    def parse(self, response):
        jsonresponse=json.loads(response.body)
        response=response.replace(body=jsonresponse["search_header"])
        response2=response.replace(body=jsonresponse["search_filters"])
        sel = Selector(response)
        sel2= Selector(response2)
        sites = sel.xpath('//span[@class="pagination-results-window"]')
        sites2 = sel2.xpath('//div[@class="filter-set place-filters"]/ul/li/label/input[@checked="checked"]')
        items = []
        for site in sites:
            item = NumberofRecordsItem()
            item['numberOfRecords']= site.xpath('./text()').extract()
            item['category']= sites2.xpath('./@value').extract()
            
            #trim the content
            item['numberOfRecords'] = [i.strip() for i in item['numberOfRecords']]
            temp=item['numberOfRecords'][0].split(" ")
            item['numberOfRecords']=temp[3]
            
            
            items.append(item)
        return items
    
class yelpNumberOfRecordsSpider_includeURL(Spider):
    name = "yelpNumberOfRecordsSpider_includeURL"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls=[
    ]
    def __init__(self):
        super(Spider, self).__init__()
        self.getInput()
    
    #get the search field from input.txt
    def getInput(self):
        with open("store/input.txt") as file:
            content = file.readlines()
            self.start_urls=content
            content[0]=content[0].strip('\n')
            content[1]=content[1].strip('\n')
            LocationFileName=content[1].replace(" ", "_")
            LocationFileName=LocationFileName.replace(",", "_")

            CategoriizedURLs= 'generated/yelp'+content[0]+LocationFileName+'CategorizedURLs_withPriceRank.txt'
            
        with open(CategoriizedURLs) as file:
            content = file.readlines()
            self.start_urls=content
    def parse(self, response):
        jsonresponse=json.loads(response.body)
        response=response.replace(body=jsonresponse["search_header"])
        response2=response.replace(body=jsonresponse["search_filters"])
        sel = Selector(response)
        sel2= Selector(response2)
        sites = sel.xpath('//span[@class="pagination-results-window"]')
        sites2 = sel2.xpath('//div[@class="filter-set place-filters"]/ul/li/label/input[@checked="checked"]')
        items = []
        for site in sites:
            item = NumberofRecordsItem_withUrl()
            item['numberOfRecords']= site.xpath('./text()').extract()
            item['url']= response.url
            
            #trim the content
            item['numberOfRecords'] = [i.strip() for i in item['numberOfRecords']]
            temp=item['numberOfRecords'][0].split(" ")
            item['numberOfRecords']=temp[3]
            
            
            items.append(item)
        return items
    