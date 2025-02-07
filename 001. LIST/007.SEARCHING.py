#SEARCHING

1. to know given element is present in list or not
2. to know index of the given element 

___________________________________________

1. to know given element is present in list or not

l=[40,30,10,22,99]
print(59 in l)              # FALSE
print(30 in l)              #TRUE

2. to know index of the given element 

SYNTAX:      list.index(element,startindex,endindex)

note1: if given element was not available then index fxn will throw error
note2: if given element occurs more than once then the result will index of first occurence

l=[40,30,10,22,99, 67,54,86,23]
print(l.index(22))             # 3
print(l.index(67,3,6))         # 5
print(l.index(67,3,4))         #VALUE ERROR
