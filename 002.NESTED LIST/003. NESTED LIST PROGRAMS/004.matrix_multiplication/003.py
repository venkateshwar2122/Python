NOTE :
Conditions for Matrix Multiplication
For two matrices A and B to be multiplied:

The number of columns in Matrix A must be equal to the number of rows in Matrix B.
If A is of size (m × n) and B is of size (n × p), then:
Resultant Matrix C will have the size (m × p).
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
1 2 3
4 5 6
Enter number of columns for second matrix: 3
Enter second matrix:
9 6 7
5 3 4
2 4 3
Product of matrices:
25 24 24
73 63 66
