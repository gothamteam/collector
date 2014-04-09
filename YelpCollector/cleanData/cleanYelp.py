#read file 
#create one file for yelp
import json


    
json_data=[None]*556
for num in range(556):
    with open("yelp/yelpRestaurantsNew_York__NYResults"+str(num)+".json") as json_file:
        json_data[num] = json.load(json_file)
        
        print num
    

#with open('data.json', 'w') as outfile:
  #json.dump(json_data, outfile)
  #json.dump(json_data2, outfile)

with open('yelpDataInOneFile.json', 'w') as outfile:
    for num in range(556):
        json.dump(json_data[num], outfile)
        
        print num
        
    
with open ("yelpDataInOneFile.json", "r") as myfile:
    data=myfile.read().replace('][', ',')
with open ("yelpDataInOneFileJson.json", "w") as myfile:
    myfile.write(data)
    