/#Your Fibonacci — for loop
a = 0
b = 1
n = 10
sum = 0

print(a)
print(b)

for i in range(3, n + 1):    # 0 and 1 already printed
    sum = a + b
    print(sum)

    a = b
    b = sum
  __________________________________________________________________

#Your Fibonacci — Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
