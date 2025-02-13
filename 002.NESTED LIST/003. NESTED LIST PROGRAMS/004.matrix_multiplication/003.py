NOTE :
Conditions for Matrix Multiplication
For two matrices A and B to be multiplied:

The number of columns in Matrix A must be equal to the number of rows in Matrix B.
If A is of size (n × m) and B is of size (m × p), then:
Resultant Matrix C will have the size (n × p).
____________________________________________________________________

# Input size of the first matrix (n × m)
n, m = map(int, input("Enter dimensions of first matrix (rows columns): ").split())

# Input first matrix
A = []
print("Enter first matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# Input size of the second matrix (m × p)
p = int(input("Enter number of columns for second matrix: "))  # B has m rows and p columns

# Input second matrix
B = []
print("Enter second matrix:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

# Initialize result matrix (n × p) with zeros
C = []
for i in range(n):
    C.append([0] * p)  # Append a row of zeros for each row in C

# Perform matrix multiplication
for i in range(n):  # Iterate through rows of A
    for j in range(p):  # Iterate through columns of B
        for k in range(m):  # Iterate through the common dimension
           C[i][j] = C[i][j] + ( A[i][k] * B[k][j] ) # Multiply and sum

# Print the resulting matrix
print("Product of matrices:")
for row in C:
    print(*row)



o/p:
Enter dimensions of first matrix (rows columns): 2 3
Enter first matrix:
2 1 10
3 9 4
Enter number of columns for second matrix: 4
Enter second matrix:
7 1 9 3
1 3 7 6
9 2 1 8
Product of matrices:
105 25 35 92
66 38 94 95
___________________________________________

note in above code example:
no  of rows, column of A = 2, 3
no of rows ,column of B =3, 4
therfore no of rows,columns of C=2,4

now range of i is 0,1,2   ........since no of column of A is 3
now range of j is 0,1,2  .........since no of row of B is 3
now range of  k is 0,1,2,3 .......since no of column of B is 4
