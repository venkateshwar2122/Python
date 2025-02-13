
NOTE:
if u want to create a tuple containing only single element and u write the below code then it will be WRONG

t=(5)
print(t)      # 5
type(t)       # int

output is int type and not tuple, becausein this case the python treat it as algebric expresssion and gives priority
to brackets and it removes brackets..thus only remaining is t=5
thus integer is assigned to t

__________________________________________________________

1. CREATE TUPLE WITH SINGLE ELEMENT

t=(5,)
print(t)       # (5,)
type(t)        # tuple
