#sort first k elements in ascending order and remaining elements in descending order

l = list(map(int, input().split()))

k = int(input())

print( sorted(l[:k]) + sorted(l[k:],reverse=True) )


i/p:
10 20 30 40 50 60 70
3
o/p:
[10, 20, 30, 70, 60, 50, 40]
