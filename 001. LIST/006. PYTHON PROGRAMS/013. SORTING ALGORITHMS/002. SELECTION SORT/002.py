Selection Sort is a comparison-based sorting algorithm that repeatedly finds the smallest element("k") from 
the unsorted part of the list and swaps it with the first element("i") of that part.


  in bubble sort, hume jahan bada element milta tha use swap kar kar ke last index tak pahuchate they.
means in bubble sort there was always swapping, but whereas in selection sort hum sabse chote element ko variable "k" mai store karte hai
then hum uss k variable ko last index tak le jaakar "i" pointer(jo first index ko point kar raha hai) se swap kar dete hai, therefore in selection sort 1 baar mai 1 hi swap hota hai !




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
