# CREATING A LIST
1) if input are given one by one in next line by user
2)by using list comprehension
3) if input are given in same line separated by space by user
          a)m1
          b)m2
          c)m3
_________________

1) IF input are given one by one in next line by user

NOTE: To add elemens at end position of list
     syntax:  l.append(element)

l=[]
n=int(input())                 #no of elemnt in list
for i in range(n):
  e=int(input())              #add element in list
  l.append(e)
print(l)

i/p:
5
10
20
30
40
50
o/p:
[10, 20, 30, 40, 50]
_____________________________________
2) by using list comprehension

n=int(input())                         #no of element in list
l=[int(input()) for i in range(n)]
print(l)

i/P:
5
10
20
30
40
50
o/p;
[10, 20, 30, 40, 50]
____________________________
      
3) if input that are in same line separted by space into LIST !!!

method 1.
  
l = list(map(int,input().split()))
print(l)

i/p: 10 20 30 50 70                      [note that all input are in same line sepparated by space}
o/p: [10,20,30,50,70]


method2.

l=[int(i) for i in input().split()]
print(l)

i/p:
10 29 3 4 5                            [note that all input are in same line sepparated by space}
o/p:
[10, 29, 3, 4, 5]


method 3. using append

l=[]
for i in input().split():
  l.append(int(i))

print(l)

i/P;
10 20 3 6 78 90                              [note that all input are in same line sepparated by space}
o/p:
[10, 20, 3, 6, 78, 90]
