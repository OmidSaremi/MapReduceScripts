#!/usr/bin/python

''' This mapper script reads the "entry hour" of every author's post and prints it onto the standard output '''
  
import sys
import csv
import datetime

reader=csv.reader(sys.stdin, delimiter='\t')

while True:
  try: 
    p=reader.next()
    authorID =p[3]
# Decimal point in the "seconds" was causing trouble. I split on "." and took the zeroth-index as "seconds" before stripping the "hour"(e.g., I discarded the fraction). This is fine, since we are interestde in the "hour" of the entry anyway. There might be a more beautiful solution
    dateTime=p[8].split(".")
    print dateTime[0]
    if dateTime[0]!="added_at": 
      t=datetime.datetime.strptime(dateTime[0],"%Y-%m-%d %H:%M:%S").time()
      h=t.hour
      print "{0}\t{1}".format(authorID, h)      
  except csv.Error:
    print "Error"
  except StopIteration:
    print "End of Iteration"
    break


    
