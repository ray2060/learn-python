def func1(n):
    a = n
    def func2():
        nonlocal a
        b = a * a
        return b
    return func2()
