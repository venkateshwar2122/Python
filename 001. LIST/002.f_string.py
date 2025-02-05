refer FSTRINGS IN W3 SCHOOL FOR MORE DETAILS


F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

Before Python 3.6 we had to use the format() method.

___________________________________________________________
F-string allows you to format selected parts of a string.
______________________________________________________________________________________

To specify a string as an f-string, simply put an f in front of the string literal, like this:

txt = f"The price is 49 dollars"
print(txt)                             # The price is 49 dollars
______________________________________________________________________

Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)                          #The price is 59 dollars

__________________________________________________________________________________

A placeholder can also include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

Example
Display the price with 2 decimals:

price = 59
print(type(price))                          #<class 'int'>
txt = f"The price is {price:.2f} dollars"
print(txt)                                   #The price is 59.00 dollars
print(type(price))                           #<class 'int'>



NOTE: IN ABOVE CODE: 
f"{price:.2f}" only affects the display, not the actual data type.
The original price variable is still an integer (int).

___________________________________________________________________________________________________________________________


SIR'S CODE

a = int(input("enter a value"))
b = int(input("enter b value"))
print("sum of",a,"and",b,"is",a+b)           # sum of 10 and 20 is 30
print(f"diff of {a} and {b} is {a-b}")       # diff of 10 and 20 is -10
print("prod of {},{} is {}".format(a,b,a*b))   # prod of 10,20 is 200
print("float div of %d,%d is %f"%(a,b,a/b))    # float div of 10,20 is 0.500000
print(f"floor div of {a},{b} is {a//b}")       # floor div of 10,20 is 0
print(f"mod div of {a},{b} is {a%b}")          # mod div of 10,20 is 10
print(f"{a} power {b} is {a**b}")              # 10 power 20 is 100000000000000000000


____________________________________________________________________________________________________________

X
