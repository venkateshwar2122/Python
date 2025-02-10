l=[5,8,2,7,9,6,3,4,2,9,1]
print(l[::])
print(l[::-1])
print(l[5:])
print(l[::2])
print(l[len(l)-3 : ])                # [2, 9, 1]                    IMP
print(l[-3:])                        # [2, 9, 1]                    IMP
print(l[-3:-6])                      # []


# INDEXING IN ABOVE CODE

l = [5,  8,  2,  7,  9,  6,  3,  4,  2,  9,  1]
      0   1   2   3   4   5   6   7   8   9   10    (Positive Index)
    -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1     (Negative Index)


# EXPLANATION

1.

print(l[-3:-6])                      # []

why it had return empty list??

l[-3] refers to the 3rd last element
l[-6] refers to the 6th last element
Slicing Rule: l[start:stop]

start = -3  is after stop = -6 .
Since slicing moves left to right by default (+1 step), it cannot move backward from -3 to -6.
Note that, slicing only works forward unless a negative step is used.
Hence, Python returns an empty list [], meaning "no elements found in the forward direction."

_______________________________________

2.



