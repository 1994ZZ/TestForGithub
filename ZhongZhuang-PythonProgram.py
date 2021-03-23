
"""
Program: Commodity Data, Filtering and Visualization
Author:Zhong Zhuang
Description: Coding same statements as the Word Document's statements
Revisions: 
       00 - Understanding the codes from the Word Document
       01 - Writing the same coding statements
           
"""
#import matplotlib modules to operation of data graphy
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

#import csv module to read CSV file with structured data
#with open( document name), as the data name is "csvfile"
#reader is a funcation and can read csv modules content
#data is show all of row, every row in for loop in reader
import csv
with open('produce_csv.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

#give price a value "$2.15"
#give cost a value, float value, use replace function to replace $ with ' '
price = "$2.15"
cost = float(price.replace('$',''))
print(price)#$2.15
print(cost)#2.15


# to import the datetime module
# give dateString a string value "4/9/2020"
# give date a value, use strptime function change dateString struction
from datetime import datetime
dateString = "4/9/2020"
date = datetime.strptime(dateString,"%m/%d/%Y")
print(date)#2020-04-09 00:00:00
#print(str(date))
#print(datetime.strptime(dateString,"%m/%d/%Y"))

#create a modDate as a empty list
#for loop, every row in data
#build a new empty list to receive values
#build a another for loop to traverse the values in the old row
#if-elif-else to decision function orders
modData = []
for row in data:
    newRow = list()
    for item in row:
        if "$" in item:# if item includes $
            #append to add new content that replace $ with ""
            newRow.append(float(item.replace("$","")))
        elif "/" in item:# if item includes /
            #append to add new content that strptime to change date struction
            newRow.append(datetime.strptime(item,'%m/%d/%Y'))
        else:# if not meet if and elif conditions
            newRow.append(item)#append new content to list
    modData.append(newRow)#add all of new content to new modDate list
#print part of (modData) 
#[['Commodity', 'Date', 'Farm', 'Atlanta', 'Chicago', 'Los Angeles', 'New York'], 
#['Strawberries', datetime.datetime(2018, 2, 25, 0, 0), 1.5, 2.13, 3.03, 2.75, 2.74], 
#['Romaine Lettuce', datetime.datetime(2018, 2, 25, 0, 0), 0.78, 1.79, 2.09, 1.47, 1.97], 
#['Red Leaf Lettuce', datetime.datetime(2018, 2, 25, 0, 0), 0.44, 1.42, 1.75, 1.47, 1.65], 
#['Potatoes', datetime.datetime(2018, 2, 25, 0, 0), 1.6, 3.97, 3.81, 3.99, 5.47],...]

#remove header and slice
locations = modData.pop(0)[2:]
records =list()#build a new empty list for data record
for row in modData:#for loop every row in modData
    newRow = row[:2]# first two value in list row.
    #zip function to combine two listes together
    #for loop, every list relative position loc,price values
    for loc, price in zip(locations, row[2:]):# traverse locations and prices
        records.append(newRow+[loc,price])#append new content to list

#list comprehensive to let select as list type
#choose list first and third position contents are oranges and chicago
select = list(filter(lambda x:x[0] == "Oranges" and x[2] == "Chicago",records))

# every x in select list second position
dates = [ x[1] for x in select]
# every x in select list fourth position
prices = [ x[3] for x in select]

#zip to combine two lists together
#for loop every d,p in new combined list
dpMerge = [[d,p] for d,p in zip(dates,prices)]
#sort dpMerge first position element in dpMerge lsit
dpMerge.sort(key=lambda a:a[0])


#for loop in every x in dpMerge
for x in dpMerge:
    #print result with f to simple statement
    print(f'{datetime.strftime(x[0],"%m-%d-%Y")} {int(25 * x[1])*"="}')


fig = plt.figure()#create a figure, returns a figure object
ax = fig.add_subplot()#add axis object to the figure

ax.plot(dates,prices,label="Oranges in Chicago")#add the data series

ax.set_xlabel('date')# a title for the x-axis
ax.set_ylabel('price in dollars')#a title for the y-axis

fmt = '${x:,.2f}' # format for dollars w/ 2 decimal places
tick = mtick.StrMethodFormatter(fmt) # define the format
ax.yaxis.set_major_formatter(tick) # establish format for y-axis labels

plt.legend()#add a legend
plt.show()#show the figures











