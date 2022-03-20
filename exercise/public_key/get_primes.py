def get_primes(n, m, f):
    res = f.readlines()
    for i in range(n, m):
        if i % 10000 == 0:
            print(i)
        flag = 0
        for j in res:
            if j == '\n':
                continue
            if int(i) % int(j) == 0:
                flag = 1
        if flag == 0:
            res.append(str(i))
            res.append('\n')
            f.write(str(i) + '\n')
RANGE = 1, 19
with open('D:\\temp\\ray\\test.txt', mode='a+') as primes:
    print(2 ** RANGE[0], 2 ** RANGE[1])
    get_primes(2 ** RANGE[0], 2 ** RANGE[1], primes)

