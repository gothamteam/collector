#1. read generated categorizedUrls.txt
#2. scrapy the page category and number of records
#3. generate all urls for each category given the number of records

import json

#get the name of the category file from input.tx
with open("../store/input.txt") as file:
    content = file.readlines()
content[0]=content[0].strip('\n')
content[1]=content[1].strip('\n')
LocationFileName=content[1].replace(" ", "_")
LocationFileName=LocationFileName.replace(",", "_")


content[1]=content[1].replace(" ", "%20");
content[1]=content[1].replace(",", "%2C");


CategoriizedURLs= '../generated/yelp'+content[0]+LocationFileName+'CategorizedURLs.txt'

with open(CategoriizedURLs) as file:
    content = file.readlines()



categoryFile= '../fetched/yelp'+content[0]+LocationFileName+'Categories.json' 

#load Json file with category data
file2= open(categoryFile)
categoryData = json.load(file2)

#write file with urls for different categories
file3= open('../generated/yelp'+content[0]+LocationFileName+'CategoriizedURLs.txt','w')


for item in categoryData:
    temp=item["category"][0]
    temp=temp.split(":")
    str="&l=p%3A"+temp[0]+"%3A"+temp[1]+"%3A"+temp[2]+"%3A"+temp[3]
    
    
    #reference url
    #{"category": ["NY:New_York:Manhattan:Alphabet_City"]},
    #url=http://www.yelp.com/search/snippet?find_desc=restaurants&find_loc=New%20York%2C%20NY&l=p%3ANY%3ANew_York%3AManhattan%3AAlphabet_City&parent_request_id=85a4b039c1d1cedf&request_origin=user
   
    url="http://www.yelp.com/search/snippet?find_desc="+content[0]+"&find_loc="+content[1]+str
    file3.write(  url+"\n") 
    
    
file3.close()
file2.close()
file.close()