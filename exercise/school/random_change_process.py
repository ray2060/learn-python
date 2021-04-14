import random


begin = float(input('Begin: '))
end = float(input('End: '))
how_many = int(input('How many: '))
sd = float(input('Fluctuation: '))
step = (end - begin) / (how_many + 1)
for i in range(how_many):
    r = begin + step * (i + 1) + random.gauss(0, sd)
    print('%2d. %.1f' % (i + 1, r))
