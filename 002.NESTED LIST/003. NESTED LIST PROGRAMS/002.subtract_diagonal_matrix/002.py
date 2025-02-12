# QUE: CALCULATE ABSOLUTE DIFFERENCE BETWEEN SUM OF DIAGONAL ELEMENTS FROM THE N*N MATRIX

n=int(input())               # note that its n*n matrix, therfore both matrix length will be same
l=[]
for i in range(n):
  l.append(list(map(int,input().split())))

d1=d2=0

for i in range(n):
  d1= d1 + l[i][i]
  d2= d2 + l[i][n-1-i]

print(abs(d1-d2))


i/p:
4
6 1 3 2
4 7 9 3
6 3 9 1
9 3 1 9
o/p:
8
