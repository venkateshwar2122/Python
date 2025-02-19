1. Explicit Line Joining (\)

s = 'line1 
line 2'
print(s)         # ERROR

s = 'line1 \
line 2'
print(s)        #  line1 line 2

note: in above code the \ (backslash) at the end of the first line tells Python that the string continues on the next line.
The backslash itself is not included in the string; it simply allows breaking the line in the source code.

  ____________________________________________________________________

  2. IMPLICIT JOINING ( system apne aap join kar deta hai)

s = '''line1 
line2
line3 '''
print(s)

o/p:
line1 
line2
line3 


note : The triple-quoted string (''' or """) allows defining multi-line strings naturally.
Python automatically includes the newline characters (\n) at the places where you break the lines.

