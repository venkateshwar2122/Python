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
