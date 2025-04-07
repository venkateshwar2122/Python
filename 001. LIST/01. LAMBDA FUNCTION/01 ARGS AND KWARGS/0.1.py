1.  *args — Non-Keyword Variable-Length Arguments

*args allows a function to accept any number of positional arguments.

Inside the function, args is treated as a tuple.

✅ Example: Using *args
python
Copy
Edit
def add_all(*args):
    return sum(args)

print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))   # 15

🔍 Why use it?
When you don’t know how many numbers a user might pass in.

_____________________________________________________________________________________________________________
2.  **kwargs — Keyword Variable-Length Arguments

**kwargs allows a function to accept any number of keyword arguments.

Inside the function, kwargs is treated as a dictionary.

✅ Example: Using **kwargs
python
Copy
Edit
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=25, city="New York")
🖨 Output:
ini
Copy
Edit
name = Alice
age = 25
city = New York
___________________________________________________________________________________________________________________
3.  Combine *args and **kwargs:
python
Copy
Edit
def mixed_function(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

mixed_function(10, 20, 30, name="Alice", age=25)
Output:
ini
Copy
Edit
a = 10
args = (20, 30)
kwargs = {'name': 'Alice', 'age': 25}
___________________________________________________________________________________________________________________

NOTE : What is keyword argument????

🔹 What Are Keyword Arguments?
Keyword arguments are arguments that you pass to a function with a name (keyword), not just a value.

Instead of relying on the position, you specify which parameter you're assigning a value to.

✅ Syntax:
python
Copy
Edit

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(name="Alice", age=25)  # keyword arguments

🖨 Output:

Hello Alice, you are 25 years old.
