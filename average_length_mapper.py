#!/usr/bin/python

import sys
import csv

# Make a dictionary with  question ids as "key" and their corresponding body length as "value"
  
questionDic={}

with open("forum_node.tsv") as f:
  reader=csv.reader(f, delimiter='\t')
  for row in reader: 
    if len(row)==19: 
       nodeID=row[0]
       qBody=row[4]
       nodeType=row[5]
       if nodeType=="question":
         questionDic[int(nodeID)]=len(qBody)

# Read the file again, if an entry is an "answer", find the length of the question it refer to. Write the question id (absParentID), length of the question as well as the answer's length onto the standard output. Warn if a node has been mislabeled as "answer"  

with open("forum_node.tsv") as f:
  reader=csv.reader(f, delimiter='\t')
  for row2 in reader:
    if len(row2)==19: 
      answerBody=row2[4]
      nodeType=row2[5]
      parentID=row2[6]
      absParentID=row2[7]
      if nodeType=="answer": 
        if int(parentID)==int(absParentID):
          answerLength=len(answerBody)  
          if int(absParentID) in questionDic:
            questionLength=questionDic[int(absParentID)]
            print "{0}\t{1}\t{2}".format(absParentID, questionLength, answerLength)
        else: 
          print "Something is not right: An answer node with two IDs not equal!"



    
