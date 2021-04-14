import numpy as np


MEAN = 36.5
SD = 0.2
DAYS = 14


s = np.random.normal(MEAN, SD, DAYS)
for i in range(len(s)):
    print('%2d. %.1f' % (i + 1, s[i]))
