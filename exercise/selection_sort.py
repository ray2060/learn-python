s = input()
ls = s.split(' ')
sw = 0
for i in range(len(ls) - 1):
    minj = i
    for j in range(i + 1, len(ls)):
        if ls[j] < ls[minj]:
            minj = j
        if i == minj:
            continue
        ls[i], ls[minj] = ls[minj], ls[i]
        sw += 1
for i in range(len(ls)):
    print(ls[i], end=' ')
