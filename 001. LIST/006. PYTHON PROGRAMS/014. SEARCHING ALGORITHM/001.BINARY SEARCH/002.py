a = list(map(int, input().split()))  # Read sorted list of integers
k = int(input())                     # Element to search
l = 0
u = len(a) - 1

while l <= u:                        # Should be l <= u, not l < u
    m = (l + u) // 2  
    if a[m] == k:
        print(m)                     # Element found at index m
        break
    elif k < a[m]:                   # Search in the left half
        u = m - 1
    else:                             # search in the right half
        l = m + 1
else:
    print(-1)                         # ✅ If the element is not found, print -1..............nstaed of using flag variable we are using while-else syntax


i/p:
1 2 3 4 5 6 7 8 9
5
o/p
4







