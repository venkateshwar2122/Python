enumerate fxn attaches index to element

chatgpt definitiion:- The enumerate() function adds an index (counter) to an iterable (like a list, tuple, or dictionary) 

x=[10,20,30,40,50]

for index,val in enumerate(x):
  print(index,val)

print(dict(enumerate(x)))

o/p:
0 10
1 20
2 30
3 40
4 50
{0: 10, 1: 20, 2: 30, 3: 40, 4: 50}
