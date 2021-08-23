s = input()
ls = s.split(' ')
for i in range(len(ls), 0, -1):
    for j in range(i - 1):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
for i in range(len(ls)):
    print(ls[i], end=' ')
