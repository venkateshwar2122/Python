1. UNION
2. INTERSECTION
3. DIFFERENCE
4. SYMMETRIC DIFFERENCE
5. SUBSET
6. DISJOINT SET
____________________________________________________________________________

1. UNION

s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s|t)             #method1, doesnt modify original set
print(s)
print(s.union(t))      #method2, doesnt modify original set  
print(s)
print(s.update(t))            #method3, modifies original set
print(s)

o/p:
{1, 2, 3, 4, 5, 7, 8, 9}
{1, 2, 5, 8, 9}
{1, 2, 3, 4, 5, 7, 8, 9}
{1, 2, 5, 8, 9}
None
{1, 2, 3, 4, 5, 7, 8, 9}


2. INTERSECTION


s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s&t)             #method1, doesnt modify original set
print(s)
print(s.intersection(t))      #method2, doesnt modify original set  
print(s)
print(s.intersection_update(t))            #method3, modifies original set
print(s)

O/P:
{1, 5, 9}
{1, 2, 5, 8, 9}
{1, 5, 9}
{1, 2, 5, 8, 9}
None
{1, 5, 9}


3. DIFFERENCE


s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s-t)             #method1, doesnt modify original set
print(t-s)
print(s)

print(s.difference(t))      #method2, doesnt modify original set  
print(s)
print(s.difference_update(t))            #method3, modifies original set
print(s)

O/P:
{8, 2}
{3, 4, 7}
{1, 2, 5, 8, 9}
{8, 2}
{1, 2, 5, 8, 9}
None
{2, 8}


4. SYMMETRIC DIFFERENCE

s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s^t)             #method1, doesnt modify original set
print(s)
print(s.symmetric_difference(t))      #method2, doesnt modify original set  
print(s)
print(s.symmetric_difference_update(t))            #method3, modifies original set
print(s)

o/p:
{2, 3, 4, 7, 8}
{1, 2, 5, 8, 9}
{2, 3, 4, 7, 8}
{1, 2, 5, 8, 9}
None
{2, 3, 4, 7, 8}



5.  SUBSET


s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s<t)             #method1
print(s.issubset(t))      #method2

s={3,1,7}
print(s<t)
print(s.issubset(t))


o/p:
False
False
True
True




6. DISJOINT SET


s={5,8,1,2,9}
t={5,9,3,4,7,1}
print(s.isdisjoint(t))     # FALSE BECAUSE THERE ARE COMMON ELEMENTS

s={8,12,19}
print(s.isdisjoint(t))      # true

o/p:
False
True

