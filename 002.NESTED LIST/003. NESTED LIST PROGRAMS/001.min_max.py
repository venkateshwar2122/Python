#QUE: FIND MIN,MAX ELEMENT FROM A GIVEN NESTED LIST

r=int(input())
l=[]

for i in range(r):
 l.append(list(map(int,input().split())))


mi=mx=l[0][0]
for i in l:
  for j in i:
    if j>mx:
      mx=j
    elif j<mi:
      mi=j
print(mi,mx)

I/P:
3
10 20 30 40
23 2 31 32 2 1 29 28
111 478 9 45
O/P:
1 478
