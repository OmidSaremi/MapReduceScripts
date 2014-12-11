#!/usr/bin/python

import sys
import csv
import re

# This mapper script takes the "tagname" field of enery entry and splits them onarbitrary number of spaces and prints them one per line onto the standard output 

delim="\s+"
reader=csv.reader(sys.stdin, delimiter='\t')
for row in reader: 
  if len(row)==19: 
    tagName=row[2]
    tags=re.split(delim, tagName.strip())
    print "\n".join(tags)




    
