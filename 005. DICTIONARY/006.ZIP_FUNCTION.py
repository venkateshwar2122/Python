zip function can be use to create a Dictionary from Two given Lists

keys = ["name", "age", "dept", "place"]
values = ["venkatesh", 22, "cse", "hyd"]

d = dict(zip(keys, values))
print(d)

o/p:
{'name': 'venkatesh', 'age': 22, 'dept': 'cse', 'place': 'hyd'}
