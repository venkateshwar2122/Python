QUE. FIND second highest number from a given list

l = list(map(int, input().split()))

unique_l = list(set(l))  # Remove duplicates
unique_l.sort(reverse=True)  # Sort in descending order

if len(unique_l) > 1:
    print(unique_l[1])  # Second largest element
else:
    print("No second largest element")  # Edge case: All elements are the same



MINE METHOD-----------______________________________________________________
a = [860, 900, 800, 700, 850, 100, 200, 300, 400, 500]

max1 = a[0]
max2 = -1

for i in range(len(a)):

    if a[i] > max1:
        max2 = max1
        max1 = a[i]

    elif a[i] > max2 and a[i] != max1:
        max2 = a[i]

print(max2)
