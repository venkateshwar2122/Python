#extract all 'k' length sublists from a given list

l = list(map(int, input().split()))
k = int(input())

for i in range(len(l) - k + 1):               # "i" pointer should only go till 40 element one by one,see output
    print(l[i:i+k])

i/p:
10 20 30 40 50 60
3
o/p:
[10, 20, 30]
[20, 30, 40]
[30, 40, 50]
[40, 50, 60]
