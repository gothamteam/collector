import json
        

#with open ("data2.json", "r") as myfile:
 #   json_data = json.load(myfile)
#print len(json_data)

#clean up yelp data 
with open("yelpDataInOneFileJson.json") as json_file:
     json_data = json.load(json_file)
for num in range(len(json_data)):
   
    if len(str(json_data[num]["starRating"]))>3:
        json_data[num]["starRating"]=str(json_data[num]["starRating"])[3:6]
    else:
        json_data[num]["starRating"]=''
    if len(str(json_data[num]["numberOfReviews"]))>3:
        json_data[num]["numberOfReviews"]=str(json_data[num]["numberOfReviews"]).split()[0][3:]
    else:
        json_data[num]["numberOfReviews"]=''
    if len(str(json_data[num]["neighborhood"]))>3:
        json_data[num]["neighborhood"]=json_data[num]["neighborhood"][0]
    else:
        json_data[num]["neighborhood"]=''
    if len(str(json_data[num]["phone"]))>3:
        json_data[num]["phone"]=json_data[num]["phone"][0]
        json_data[num]["phone"]=json_data[num]["phone"][1:4]+json_data[num]["phone"][6:9]+json_data[num]["phone"][10:]
    else:
        json_data[num]["phone"]=''
    if len(str(json_data[num]["priceRange"]))>3:
        json_data[num]["priceRange"]=json_data[num]["priceRange"][0]
    else:
        json_data[num]["priceRange"]=''
    if len(str(json_data[num]["numberOfReviews"]))>3:
        json_data[num]["numberOfReviews"]=json_data[num]["numberOfReviews"][0]
    else:
        json_data[num]["numberOfReviews"]=''
    if len(str(json_data[num]["name"]))>3:
        json_data[num]["name"]=json_data[num]["name"][0]
    else:
        json_data[num]["name"]=''

with open("yelpDataInOneFileJsonCleanedUp.json", 'w') as json_file:
    json.dump(json_data, json_file)