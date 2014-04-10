#add cuisine text to restaurant_dataset
import ast

cuisine=dict()
with open ("inspection/Cuisine.txt", "r") as myfile:
    data=myfile.readlines()

print len(data)
print data[0]

for num in range(len(data)):
    temp=data[num].split(',')
    #print temp[0]
    #print temp[1]
    cuisine[int(temp[0].strip("\""))]=temp[1].strip("\",\n")
print cuisine
print cuisine[25]
with open ("inspection/restaurant_dataset", "r") as myfile:
    data1=myfile.readlines()
print data1[0]
for num in range(len(data1)):
    data1[num]=data1[num].replace("addr","address").replace("location","geoLocation").replace("type", "category")
    dict=ast.literal_eval(data1[num])
    print cuisine[(dict["category"])]
    dict["category"]= cuisine[(dict["category"])]
    data1[num]= str(dict)+'\n'

with open ("inspection/restaurant_dataset2", "w") as myfile:
    myfile.writelines(data1)
#dict=ast.literal_eval(data1[0])
#print dict['name']