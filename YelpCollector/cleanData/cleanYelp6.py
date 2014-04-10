#insert inspection data which has a phone number
import json
import ast
        
from sets import Set
#remove duplicate data
#data5.json
with open("yelpDataInOneFileJsonCleanedUpRemoveDulplicateExtraKeys.json") as json_file:
     json_data = json.load(json_file)
print len(json_data)

#with open ("inspection/restaurant_dataset2_test", "r") as myfile:
with open ("inspection/restaurant_dataset2", "r") as myfile:
    data1=myfile.readlines()
print data1[0]
for num in range(len(data1)):
    dict=ast.literal_eval(data1[num])
    phone1=dict["phone"]
    print phone1 
    flag=0
    if len(phone1)>3:
        for num2 in range(len(json_data)):
            if phone1==json_data[num2]["phone"]:
                flag=1
        if flag==0:
            print "insert this data"
            print num
            json_data.append({u"category":dict["category"].decode('unicode-escape'), u"geoLocation":dict["geoLocation"], u"neighborhood":u'', u"name":dict["name"].decode('unicode-escape') ,u"city": u"New York", u"starRating": u'', u"zipcode":str(dict["zipcode"]).decode('unicode-escape'),u"phone":dict["phone"].decode('unicode-escape'), u"priceRange":u'', u"address":dict["address"].decode('unicode-escape'),u"numberOfReviews":u'', u"insp_scr":str(dict["insp_scr"]).decode('unicode-escape')})
        data1[num]=''
        flag=0
    
    
    

print len(json_data)


#with open("data6.json", 'w') as json_file:
with open("yelpDataInOneFileJsonCleanedUpRemoveDulplicateExtraKeysAddInspectWithPhone.json", 'w') as json_file:
    json.dump(json_data, json_file)
#with open ("inspection/restaurant_dataset3", "w") as myfile:    
with open ("inspection/restaurant_dataset3_withoutPhone", "w") as myfile:
    myfile.writelines(data1)
