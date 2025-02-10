l=[5,8,2,7,9,6,3,4,2,9,1]
print(l[::])
print(l[::-1])
print(l[5:])
print(l[::2])
print(l[len(l)-3 : ])                # [2, 9, 1]                    IMP
print(l[-3:])                        # [2, 9, 1]                    IMP
print(l[-3:-6])                      # []                           IMP
print(l[-3:-6:-1])                   # [2, 4, 3]                    IMP
print(l[-4:2:-1])                    # [4, 3, 6, 9, 7]               IMP
print(l[-4:2])                       # []                            IMP

#Syntax of Slicing:

sequence[start : stop-1 : step]


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
Since slicing moves left to right by default(+1 step) unless negative step is used,therefore  it cannot move backward from -3 to -6.
Note that, slicing only works forward UNLESS a negative step is used.
Hence, Python returns an empty list [], meaning "no elements found in the forward direction."

MY CONCLUSION:
formulae: moves left to right unless -ve step is used
here start=-3 and step=+1(default). 
Since no -ve step is used therefore it will always move from left to right.
means index -3 then index -2 then index -1
but here start=-3 and stop=-6
therefore its impossible to move backward

l = [5,  8,  2,  7,  9,  6,  3,  4,  2,  9,  1]
                                     -3              (Positive Index)
                         -6                            (Negative Index)

_______________________________________

2.

print(l[-3:-6:-1])                # [2, 4, 3]

MY CONCLUSION:
formulae: moves left to right unless -ve step is used
here start=-3 , step=-1 
since here -ve step is used therefore it can move backwards!!
here start=-3 and stop =-6
means index -3 then index -4 then index -5

_______________________________________________

3.

print(l[:-3])                        # [5, 8, 2, 7, 9, 6, 3, 4]      IMP

MY CONCLUSION:
formulae:moves left to right unless -ve step is used
here start=0(by default), step=+1(by default)
since here no -ve step is used therefore it will always move left to right
means start=0 to stop =-3


l = [5,  8,  2,  7,  9,  6,  3,  4,  2,  9,  1]
      0                                             (Positive Index)
                                     -3              (Negative Index)

__________________________________________________________

4.

print(l[-4:2:-1])                    # [4, 3, 6, 9, 7]               IMP

MY CONCLUSION:
formulae: moves left to right unless -ve step is used
here start = -4 and step=-1
since here -ve step is used therefore it can move backwards!!
here start=-4 and stop =2
means index -4 to  index 2

l = [5,  8,  2,  7,  9,  6,  3,  4,  2,  9,  1]
             2                                      (Positive Index)
                                 -4                 (Negative Index)


5. 

print(l[-4:2])                       # []                            IMP

MY CONCLUSION:
formulae: moves left  to right unless -ve step is used
here start=-4 and step=+1(by default)
Since no -ve step is used therefore it will always move from left to right.

but here start=-4 and stop=2
therefore its impossible to move backward


l = [5,  8,  2,  7,  9,  6,  3,  4,  2,  9,  1]
                                 -4                (Positive Index)
             2                                     (Negative Index)









