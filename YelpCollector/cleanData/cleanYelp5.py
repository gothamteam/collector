#split the address to address, city and zipcode
import json
        
from sets import Set
#remove duplicate data

with open("yelpDataInOneFileJsonCleanedUpRemoveDulplicate.json") as json_file:
     json_data = json.load(json_file)

print len(json_data)


for num in range(len(json_data)):
    print json_data[num]["address"]
    if len(json_data[num]["address"])==2:
        json_data[num]["zipcode"]=json_data[num]["address"][1][-5:]
        json_data[num]["city"]=json_data[num]["address"][1][:-6]
        json_data[num]["address"]=json_data[num]["address"][0]
        json_data[num]["insp_scr"]=''
    elif len(json_data[num]["address"])==1:
        json_data[num]["zipcode"]=json_data[num]["address"][0][-5:]
        json_data[num]["city"]=json_data[num]["address"][0][:-6]
        json_data[num]["address"]=''
        json_data[num]["insp_scr"]=''
    else:
        json_data[num]["zipcode"]=''
        json_data[num]["city"]=''
        json_data[num]["address"]=''
        json_data[num]["insp_scr"]=''

with open("yelpDataInOneFileJsonCleanedUpRemoveDulplicateExtraKeys.json", 'w') as json_file:
    json.dump(json_data, json_file)