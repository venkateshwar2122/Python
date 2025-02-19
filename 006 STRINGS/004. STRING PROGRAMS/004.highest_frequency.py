# DISPLAY WHICH CHARCTER REPEATED HIGHEST TIME IN A GIVEBN STRING


s = "adddcdbadbcdb"
d = {}

for ch in s:
  d[ch] = d.get(ch,0) + 1

print(d)
print(sorted(d.items(),reverse=True,key=lambda x:x[1])[0])

O/P:
{'a': 2, 'd': 6, 'c': 2, 'b': 3}
('d', 6)
