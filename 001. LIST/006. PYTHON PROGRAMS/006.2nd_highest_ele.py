QUE. FIND second highest number from a given list

l = list(map(int, input().split()))

unique_l = list(set(l))  # Remove duplicates
unique_l.sort(reverse=True)  # Sort in descending order

if len(unique_l) > 1:
    print(unique_l[1])  # Second largest element
else:
    print("No second largest element")  # Edge case: All elements are the same
