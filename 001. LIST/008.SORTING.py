#SORTING 

1. sort()        ------> sort in first line and print in next line , modifies the original list
    a. ascending sort
    b. descending sort

2. sorted()      --------> sort and print in the same line , doesnot modifies the original list
    a. ascending sort
    b. descending sort

____________________

1. sort()

NOTE: sort() modifies the Original List

a. ascending sort

l=[5,8,7,2,3,8,3,4,1]
l.sort()                        # sorted first
print(l)                        # then printed

o/p: [1, 2, 3, 3, 4, 5, 7, 8, 8]

'''
NOTE: for above code don't sort and print in the same line:
              l=[5,8,7,2,3,8,3,4,1]
              print(l.sort())           #  DON'T SORT AND PRINT IN SAME LINE

              o/p: none                 # NOT GETTING OUTPUT
'''

b. descending sort

l=[5,8,7,2,3,8,3,4,1]
l.sort(reverse=True)    # T is capital
print(l)

o/p: [8, 8, 7, 5, 4, 3, 3, 2, 1]
_______________________________________________________________

2.SORTED

----> sorted and print in the same line

NOTE: sorted() Does Not Modify the Original List

l=[5,8,7,2,3,8,3,4,1]
print(sorted(l))                       # [1, 2, 3, 3, 4, 5, 7, 8, 8]
print(sorted(l,reverse=True))          #  [8, 8, 7, 5, 4, 3, 3, 2, 1]
print(l)                               # [5, 8, 7, 2, 3, 8, 3, 4, 1]



                            
