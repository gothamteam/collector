with open ("inspection/restaurant_dataset2_test", "r") as myfile:
#with open ("inspection/restaurant_dataset2", "r") as myfile:
    data1=myfile.read()
data1=data1.decode('iso-8859-1')
with open ("inspection/restaurant_dataset2_testUtf", "w") as myfile:
    myfile.write(data1)
    
a="\u2026"
print repr(a)
print repr(a.decode('unicode-escape'))