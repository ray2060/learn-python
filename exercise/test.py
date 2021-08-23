import random as r
def test(start, stop, target, i = 0):
    while True:
        max_time = stop * 100
        r.seed(i)
        i += 1
        tmp = r.randrange(start, stop)
        if tmp == target:
            return True
        if i > max_time:
            break
    return False
