#REVERSE STRING


s = "abcd"
r = ""         # dont forget to initialize r
for ch in s:
  r= ch + r     # "ch+r" and not "r+ch"

print(r)
