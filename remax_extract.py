#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET
import re
import csv

## Download File
file = urllib2.urlopen('http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml')
content = file.read()
file.close()


## Open XML File
root = ET.parse('/Users/dwoolfolk/Desktop/BoojCodeTest.xml').getroot()

## Filter Out Non-2016 from DateListed


# parent = root.findall("./Listing/Location")
# parent1 = root.findall("./Listing/ListingDetails/DateListed")
#                        # "[DateListed='2014-10-03 00:00:00']")
# print(parent1)
child = root.getchildren()[0]
kids1 = child.getchildren()[0]
kids2 = child.getchildren()[1]
kids3 = child.getchildren()[2]
kids4 = child.getchildren()[3]
kids5 = child.getchildren()[4]
kids6 = child.getchildren()[5]
kids7 = child.getchildren()[6]
kids8 = child.getchildren()[7]
kids9 = child.getchildren()[8]
kids10 = child.getchildren()[9]
kids11 = child.getchildren()[10]
grandkids = kids11.getchildren()[1]


myData = kids2.findtext('MlsId'), kids2.findtext('MlsName'), kids2.findtext('DateListed'), kids1.findtext('StreetAddress'), \
      kids2.findtext('Price'), kids4.findtext('Bedrooms'), kids4.findtext('Bathrooms'), kids11.findtext('Appliances'), \
      kids4.findtext('Rooms'),  kids4.findtext('Description')

csvfile = open('/Users/dwoolfolk/Desktop/BoojCodeTest2.csv', 'wb')
writer = csv.writer(csvfile, delimiter=",")
writer.writerow(['MlsId', 'MlsName', 'DateListed', 'StreetAddress', 'Price', 'Bedrooms', 'Bathrooms', 'Appliances', \
                 'Rooms',  'Description'])
# for row in myData:
writer.writerow(myData)


print(myData)

print("Writing complete")
