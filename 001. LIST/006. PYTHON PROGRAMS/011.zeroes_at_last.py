# move all zeroes to last of list

l=[0,0,1,0,0,2,0,3,0,0]
for i in range(len(l)-1):
  for j in range(i+1,len(l)):
    if l[i]==0:
      if l[j]!=0:
        l[i],l[j]=l[j],l[i]
   
print(l)
