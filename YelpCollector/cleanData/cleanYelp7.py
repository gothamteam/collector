#insert inspection data which has no phone number
import json
import ast

with open ("inspection/restaurant_dataset", "r") as myfile:
    data1=myfile.readlines()
count=0
for num in range(len(data1)):
    dict=ast.literal_eval(data1[num])
    phone1=dict["phone"]
    print len(phone1)
    flag=0
    if len(phone1)<4:
        count=count+1
print count