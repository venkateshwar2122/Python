What is a Lambda Function?
A lambda function is a small anonymous function (i.e., a function without a name).

It’s mainly used for short, one-line operations — typically when you need a function only once or for a short period.
______________________________________________
✅ Syntax:
python
Copy
Edit

lambda arguments: expression
_____________________________________________
🔧 Example 1: Simple Add Function
python
Copy
Edit

add = lambda a, b: a + b
print(add(5, 3))

🖨 Output:
Copy
Edit
8
_________________________________________________________________________
✅ Where Is It Used?
Lambda functions are commonly used with:

1. map()
Applies a function to every item in a list.

python
Copy
Edit
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

Output: [1, 4, 9, 16]

2. filter()
Filters items in a list based on a condition.

python
Copy
Edit
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

Output: [2, 4]

3. sorted() with key=
Used to sort based on a custom rule.

python
Copy
Edit
students = [('Alice', 85), ('Bob', 75), ('Charlie', 95)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

Output: [('Bob', 75), ('Alice', 85), ('Charlie', 95)]

✅ Example 4: In a Function Return
python
Copy
Edit
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
print(double(5))  # Output: 10

------*** VERY IMPORTANT BELOW *****_____________________
🔁 Comparison with Normal Function:
python
Copy
Edit
# Regular function
def square(x):
    return x * x

# Lambda function
square = lambda x: x * x
Both do the same thing, but the lambda is shorter.

______________________________________________________________

🧠 When to Use Lambda Functions?
Use When...	                                                  Avoid When...
You need a short, temporary function	                          The logic is complex
Using with map(), filter(), etc	                                The function needs reusability/naming
You want more concise code	                                    You need debugging or documentation
