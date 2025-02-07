QUE. display which element was repeated highest number of times in a list and how aslo mention how many time it was repeated

l=[50,80,70,20,30,80,30,40,20,10,50,20,70]
ele=l[0]
max=1                                       # every element is repeated atleast one time

for i in set(l):                       # set(l) is a list that contain unique elements from l
  count=0                             # initialising count in each iteration of i
  for j in l:
    if i==j:
      count=count+1
      
  if count>max:
    max=count
    ele=i
    
print(ele,max)

o/p:
20  3


explanation:
one list is l that contains duplicate elements
another list is set(l) which contain unique elements froml
now,
take one pointer in set(l) and another pointer in l
compare each each element of l with set(l)
