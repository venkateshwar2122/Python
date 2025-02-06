

 map(int, input().split())

The expression map(int, input().split()) is commonly used in Python to take 
multiple space-separated  integer inputs from the user. 
Here's how it works:

1.  input(): Takes the user input as a single string.
Example:

10 20 30 40

2.    .split(): Splits the input string into a list of substrings based on spaces (default delimiter).
Result:

['10', '20', '30', '40']

3.    map(int, ...): Applies the int() function to each element of the list, converting them from strings to integers.
Result:


map(int, ['10', '20', '30', '40'])  # This is an iterable of integers
________________________________________________________________________________
Usage Example:

# Input: 10 20 30 40
numbers = map(int, input().split())

# Converting map object to list for display
print(list(numbers))

Output:
[10, 20, 30, 40]

___________________________________________________________________

Common Use Case:
When assigning multiple variables:

a, b, c = map(int, input().split())
# Input: 5 15 25
# a = 5, b = 15, c = 25
_______________________________________________________________________

# WHAT IS MAP OBJECT ????

In Python, the map() function applies a specified function to each item of an iterable (such as a list, tuple, or string)
and returns a map object, which is an iterator. This allows for efficient processing of large datasets, as
items are produced on demand rather than all at once. 

Syntax:
map(function, iterable, *iterables)

WHERE,
function: A function that accepts as many arguments as there are iterable arguments.
iterable, *iterables: One or more iterable objects (e.g., lists, tuples).

Example:

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

EXPLANATION:
ITERATION 1 : 1**1=1
iteration2 : 2**2 = 4
iteration3: 3**2=9
iteration4: 4**2=16
iteration5: 5**2=25

In this example, the square function is applied to each item in the numbers list. The map object squared_numbers 
is then converted into a list to display the results.

It's important to note that in Python 3.x, map() returns a map object, which is an iterator. This means it 
computes its values on the fly and doesn't store them in memory. To retrieve the results, you can convert the
map object into a list or another iterable. 

________________________________________________________________________________________


Additionally, map() can accept multiple iterables. In such cases, the specified function should be
able to accept the same number of arguments as there are iterables. The function will be applied to the corresponding items of all iterables.

Example with Multiple Iterables:

def add(a, b):
    return a + b

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(add, list1, list2)

print(list(result))  # Output: [5, 7, 9]


explanation
Here, the add function takes two arguments and is applied to corresponding elements of list1 and list2.

