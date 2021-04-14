def fibonacci(n):
    if n <= 1:
        print(n)
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

for i in range(5):
    print(i, fibonacci(i))
