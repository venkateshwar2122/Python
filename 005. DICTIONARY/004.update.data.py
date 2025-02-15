# TO ADD NEW KEY-VALUE IN DICTIONARY

SYNTAX1      d[key] = value

SYNTAX2      key.update({key:value})

note: if the given key was alraedy available, then old value gets replaced with new value.

_____________________________________________________________________


d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}

d[8] = 99
d["age"]= 47
d.update( {"phno":7987 , 3:30 , 4:40} )

print(d)

o/p:
{'name': 'venkatesh', 'age': 47, 'dept': 'cse', 'place': 'hyd', 8: 99, 'phno': 7987, 3: 30, 4: 40}
