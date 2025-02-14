Selection Sort is a comparison-based sorting algorithm that repeatedly finds the smallest element("k") from 
the unsorted part of the list and swaps it with the first element("i") of that part.

l = list(map(int, input().split()))
for i in range(len(l)-1):
  k=i
  for j in range(i+1,len(l)):
    if l[k]>l[j]:
      k=j

  l[i],l[k]=l[k],l[i]
print(l)


i/p:
8 12 3 5  9 7 14
o/p:
[3, 5, 7, 8, 9, 12, 14]
