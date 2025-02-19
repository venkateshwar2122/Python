# check given string is palindrome or not ( without slicing)


s = "abcddcba"
flag=1
i=0
j=len(s)-1-i
while i<j:
 if(s[i]==s[j]):
  flag=1
  i=i+1
  j=len(s)-1-i
 else:
  flag=0
  break

if(flag==1):
  print("palindrome")
else:
  print("NOT PALINDROME")

o/p:
palindrome

NOTE: in above code dont use for loop, beacause for loop range goes from 0 to last, wheras we want range until i<j.
