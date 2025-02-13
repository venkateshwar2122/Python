1. ACCESS PARTICULAR ELEMENT

t=(10,20,30,40,50)
print(t[3])

O/P:
40
________________________________________

2. ACCESS EACH ELEMENT

t=(10,20,30,40,50)
for i in t:
  print(i)


O/P:
10
20
30
40
50
____________________________________________

3. ACCESS EACH ELEMENT THROUGH INDEXING


t=(10,20,30,40,50)
for i in range(len(t)-1):
  print(t[i])

O/P:
10
20
30
40
50
______________________________________________________


4. DESTRUCTURING

t=(10,20,30,40,50)
print(*t)

O/P:
10 20 30 40 50

