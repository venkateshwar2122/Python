#METHOD 1 

l=[10,20,30,40,50]
k=int(input())
for i in range(k):
  l.append(l.pop(0))

print(l)

I/p:
2
o/p:
[30, 40, 50, 10, 20]


#METHOD2
