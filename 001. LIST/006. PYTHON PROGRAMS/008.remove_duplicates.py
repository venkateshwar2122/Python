QUE: remove dupliactes from list

method 1:

l=list(map(int,input().split()))
r=[]

for i in l:
  if i not in r:
    r.append(i)
print(r)

i/p:
10 20 20 30 30 30 40 50
o/p:
[10, 20, 30, 40, 50]


method 2: using two pointers

l=list(map(int,input().split()))
i=0

while i<len(l)-1:
  j=i+1
  while j<len(l):
    if l[i]==l[j]:
      l.pop(j)
    else:
      j=j+1
  i=i+1

print(l)

i/p:
10 10 20 30 20 80 30 80 20
o/p:
[10, 20, 30, 80]


explanation:
two pointers i and j in the same list l.
i is starting from 1st element and j is staring from 2nd element.
i will go untill 2nd last element and j will go till last element
 
