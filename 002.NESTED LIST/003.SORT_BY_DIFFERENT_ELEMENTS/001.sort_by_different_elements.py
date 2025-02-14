NOTE: nestedlist = [ [list1 conatining id1,name1,age1]  ,  [list2 containing id2, name2, age2]  ,  [ list3 containing id3, name3, age3 ] ]

in above nested list if u perform sorting then by default the lists inside nestedlist will be sorted according to 
the first element which in this case is "id"

now , if u want to sort the lists inside the nested list acccording to other than first element, then how to do it??
___________________________________________________________________________________________________________


Question: Sorting Student Records Based on Multiple Criteria

You are given a list of student records, where each student has the following attributes:

Student ID (Integer)
Name (String)
Age (Integer)
Department (String)
Marks (Float)

Task:
Sorts and displays the records based on the following criteria:
1. By Name (Alphabetical Order)
2. By Age (Ascending Order)
3. By Marks (Descending Order)
4. By Department (Ascending Order), and if the department is the same, then by Marks (Descending Order)      ****IMP*****

example input list:
[[101, 'Alice', 22, 'CSE', 85.5], [102, 'Bob', 20, 'ECE', 90.0], [103, 'Charlie', 21, 'CSE', 92.0], [104, 'Dave', 23, 'ECE', 78.5]]
                                                                     
NOTE: sorted() doesn't modify the original list
_______________________________________________________________________________________________________

n = int(input("Enter number of records: "))  # Get the number of records
li = []

for i in range(n):
    try:
        print(f"\nEnter details for record {i + 1}:")
        student_id = int(input("Enter ID: "))           # ID (Integer)
        name = input("Enter Name: ")                    # Name (String)
        age = int(input("Enter Age: "))                 # Age (Integer)
        department = input("Enter Department: ")        # Department (String)
        marks = float(input("Enter Marks: "))          # Marks (Float)
        li.append([student_id, name, age, department, marks])
    except ValueError:
        print("Invalid input! Please enter values in the correct format.")
        exit()  # Stop execution if invalid input is found

print("\nOriginal List:")
print(li)

# Sorting by Name
sorted_by_name = sorted(li, key=lambda t: t[1])
print("\nSorted by Name:")
print(sorted_by_name)

# Sorting by Age
sorted_by_age = sorted(li, key=lambda t: t[2])
print("\nSorted by Age:")
print(sorted_by_age)

# Sorting by Marks in descending order
sorted_by_marks_desc = sorted(li, key=lambda t: t[4], reverse=True)
print("\nSorted by Marks (Descending Order):")
print(sorted_by_marks_desc)

# Sorted by Dept, if dept is same then sorted by marks (Descending)
sorted_by_dept_marks = sorted(li, key=lambda t: (t[3], -t[4]))                  # if u want dept to be ascending then just "t[3], t[4]" NO NEGATIVE SIGN REQUIRED
print("\nSorted by Dept, if dept is same then sorted by Marks (Descending):")
print(sorted_by_dept_marks)
_________________________________________________________________________________________________________________
                    
 INPUT:
                    
Enter number of records: 4

Enter details for record 1:
Enter ID: 101
Enter Name: Alice
Enter Age: 22
Enter Department: CSE
Enter Marks: 85.5

Enter details for record 2:
Enter ID: 102
Enter Name: Bob
Enter Age: 20
Enter Department: ECE
Enter Marks: 90.0

Enter details for record 3:
Enter ID: 103
Enter Name: Charlie
Enter Age: 21
Enter Department: CSE
Enter Marks: 92.0

Enter details for record 4:
Enter ID: 104
Enter Name: Dave
Enter Age: 23
Enter Department: ECE
Enter Marks: 78.5


OUTPUT:

Original List:
[[101, 'Alice', 22, 'CSE', 85.5], [102, 'Bob', 20, 'ECE', 90.0], [103, 'Charlie', 21, 'CSE', 92.0], [104, 'Dave', 23, 'ECE', 78.5]]

Sorted by Name:
[[101, 'Alice', 22, 'CSE', 85.5], [102, 'Bob', 20, 'ECE', 90.0], [103, 'Charlie', 21, 'CSE', 92.0], [104, 'Dave', 23, 'ECE', 78.5]]

Sorted by Age:
[[102, 'Bob', 20, 'ECE', 90.0], [103, 'Charlie', 21, 'CSE', 92.0], [101, 'Alice', 22, 'CSE', 85.5], [104, 'Dave', 23, 'ECE', 78.5]]

Sorted by Marks (Descending Order):
[[103, 'Charlie', 21, 'CSE', 92.0], [102, 'Bob', 20, 'ECE', 90.0], [101, 'Alice', 22, 'CSE', 85.5], [104, 'Dave', 23, 'ECE', 78.5]]

Sorted by Dept, if dept is same then sorted by Marks (Descending):
[[103, 'Charlie', 21, 'CSE', 92.0], [101, 'Alice', 22, 'CSE', 85.5], [102, 'Bob', 20, 'ECE', 90.0], [104, 'Dave', 23, 'ECE', 78.5]]


                    
