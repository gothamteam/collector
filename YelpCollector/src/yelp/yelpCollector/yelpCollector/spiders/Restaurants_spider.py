from scrapy.spider import Spider
from scrapy.selector import Selector
import json

from yelpCollector.items import RestaurantItem
class yelpSpider(Spider):
    name = "yelp"
    allowed_domains = ["http://www.yelp.com/"]
    start_urls = [
        "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true",
       "http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&start=10&l=p%3ANY%3ANew_York%3AQueens%3AFlushing&parent_request_id=28a3b910a7c56207&request_origin=hash&bookmark=true"
    ]

    def parse(self, response):
        jsonresponse=json.loads(response.body)
        response=response.replace(body=jsonresponse["search_results"])
        print("eeee")
        print(response)
        print("eee")
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
            items.append(item)
        return items