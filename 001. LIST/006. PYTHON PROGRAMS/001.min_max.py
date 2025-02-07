QUE. Find min,max elemnt from a given list

l= list(map(int,input().split()))
min=max=l[0]
for i in l:
  if max<i:                             # max<i       i is greateer than max
    max=i
  elif min>i:                           # min>i       i is less than min
    min=i

print(max,min)
