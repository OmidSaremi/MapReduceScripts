#!/usr/bin/python

import sys
import csv
from collections import  defaultdict
  
# Make a dictionary of the tags: tags as "key" and lists as "value". add ones to the list corresponds to a tag  

tagDic=defaultdict(list)
countDic={}

for line in sys.stdin: 
  row=line.strip().split('\t')
  if len(row)==1: 
    tag=row[0]
    tagDic[tag].append(1)

# Compute total number of each tag and write it in countDic

for key in tagDic:
  countDic[key]=sum(tagDic[key])

# Sort the dictionary based on the values and get the corresponding keys 

topTags=sorted(countDic, key=countDic.get, reverse=True)

# Print the top-ten list by subsetting the list 

print "\n".join(topTags[0:10])  



    
