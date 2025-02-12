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

______________________________________________
#METHOD2

l=[10,20,30,40,50]
k=int(input())

k=k%len(l)                             # Ensures k is within bounds means it will not able to give index error when user gives input k which can be more than the length of list and it also helps in raotaion
print(l[k:]+l[:k])

i/p:
2
o/p:
[30, 40, 50, 10, 20]


CHATGPT: 

Understanding the Rotation Step by Step:--

List before rotation:
[10, 20, 30, 40, 50]
___________________________
Example 1: User enters k = 1
Step-by-Step Execution
k = 1 % 5 = 1 (No change since k < len(l))
l[k:] → l[1:] → [20, 30, 40, 50]
l[:k] → l[:1] → [10]
Concatenation: [20, 30, 40, 50] + [10]
Final List After Rotation by 1:
[20, 30, 40, 50, 10]
____________________________________

Example 2: User enters k = 2
Step-by-Step Execution
k = 2 % 5 = 2
l[k:] → l[2:] → [30, 40, 50]
l[:k] → l[:2] → [10, 20]
Concatenation: [30, 40, 50] + [10, 20]
Final List After Rotation by 2:
[30, 40, 50, 10, 20]

___________________________________________

Example 3: User enters k = 3
Step-by-Step Execution
k = 3 % 5 = 3
l[k:] → l[3:] → [40, 50]
l[:k] → l[:3] → [10, 20, 30]
Concatenation: [40, 50] + [10, 20, 30]
Final List After Rotation by 3:
[40, 50, 10, 20, 30]

____________________________________________

Example 4: User enters k = 5 (Full Rotation)
Step-by-Step Execution
k = 5 % 5 = 0
l[k:] → l[0:] → [10, 20, 30, 40, 50]
l[:k] → l[:0] → []
Concatenation: [10, 20, 30, 40, 50] + []
Final List After Rotation by 5 (No Change):
[10, 20, 30, 40, 50]

____________________________________________

Example 5: User enters k = 7 (Larger than List Length)
Step-by-Step Execution
k = 7 % 5 = 2 (Equivalent to rotating by 2 places)
l[k:] → l[2:] → [30, 40, 50]
l[:k] → l[:2] → [10, 20]
Concatenation: [30, 40, 50] + [10, 20]
Final List After Rotation by 7 (Same as k=2):
[30, 40, 50, 10, 20]
_______________________________

Summary of Rotations
k(input)   	k % len(l)	                      Final List After Rotation
1	          1	                                [20, 30, 40, 50, 10]
2         	2                                	[30, 40, 50, 10, 20]
3         	3                                	[40, 50, 10, 20, 30]
4          	4	                                [50, 10, 20, 30, 40]
5	          0	                                [10, 20, 30, 40, 50] (No change)
6           1                                 [20, 30, 40, 50, 10]
7	          2                                	[30, 40, 50, 10, 20]
________________________________________________________________________
Why Use k % len(l)?
Ensures that k never exceeds the list length, preventing errors.
Allows cycling through the list even when k is very large.
Efficient as it avoids unnecessary iterations.
