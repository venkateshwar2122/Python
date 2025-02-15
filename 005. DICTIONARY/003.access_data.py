#ACCESS DATA FROM DICTIONARY

1. d[key]
-> if key was available then it's associated value would have been also present, if key was not available then it will
throw key error

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}
print(d["dept"])           # cse
print(d["marks"])          # KEYERROR
_____________________________________________________________________________________________
2.  d.get(key, defaultvalue)
->if key was avalable then its associated value will be given, if key was not available then default value will be given

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}
print(d.get("age",-1))        # 22
print(d.get("marks",-1))      # -1

___________________________________________________________________________________
3. membership operator

-> to verify given key in dictionary is available or not,we will use membership operator.

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}
print("age" in d)             # TRUE
print("marks" in d)           # FALSE
____________________________________________________________________________________________

4. Access keys with its associated values

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}

for k in d.keys():
  print(k,"--->",d[k])

o/p:
name ---> venkatesh
age ---> 22
dept ---> cse
place ---> hyd
__________________________________________________________________________________________

5. access only values

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}

for v in d.values():
  print(v)

o/p:
venkatesh
22
cse
hyd
________________________________________________________________________________________

5. Access keys with its associated values

d={"name":"venkatesh","age":22,"dept":"cse","place":"hyd"}

for k,v in d.items():         # note that d.items() holds list of key-value pair tuples
  print(k,"-->",v)

o/p:
name --> venkatesh
age --> 22
dept --> cse
place --> hyd

