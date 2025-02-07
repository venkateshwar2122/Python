QUE:  REVERSE THE LIST

l=list(map(int,input().split()))
i=0
j=len(l)-1
while i<j:
  l[i],l[j]=l[j],l[i]                    # swap
  i=i+1
  j=j-1

print(l)


i/p:
10 20 30
o/p:
[30, 20, 10]

explanation:
two pointer i and j in same list.
i is pointing to first element, j is pointing to last element.
sawp l[i] with l[j]
i++, j--
