# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class RestaurantItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    neighborhood = Field()
    address = Field()
    phone = Field()
    priceRange = Field()
    starRating=Field()
    category=Field()
    numberOfReviews=Field()
    geoLocation=Field()


    
class categoryItem(Item):
    category=Field()
