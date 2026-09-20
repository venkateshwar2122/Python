# Factorial — for loop

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)
________________________________________
Output:
120
Logic:
1 × 2 × 3 × 4 × 5 = 120
_________________________________________

#Factorial — Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
