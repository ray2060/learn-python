res = []
def func(m):
    n = m
    if n > 200 or n == 1:
        return
    res.append(n)
    if n % 2 == 0 and (n - 1) % 3 == 0 and (n - 1) // 3 % 2 != 0:
        func((n - 1)// 3)
    func(n * 2)

def test():
    while True:
        global res
        res = []
        func(int(input('input:')))
        res.sort()
        print(res)
