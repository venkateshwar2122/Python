QUE. find lonely integer from given list
note: lonely integer means the elements which are not repeated more than 1 time

l=[50,80,70,20,30,80,30,40,20,10,50,20,70,100]

for i in l:
  if l.count(i)==1:
    print(i)

o/p:
40
10
100
