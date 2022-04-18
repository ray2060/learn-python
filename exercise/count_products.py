import random as r

n = int(input('n: '))
k = int(input('k: '))
cnta = 0
cntb = 0
for i in range(n):
    if i % 1000 == 0:
        print(f'已计算至第{i}个数')
    a = r.randint(1, k)
    b = r.randint(1, k)
    c = a * b
    if c % 2 == 1:
        cnta += 1
    if c % 2 == 0:
        cntb += 1
print(f'奇数数：{cnta}， 偶数数：{cntb}')
