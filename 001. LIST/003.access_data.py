NOTE: To know number of element in given list

l = [6,4,5,67,78,9]
print(len(l))           # 6

______________________________________________________________________________

# TO ACCESS DATA FROM A LIST

1) direct access
2) acccess through indexing
3) destructuring

1) DIRECT ACCESS

l =[4,6,2,1,3]
for i in l:
  print(i)

o/p:
4
6
2
1
3
______________________________
2) Access through INdexing

l=[4,6,2,1,3]
for i in range(len(l)):
  print(f"{i}---->{l[i]}")

o/p:
0---->4
1---->6
2---->2
3---->1
4---->3
______________________________

3) destructuring

l=[4,6,2,1,3]
print(*l)                 #separated by space
print(*l,sep="\t")         #separated by tab space

o/p:
4 6 2 1 3
4  	6	  2  	1  	3


