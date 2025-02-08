#QUE. remove a pair of adjacent element in list such that after removing that pair the sum of all other elements present in list is maximum 

l=[1,2,3,4,5]
r=[]
i=j=0
while i<len(l)-1:
    j=i+1
    sum=0
    while j<len(l):
        sum=l[i]+l[j]
        r.append(sum)
        break
    i=i+1
        
x=r.index(min(r))
l.pop(x)
l.pop(x)
print(l)
