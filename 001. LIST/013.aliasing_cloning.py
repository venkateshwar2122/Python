#ALIASING
Providing more than one name(varaible) for same object is called aliasing.
If u did modification in a object using particular variable ,then all other variables referencing to same object will also reflect the same changes.
In Python, aliasing refers to creating multiple references (aliases) to the same object in memory. 
This means that modifying the object using one reference will affect all other references.


l=[10,20,30,40]
m=l
print(m)
l[2]=99
print(m)

o/p: 
[10, 20, 30, 40]
[10, 20, 99, 40]    #i am changing "l" but the changes reflected in m.
_________________________________________________________________________________

#CLONING

Crearting another copy of existing object is called cloning.
If u did modification on one object using any reference variable then it will not reflect to other object.

THREE METHODS FOR CLONING:----

1. METHOD 1

l=[10,20,30,40]
m=list(l)                             #******************
l[2]=99
print(l)
print(m)

O/P:
[10, 20, 99, 40]
[10, 20, 30, 40]

2. METHOD 2

l=[10,20,30,40]
m=l[::]                             #****************
l[2]=99
print(l)
print(m)

O/P:
[10, 20, 99, 40]
[10, 20, 30, 40]

3. METHOD 3

l=[10,20,30,40]
m=l.copy()                      #**************************
l[2]=99
print(l)
print(m)

O/P:
[10, 20, 99, 40]
[10, 20, 30, 40]
