import random


MEAN = 36.5
SD = 0.2
DAYS = 14
PATH = '.\\body_temperature.txt'


'''
with open(PATH, 'w') as f:
    for elem in s:
        f.write('%.1f\n' % (elem,))
'''
for i in range(DAYS):
    r = random.gauss(MEAN, SD)
    print('%2d. %.1f' % (i + 1, r))
