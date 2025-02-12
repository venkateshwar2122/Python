#METHOD 1
print('Enter number of lists in the nested list:')
r = int(input())  # Number of sublists
l = []

for i in range(r):
    print(f'Enter number of elements in list {i + 1}:')
    c = int(input())  # Number of elements in each sublist
    sub_list = []  # Create a new sublist  ********************************************************************

    for j in range(c):
        print(f'Enter element {j + 1}:')
        x = int(input())  # Read the element
        sub_list.append(x)  # Append to the sublist

    l.append(sub_list)  # Append sublist to main list

print('Final Nested List:', l)

O/P:
Enter number of lists in the nested list:
2
Enter number of elements in list 1:
3
Enter element 1:
10
Enter element 2:
20
Enter element 3:
30
Enter number of elements in list 2:
2
Enter element 1:
40
Enter element 2:
50
Final Nested List: [[10, 20, 30], [40, 50]]
________________________________________________

method 2 : USING LIST COMPREHENSION

r = int(input())  # Number of rows (sublists)
c = int(input())  # Number of columns (elements in each sublist)

# Using list comprehension to create the nested list
l = [[int(input()) for j in range(c)] for i in range(r)]

print(l)  # Printing the final nested list

Input:
2
3
1
2
3
4
5
6

Output:
[[1, 2, 3], [4, 5, 6]]

-----------------------------------------------------------------------------

METHOD 3 : TAKING ONE LIST AT A TIME IN SAME LINE FROM USER IN NESTED LIST

r = int(input())  # Number of lists
l = []

for i in range(r):
    l.append(list(map(int, input().split())))  # Read entire row as a list of integers

print(l)  # Print the nested list

Input:
3
1 2 3
4 5 6
7 8 9

Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]



 

