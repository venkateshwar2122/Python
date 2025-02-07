QUE: merge 2 sorted into a single sorted list

# NOTE THAT BOTH THE GIVEN INPUT LISTS SHOULD BE SORTED

l=list(map(int,input().split()))
m=list(map(int,input().split()))
r=[]
i=j=0

while i<len(l) and j<len(m):
  if l[i]<m[j]:
    r.append(l[i])
    i=i+1
  else:
    r.append(m[j])
    j=j+1

while i<len(l):             # if elements are left in l list
  r.append(l[i])
  i=i+1

while j<len(m):              # if elements are left in m list
  r.append(m[j])
  j=j+1

print(r)
  
  
i/p:
1 5 8 9
0 4 7 8 9 66
o/p:
[0, 1, 4, 5, 7, 8, 8, 9, 9, 66]

explanation:
i pointer in l list
j pointer in m list
