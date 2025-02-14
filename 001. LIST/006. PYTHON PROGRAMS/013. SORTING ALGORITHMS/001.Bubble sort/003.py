# How Bubble Sort Works:-
1. Compare adjacent elements: If the left element is greater than the right, swap them.
2. Continue comparing and swapping until the largest element moves to the end.

________________________________________________________________________________________
  
l = list(map(int, input().split()))
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)


I/P:
8 12 3 5 9 7 14
O/P:
[3, 5, 7, 8, 9, 12, 14]
