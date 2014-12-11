#!/usr/bin/python

import sys
from collections import defaultdict

# A dictionary with "list" values is declared and Initialized to an empty list  

dic=defaultdict(list)

# For each parentID as key, append the answer length as value to the corresponding list.

questionLengthDic={} 

for line in sys.stdin:
    dataMapped = line.strip().split("\t")
    if len(dataMapped) == 3:
      absParentID, questionLength, answerLength =dataMapped
      dic[int(absParentID)].append(int(answerLength))
      questionLengthDic[int(absParentID)]=questionLength

# Compute the average for each key in the dictionary

for key in dic:
         averageAnswerLength=sum(dic[key])/len(dic[key]) 
         qstLength=questionLengthDic[key]       
         print "{0}\t{1}\t{2}".format(key, qstLength, averageAnswerLength)   
        
