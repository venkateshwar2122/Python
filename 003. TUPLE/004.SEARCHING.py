t=(10,20,30,40,50)
print(50 in t)                 #true
print(t.index(20))             # 1
print(t.index(40,0,4))         # 3                SYNTAX: (ele, startindex, stopindex+1 )
print(t.index(40,0,2))         # VALUE ERROR BECAUSE 40 is not present in this ranger.
