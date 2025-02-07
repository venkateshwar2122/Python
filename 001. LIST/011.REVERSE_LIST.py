# REVERSE LIST OF ELEMENTS

1. list.reverse()
2. using slice
___________________________

1. list.reverse()

l=[5,6,4,3,9]
l.reverse()
print(l)

o/p:
[9, 3, 4, 6, 5]

'''
NOTE: in above code dont reverse and print in the same line otherwise u will not get the output
                  l=[5,6,4,3,9]
                  print(l.reverse())            # dont do this

                  o/p: None
'''

2. using slice

l=[5,6,4,3,9]
print(l[ : :-1])     # list[startindex , stop index , step ]

o/p:  [9, 3, 4, 6, 5]

note: in above code the step is -1 means -ve therefore indexing will start from last. in normal conditionindexes--> [-5 -4 -3 -2 -1 ]   or [0 1 2 3 4]
