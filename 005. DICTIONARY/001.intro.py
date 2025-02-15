1. Dictionary is collection of key-value pair.

2. In Python, dictionary keys must be unique and hashable. This means the key must be of an immutable data type. Some common 
immutable data types that can be used as dictionary keys are:
Strings (str)
Numbers (int, float, complex)
Tuples (only if all the elements inside the tuple are immutable)
Booleans (True, False)


3.  dictionaries in Python are mutable! 🎯 This means you can add, remove, or modify key-value pairs after 
the dictionary is created.


4. from Python versions (3.7+), dictionary has started to maintain insertion order.


5. In Python, Keys of Dictionary must be unique. If you try to create a dictionary 
with duplicate keys, the last occurrence of the key will overwrite any previous ones.

Example:

my_dict = {'a': 1, 'b': 2, 'a': 3}
print(my_dict)

Output:
{'a': 3, 'b': 2}

In the above example, the key 'a' appears twice. The second assignment ('a': 3) overwrites
the first ('a': 1), so only the last value (3) is retained for key 'a'.

Thus, if duplicate keys are provided, only the last inserted key-value pair is shown in the dictionary.

6. 0(1) complexity because it uses hashing to store keys


                         
