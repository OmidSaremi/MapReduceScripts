#!/usr/bin/python

import sys
import csv
  
# If a forum entry is a "comment" or "answer", print its abs_parent_id (the id of the "question" it refers to) and its author_id 

with open("forum_node.tsv") as f:
  reader=csv.reader(f, delimiter='\t')
  for row2 in reader:
    if len(row2)==19:
      nodeID=row2[0] 
      authorID=row2[3]
      nodeType=row2[5]
      absParentID=row2[7]
      if nodeType=="answer" or nodeType=="comment": 
        print "{0}\t{1}".format(absParentID, authorID)

# To keep the identity of the student asking the question: If a node is a "question" node, keep the questionID and the authorID

      if nodeType=="question":
        print "{0}\t{1}".format(nodeID, authorID)


    
