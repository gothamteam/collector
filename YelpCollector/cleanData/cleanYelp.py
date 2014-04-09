#read file 

import json

with open("yelp/yelpRestaurantsNew_York__NYResults352.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

with open("yelp/yelpRestaurantsNew_York__NYResults496.json") as json_file:
    json_data2 = json.load(json_file)
    print(json_data2)



with open('data.json', 'w') as outfile:
  json.dump(json_data, outfile)
  json.dump(json_data2, outfile)