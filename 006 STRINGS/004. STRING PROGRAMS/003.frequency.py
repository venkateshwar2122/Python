# calculate frequency of each character in given string

note:- in above question don't use list,because for that first u have to creat a list which is all filled with some random 
charcater(u cannot create an empty list beacuyse if u create an empty list and try to insert at ASCII index then it will give 
u index error as list is empty)....therfore this procedure is too lengthY!!!

USE DICTIONARY:-

s = "abcdaabcd"
dict = {}             #Empty dictionary

for ch in s:
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1

print(dict)

O/P:
{'a': 3, 'b': 2, 'c': 2, 'd': 2}

________________________
sirs method using dictionary:


s = "abcdaabcd"
d = {}

for ch in s:
  d[ch] = d.get(ch,0) + 1    # get fxn if founds the character(which is key) in dictionary then it will return that key's value,if not it will return 0

print(d)

o/p:
{'a': 3, 'b': 2, 'c': 2, 'd': 2}






