#ACCESSING DATA FROM NESTED LIST

l=[[4,6,5,7],[8,9,1,2],[7,9,8,999,3],[5,9,8]]

print(len(l))              # 4
print(l[0])                # [4, 6, 5, 7]
print(l[1])                # [8, 9, 1, 2]
print(l[2][3])             # 999

_____________________________________________________

1.  ACCESSING ALL LIST PRESENT INSIDE NESTED LIST

l=[[4,6,5,7],[8,9,1,2],[7,9,8,999,3],[5,9,8]]

for i in l:
  print(i)

o/p:
[4, 6, 5, 7]
[8, 9, 1, 2]
[7, 9, 8, 999, 3]
[5, 9, 8]

_______________________________________________________________

2. ACCESSING EACH ELEMENT PRESENT INSIDE NESTED LIST

l=[[4,6,5,7],[8,9,1,2],[7,9,8,999,3],[5,9,8]]

for i in l:
  for j in i:
    print(j, end=" ")
  print()

o/p:
4 6 5 7 
8 9 1 2 
7 9 8 999 3 
5 9 8 
______________________________________________________________________

3. ACCEESSING EACH ELEMENT THROUGH INDEXING

l=[[4,6,5,7],[8,9,1,2],[7,9,8,999,3],[5,9,8]]

for i in range(len(l)):
  for j in range(len(l[i])):
    print(l[i][j], end=" ")
  print()

O/P:
4 6 5 7 
8 9 1 2 
7 9 8 999 3 
5 9 8 
__________________________________________________________________



