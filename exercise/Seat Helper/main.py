import random

WEIGHT = [7594, 5063, 3375, 2250, 1500, 1000]
W_FACT = [float(s) for s in input('input W fact: ').split()]
NAME = [s for s in input('name: ').split()]
WILL = []
for i in range(len(NAME)):
    ts = input(f'input {NAME[i]}\'s will: ').split()
    WILL.append([int(s) for s in ts])

results = []
max_wei = -1

for i0 in range(6):
    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        wills = [WILL[0][i0], WILL[1][i1], WILL[2][i2], WILL[3][i3], WILL[4][i4], WILL[5][i5]]
                        if not (wills.count(1) == 1 and wills.count(2) == 1 and wills.count(3) == 1 and wills.count(4) == 1 and wills.count(5) == 1 and wills.count(6) == 1):
                            break
                        wei = WEIGHT[i0] * W_FACT[0] + WEIGHT[i1] * W_FACT[1] + WEIGHT[i2] * W_FACT[2] + WEIGHT[i3] * W_FACT[3] + WEIGHT[i4] * W_FACT[4] + WEIGHT[i5] * W_FACT[5]
                        if wei > max_wei:
                            results.clear()
                            max_wei = wei
                        if wei >= max_wei:
                            results.append(f'{NAME[0]}\'s will #{i0 + 1}, seat #{WILL[0][i0]}, weight {WEIGHT[i0] * W_FACT[0]}\n{NAME[1]}\'s will #{i1 + 1}, seat #{WILL[1][i1]}, weight {WEIGHT[i1] * W_FACT[1]}\n{NAME[2]}\'s will #{i2 + 1}, seat #{WILL[2][i2]}, weight {WEIGHT[i2] * W_FACT[2]}\n{NAME[3]}\'s will #{i3 + 1}, seat #{WILL[3][i3]}, weight {WEIGHT[i3] * W_FACT[3]}\n{NAME[4]}\'s will #{i4 + 1}, seat #{WILL[4][i4]}, weight {WEIGHT[i4] * W_FACT[4]}\n{NAME[5]}\'s will #{i5 + 1}, seat #{WILL[5][i5]}, weight {WEIGHT[i5] * W_FACT[5]}\n')

random.shuffle(results)
print(('-'*20 + '\n').join(results))
