1.   d.keys()             -> This returns all the keys in the dictionary.
2.   d.values()           -> This returns all the values in the dictionary.
3.   d.items()           ->  This returns all the key-value pairs as tuples inside a list.
_______________________

1. 

d = {"name": "venkatesh", "age": 22, "dept": "cse", "place": "hyd"}
print( d.keys())

o/p:
dict_keys(['name', 'age', 'dept', 'place'])
_________________________________________________
2.

d = {"name": "venkatesh", "age": 22, "dept": "cse", "place": "hyd"}
print(d.values())

o/p:
dict_values(['venkatesh', 22, 'cse', 'hyd'])

__________________________________________________

3.

d = {"name": "venkatesh", "age": 22, "dept": "cse", "place": "hyd"}
print( d.keys())

o/p:
dict_items([('name', 'venkatesh'), ('age', 22), ('dept', 'cse'), ('place', 'hyd')])








