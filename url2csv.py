import pycurl
from cStringIO import StringIO
import csv

try:
    buffer = StringIO()
    d = pycurl.Curl()
    d.setopt(d.URL, 'http://host:port/getResultsForYourData?parameters=your%20values')
    d.setopt(d.WRITEDATA, buffer)
    d.perform()
    if(buff.getvalue() == ""): # if no response, retry 3 times
        for x in range(0, 3):
            d.perform()
    d.close()
except:
    print "Error getting data from the API"

data = buffer.getvalue()

# Some string manipulation
ids = []
dates = []
id1 = data.split("u'access_key': ")
date1 = data.split("u'date_created': ")

for i in range(len(id1) -1): #split creates an extra string at the begining
    id2 = id1[i+1].split(", 'next/following_pattern':")
    ids.append(id2[0])
    date2 = date1[i+1].split("}")
    dates.append(date2[0])

# Write data to CSV file.
try:
    writeFile = csv.writer(open('data.csv', 'wb', buffering=0))
    writeFile.writerow([('id'), ('date_created'), ('state')])
except:
    print "Error creating csv file for writing"
    raise

for index in range(len(id1) -1):
    writeFile.writerow([(ids[index]),(dates[index]),('CA')])


print 'The CSV file is saved into the local directory as {}'.format('data.csv')
