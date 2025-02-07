#LIST OPERATAIONS

1. Adding element into list
    a. add element at end position
    b. adding at beginning or specific index position

2. deleting element from list
    a. deleting element from ending
    b. delete element from beginning or from specific index
    c. delete specif element

3. update element at specif index
_________________________________________________________

1. Adding element into list

a. add element at end position

l=[5,9,8,2]
l.append(10)
print(l)

o/p:
[5, 9, 8, 2, 10]

b. adding at beginning or specific index position

SYNTAX :   list.insert(index,element)

l=[5,9,7,2,4]
l.insert(3,99)
print(l)

o/p:
[5, 9, 7, 99, 2, 4]
____________________________________________________________

2. deleting element from list
    
a. deleting element from ending

l=[5,9,7,2,4]
l.pop()
print(l)

o/p: [5, 9, 7, 2]

b. delete element from beginning or from specific index

SYNTAX:  list.pop(index)

l=[5,9,7,2,4]
l.pop(2)
print(l)

o/p: [5, 9, 2, 4]


c. delete specif element

SYNTAX : list.remove(element)

l=[40,30,10,22,88]
l.remove(10)
print(l)

o/p: [40, 30, 22, 88]
____________________________________________________________________


3. update element at specif index

SYNTAX: list[index] = value

l=[40,30,10,22,88]
l[3]=35
print(l)

o/p:[40, 30, 10, 35, 88]


    


