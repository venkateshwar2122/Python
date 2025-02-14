que. In above code we used syntax for sortiing:
sorted(li, key=lambda t: (t[3], -t[4]))  

explain this syntax

ans.

The syntax:
sorted(li, key=lambda t: (t[3], -t[4]))
is used to sort a list of student records based on multiple criteria. Let's break it down step by step.

1.  sorted(iterable, key=function)
sorted() is a built-in Python function that sorts a list.
It takes two main parameters:
iterable → The list to be sorted (li in this case).
key=function → A function that defines how the elements should be sorted.

2. key=lambda t: (t[3], -t[4])
This part tells Python how to compare elements in the list.

 A) lambda t: ...
lambda creates an anonymous function (a small function without a name).
t represents each element in li (each student record).
lambda t: (t[3], -t[4]) returns a tuple that determines sorting.

 B) (t[3], -t[4])
This tuple is used as the sorting key:
t[3] → Sorts first by Department (Alphabetical order).
-t[4] → Sorts second by Marks in descending order (negative sign reverses order).  

Example Breakdown
Consider this list of students:
li = [
    [101, 'Alice', 22, 'CSE', 85.5],  
    [102, 'Bob', 20, 'ECE', 90.0],  
    [103, 'Charlie', 21, 'CSE', 92.0],  
    [104, 'Dave', 23, 'ECE', 78.5]  
]

Step 1: Extract Sorting Keys
For each student, the lambda function generates the sorting key:

(Department, -Marks)
# ('CSE', -85.5)  → Alice
# ('ECE', -90.0)  → Bob
# ('CSE', -92.0)  → Charlie
# ('ECE', -78.5)  → Dave

Step 2: Sorting Process
Sort by Department (t[3]):
"CSE" comes before "ECE" (since "CSE" < "ECE" in alphabetical order).
Sort by Marks (-t[4]) within the same department:
For "CSE", sort (-92.0, -85.5), so Charlie comes before Alice.
For "ECE", sort (-90.0, -78.5), so Bob comes before Dave.

Final Sorted List:
[
    [103, 'Charlie', 21, 'CSE', 92.0],  
    [101, 'Alice', 22, 'CSE', 85.5],  
    [102, 'Bob', 20, 'ECE', 90.0],  
    [104, 'Dave', 23, 'ECE', 78.5]  
]

Summary
sorted(li, key=lambda t: (t[3], -t[4])) sorts by:

Department (Ascending)
Marks (Descending within the same department)
The negative sign (-t[4]) is used to reverse the order of marks.

🔹 Without -t[4], it would sort marks ascending (lowest to highest).
🔹 With -t[4], it sorts marks descending (highest to lowest).
_________________________________________________________________________________

que.2. IF ITS STORED IN TUPLE THEN HOW THE OUTPUT IS A LIST???


the key function (the lambda) returns a tuple that is used internally to determine the order of the 
elements. However, the sorted() function itself always returns a new list containing the original elements 
in the sorted order.

Here's a breakdown:

Lambda Key Function:

The lambda lambda t: (t[3], -t[4]) takes each element (for example, a student record) and returns a tuple.
This tuple might look like ('CSE', -92.0) for a student.
This tuple is only used for comparison purposes during sorting.

sorted() Function:
The sorted() function uses the tuples produced by the lambda to decide the order of the elements.
Regardless of what the key function returns, sorted() returns a list containing the original elements (not the tuples). # already i studies in list

Output:
The output is still a list of student records, sorted according to the criteria defined by the tuple.

Example
Given:
li = [
    [101, 'Alice', 22, 'CSE', 85.5],
    [102, 'Bob', 20, 'ECE', 90.0],
    [103, 'Charlie', 21, 'CSE', 92.0],
    [104, 'Dave', 23, 'ECE', 78.5]
]

When you run the below code:
sorted_by_dept_marks = sorted(li, key=lambda t: (t[3], -t[4]))
print(sorted_by_dept_marks)

The lambda returns tuples like:
For Alice: ('CSE', -85.5)
For Bob: ('ECE', -90.0)
For Charlie: ('CSE', -92.0)
For Dave: ('ECE', -78.5)
These tuples are used to sort the list, but the resulting output is still a list of the 
original records, just arranged in sorted order.

Conclusion
Even though the key function returns a tuple, the sorted() function itself produces a list as its output, preserving 
the data type of your original elements.

  
