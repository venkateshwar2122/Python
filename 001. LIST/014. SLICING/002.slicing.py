#What is Slicing?
Slicing is a technique in Python used to extract a portion of a sequence (like lists, tuples, strings, etc.) using the slice notation.of abo

___________________________________
#INDEXING
l=[10,20,30,40]
index of above list : 0,1,2,3  OR  -4,-3,-2,-1

____________________________________
#Syntax of Slicing:
sequence[start:stop-1:step]

where,
start → Index where slicing begins (inclusive).
stop → Index where slicing ends (exclusive).
step → The interval between elements (default is 1).

note:-
If start, stop, or step are omitted, Python fills in default values:-
start defaults to 0
stop defaults to the length of the sequence
step defaults to 1

__________________________________________

1. Slicing a List

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:5])              # Output: [30, 40, 50]  (Indexes 2 to 4)
_____________________________

2. Omitting Start or Stop

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[:4])   # Output: [10, 20, 30, 40]  (Start from 0 and go upto 3rd index)
print(numbers[3:])   # Output: [40, 50, 60, 70, 80, 90]  (Go till end)
print(numbers[:])    # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90] (Full list)

___________________________________
       
3. Using Step Value

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[1:7:2])  # Output: [20, 40, 60]  (Every second element)
print(numbers[::3])    # Output: [10, 40, 70]  (Every third element)

__________________________________

4. Negative Indexing
Python allows negative indexing:
-1 represents the last element
-2 represents the second last element, and so on

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]     
print(numbers[-5:-2])  # Output: [50, 60, 70]  (Counts from end)

________________________________________


5. Reverse a List Using Negative Step

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[::-1])  # Output: [90, 80, 70, 60, 50, 40, 30, 20, 10]  (Reverses list)

_______________________________________
       
6. Slicing a String
Slicing works on strings too!


text = "Hello, World!"
print(text[7:12])  # Output: "World"
print(text[:5])    # Output: "Hello"
print(text[::-1])  # Output: "!dlroW ,olleH" (Reversed string)

__________________________________________

7. Slicing a Tuple
Since tuples are immutable, you can only slice them (not modify them):


tuple_data = (1, 2, 3, 4, 5, 6, 7)
print(tuple_data[1:5])  # Output: (2, 3, 4, 5)

_______________________________________________

8. Using slice() Function
Instead of [:] notation, Python has a built-in slice() function:

data = [10, 20, 30, 40, 50]
s = slice(1, 4)   # Equivalent to [1:4]
print(data[s])    # Output: [20, 30, 40]

_________________________________________________

9. Modifying Lists Using Slicing
You can replace multiple values at once:

nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30, 40]
print(nums)  # Output: [1, 20, 30, 40, 5]

________________________________________________

10. Deleting Elements Using Slicing
You can delete multiple elements:


nums = [1, 2, 3, 4, 5]
del nums[1:4]
print(nums)  # Output: [1, 5]





