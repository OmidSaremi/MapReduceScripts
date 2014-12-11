#!/usr/bin/python

# This reducer script find the most active hour of a student 

import sys
from collections import defaultdict

# The function "counter" takes a dictionary of hours and an ID as ("key") and finds the most active hour (largest "value" in the list), if more than one candidate as "most active", it returns all of them. 

def counter(dic, ID):
    h=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    for item in dic[ID]:
        h[item]=h[item]+1
    m=max(h)
    return [i for i in range(len(h)) if h[i]==m]  

# Make a dictionary with authorID as key and a "list" of hours as "value" 

dicAuthorActivity=defaultdict(list)

for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) == 2:
    authorID, h =data_mapped
    dicAuthorActivity[int(authorID)].append(int(h))
c=0
for key in dicAuthorActivity:
  c+=1
  result=counter(dicAuthorActivity, key);
  for item in result:
    print "{0}\t{1}".format(key, item)             
    
