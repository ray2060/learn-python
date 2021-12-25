def is_date(yr, dts):
    y = int(yr)
    m = int(dts[:2])
    d = int(dts[2:])
    if m in [1, 3, 5, 7, 8, 10, 12] and d > 0 and d < 32:
        return True
    if m in [4, 6, 9, 11] and d > 0 and d < 31:
        return True
    if m == 2:
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    if d > 0 and d < 30:
                        return True
                if d > 0 and d < 29:
                    return True
            if d > 0 and d < 30:
                return True
    return False

def sreverse(s):
    ret = ''
    for i in range(len(s) - 1, -1, -1):
        ret += s[i]
    return ret

num = 1
for i in range(1, 9999):
    ystr = '{:04d}'.format(i)
    dtstr = sreverse(ystr)
    if is_date(ystr, dtstr):
        print(num, ' ', ystr, dtstr, sep='', end='   ')
        num += 1
        if num % 3 == 1:
            print()
