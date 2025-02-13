MATRIX ADDITION CONDITIONS:-

For matrix addition, the following conditions must be satisfied:

1. Same Dimensions:

Both matrices must have the same number of rows and columns.
If A is of size m×n, then B must also be of size  m×n.

2. Element-wise Addition:

Each element in the resulting matrix C is obtained by adding corresponding elements from A and B:

C[i][j]=A[i][j]+B[i][j]
__________________________________________________

NOTE: IN PYTHON 
 for matrix additon
   A + B = C

NOW,
A matrix:
1 2 3           # THIS FIRST ROW IS LIST1  OF A
4 5 6           # THIS SECOMD ROW IS LIST2 OF A

therfore in list format A would be look like this:-
A= [[1, 2, 3], [4, 5, 6]]


similarly,
B matrix:
7 8 9              # THIS FIRST ROW IS LIST1  OF B
10 11 12            # THIS FIRST ROW IS LIST2  OF B


therfore in list format B would be look like this:-
B= [[7, 8, 9], [10, 11, 12]]

THERFORE 
C = [ [ list1 of A + list1 of B ] , [ list2 of A + list2 of B ] ]

  




-----------------------------------------------------------------------------------------
que. add two matrix of order n*m


# Input size of matrix
n, m = map(int, input().split())  # Taking rows (n) and columns (m) as input

# Input first matrix
A = []
print("Enter first matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
#print(A)           ........here A= [[1, 2, 3], [4, 5, 6]]

# Input second matrix
B = []
print("Enter second matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

#print(B)       ........here B= [[7, 8, 9], [10, 11, 12]]

# Initialize result matrix
C = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])  # Add corresponding elements
    C.append(row)

#print(C)       .........here C= [[8, 10, 12], [14, 16, 18]]

# Print the resulting matrix
print("Sum of matrices:")
for row in C:
    print(*row)


O/P:
2 3
Enter first matrix:
1 2 3
4 5 6

Enter second matrix:
7 8 9
10 11 12

Sum of matrices:
8 10 12
14 16 18

