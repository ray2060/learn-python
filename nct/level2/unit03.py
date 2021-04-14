# factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n

print(fact(int(input())))

# fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

for i in range(int(input()) + 1):
    print(fibonacci(i))

# full alignment

def full_alignment(ls, start, end):
    if start == end:
        print(ls)
    else:
        for i in range(start, end+1):
            ls[start], ls[i] = ls[i], ls[start]
            full_alignment(ls, start+1, end)
            ls[i], ls[start] = ls[start], ls[i]

lst = eval(input())
full_alignment(lst, 0, len(lst)-1)
