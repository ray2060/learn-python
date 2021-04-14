import math


def get_numbers(d):
    lst = []
    for i in range(d):
        lst.append(float(input()))
    return lst

def compute(index, lst):
    return abs(lst[0][index] - lst[1][index]) ** 2

dimensionality = int(input())
ls = []
for i in range(2):
    ls.append(get_numbers(dimensionality))
ls2 = []
for i in range(dimensionality):
    ls2.append(compute(i, ls))
print('%.3f' % (math.sqrt(sum(ls2))))
