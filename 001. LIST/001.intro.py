
1. list is a collection of element, it may be homogenoeous(same type)  or hetrogeneous(different types) data.

homogeneous_list = [1, 2, 3, 4]                 # All integers
heterogeneous_list = [1, "Hello", 3.14, True]   # Mixed data types

2. list is mutable  meaning you can modify their content after creation means You can add, remove, or change elements.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"             # Modifying an element
fruits.append("orange")             # Adding an element
print(fruits)                       # Output: ['apple', 'blueberry', 'cherry', 'orange']



3. list support both positive and negative indexes
Positive Indexing: Starts from 0 (left to right).
Negative Indexing: Starts from -1 (right to left, accessing elements from the end).

numbers = [10, 20, 30, 40, 50]                 # 0,1,2,3,4     #-5,-4,-3,-2,-1
print(numbers[0])        # 10 (first element)
print(numbers[-1])       # 50 (last element)



4. list maintain data in insertion order
items = [3, 1, 4, 2, 5]
print(items)  # Output: [3, 1, 4, 2, 5]
