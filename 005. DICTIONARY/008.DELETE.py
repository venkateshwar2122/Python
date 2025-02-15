1. to delete any object from memory "del" will be used.

d={1:10,2:20,3:30,4:40}
del d[2]
print(d)

o/p:
{1: 10, 3: 30, 4: 40}
__________________________________________________________________

2. to delete given key from a dictionary "d.pop(key)" will be used.

d={1:10,2:20,3:30,"name":"venkatesh",4:40}
print(d.pop("name"))   # name is key here
print(d)
print(d.pop(3))       # 3 is key here
print(d)

o/p:
venkatesh
{1: 10, 2: 20, 3: 30, 4: 40}
30
{1: 10, 2: 20, 4: 40}
___________________________________________________________

3.to remove any random key-value pair from dictionary "d.pop(item)" will be used.

d={1:10,2:20,3:30,"name":"venkatesh",4:40}
print(d.popitem())
print(d)

o/p:
(4, 40)
{1: 10, 2: 20, 3: 30, 'name': 'venkatesh'}
