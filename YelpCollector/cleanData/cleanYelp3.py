import json
        
from sets import Set
#remove duplicate data

with open("yelpDataInOneFileJsonCleanedUp.json") as json_file:
     json_data = json.load(json_file)
print "number of records before removing duplicates:"
print len(json_data)
duplicateCount=0
tempName=Set()
tempNumber=Set()

for number in range(len(json_data)):
    num=number-duplicateCount
    if (json_data[num]["name"] in tempName) and  (json_data[num]["phone"] in tempNumber):
            del json_data[num]
            
            duplicateCount=duplicateCount+1
            #print duplicateCount
    else:
            tempName.add(json_data[num]["name"])
            tempNumber.add(json_data[num]["phone"])

#print tempName
#print len(tempName)
#print tempNumber
#print len(tempNumber)
print "number of records after removing duplicates:"
print len(json_data)

with open("yelpDataInOneFileJsonCleanedUpRemoveDulplicate.json", 'w') as json_file:
    json.dump(json_data, json_file)