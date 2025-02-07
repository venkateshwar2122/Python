'''
display the index position of given elemnet , if its not present print -1
'''
'''
NOTE: WE HAVE USED FOR-ELSE LOOP INSTEAD OF TAKING A FLAG VARIABLE
'''

l=list(map(int,input().split()))             #input list 
k=int(input())                               #element to be searched              
for i in range(len(l)):
  if l[i]==k:
    print(i)
    break
else:
  print(-1)
