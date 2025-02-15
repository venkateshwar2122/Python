quel. display which element was repeated highest time in below list
         [5,8,7,5,7,5,5,7,3,7,8,9,7,4]
______________________________________________________________
l=[5,8,7,5,7,5,5,7,3,7,8,9,7,4]
d = {}

for i in l:
  d[i] = d.get(i,0) + 1
         
print(d)

l= sorted(d.items(), key=lambda x:x[1], reverse=True)          # sorting based on value not key
#the above sorting u have learned in topic 'NESTED LOOP" IN "sort by different elemnts" topic

print(l)
print(l[0][0])
_________________________________________________________________
o/p:
{5: 4, 8: 2, 7: 5, 3: 1, 9: 1, 4: 1}
[(7, 5), (5, 4), (8, 2), (3, 1), (9, 1), (4, 1)]
7





