#!/usr/bin/python

import sys
import csv
from collections import defaultdict
  
# The reducer scripts prints a "list" per-line. The zeroth element is the ID of the question and the rest of the list elements are the authorIDs of the studentswho answered or commented on that specific question 

studyGroup=defaultdict(list)

for line in sys.stdin:
  row=line.strip().split('\t')
  if len(row)==2: 
    questionID=row[0]
    student=row[1]
    studyGroup[questionID].append(student)
for key in studyGroup:
   print [key]+studyGroup[key]  


    
